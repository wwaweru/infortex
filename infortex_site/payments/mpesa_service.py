import requests
import base64
import json
from datetime import datetime
from django.conf import settings
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)


class MpesaService:
    """
    M-Pesa Daraja API integration service
    """
    
    def __init__(self):
        # These should be set in Django settings
        self.consumer_key = getattr(settings, 'MPESA_CONSUMER_KEY', '')
        self.consumer_secret = getattr(settings, 'MPESA_CONSUMER_SECRET', '')
        self.business_short_code = getattr(settings, 'MPESA_BUSINESS_SHORT_CODE', '')
        self.passkey = getattr(settings, 'MPESA_PASSKEY', '')
        self.callback_url = getattr(settings, 'MPESA_CALLBACK_URL', '')
        self.environment = getattr(settings, 'MPESA_ENVIRONMENT', 'sandbox')  # 'sandbox' or 'production'
        
        # API URLs
        if self.environment == 'production':
            self.base_url = "https://api.safaricom.co.ke"
        else:
            self.base_url = "https://sandbox.safaricom.co.ke"
        
        self.oauth_url = f"{self.base_url}/oauth/v1/generate?grant_type=client_credentials"
        self.stk_push_url = f"{self.base_url}/mpesa/stkpush/v1/processrequest"
        self.query_url = f"{self.base_url}/mpesa/stkpushquery/v1/query"
    
    def get_access_token(self):
        """Get OAuth access token from M-Pesa API"""
        try:
            credentials = f"{self.consumer_key}:{self.consumer_secret}"
            encoded_credentials = base64.b64encode(credentials.encode()).decode()
            
            headers = {
                'Authorization': f'Basic {encoded_credentials}',
                'Content-Type': 'application/json'
            }
            
            response = requests.get(self.oauth_url, headers=headers, timeout=30)
            response.raise_for_status()
            
            result = response.json()
            return result.get('access_token')
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error getting M-Pesa access token: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error getting access token: {e}")
            return None
    
    def generate_password(self):
        """Generate password for STK push"""
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        password_string = f"{self.business_short_code}{self.passkey}{timestamp}"
        password = base64.b64encode(password_string.encode()).decode()
        return password, timestamp
    
    def initiate_stk_push(self, phone_number, amount, account_reference, transaction_desc):
        """
        Initiate STK Push payment
        
        Args:
            phone_number (str): Customer phone number (254XXXXXXXXX)
            amount (float): Amount to be paid
            account_reference (str): Account reference for the transaction
            transaction_desc (str): Description of the transaction
            
        Returns:
            dict: Response from M-Pesa API
        """
        access_token = self.get_access_token()
        if not access_token:
            return {'success': False, 'message': 'Failed to get access token'}
        
        password, timestamp = self.generate_password()
        
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        
        payload = {
            "BusinessShortCode": self.business_short_code,
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": int(float(amount)),
            "PartyA": phone_number,
            "PartyB": self.business_short_code,
            "PhoneNumber": phone_number,
            "CallBackURL": self.callback_url,
            "AccountReference": account_reference,
            "TransactionDesc": transaction_desc
        }
        
        try:
            response = requests.post(
                self.stk_push_url,
                json=payload,
                headers=headers,
                timeout=30
            )
            response.raise_for_status()
            
            result = response.json()
            logger.info(f"STK Push initiated: {result}")
            
            return {
                'success': True,
                'checkout_request_id': result.get('CheckoutRequestID'),
                'merchant_request_id': result.get('MerchantRequestID'),
                'response_code': result.get('ResponseCode'),
                'response_description': result.get('ResponseDescription'),
                'customer_message': result.get('CustomerMessage')
            }
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error initiating STK push: {e}")
            return {'success': False, 'message': f'Request error: {str(e)}'}
        except Exception as e:
            logger.error(f"Unexpected error in STK push: {e}")
            return {'success': False, 'message': f'Unexpected error: {str(e)}'}
    
    def query_stk_status(self, checkout_request_id):
        """
        Query STK Push transaction status
        
        Args:
            checkout_request_id (str): CheckoutRequestID from STK push response
            
        Returns:
            dict: Transaction status response
        """
        access_token = self.get_access_token()
        if not access_token:
            return {'success': False, 'message': 'Failed to get access token'}
        
        password, timestamp = self.generate_password()
        
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        
        payload = {
            "BusinessShortCode": self.business_short_code,
            "Password": password,
            "Timestamp": timestamp,
            "CheckoutRequestID": checkout_request_id
        }
        
        try:
            response = requests.post(
                self.query_url,
                json=payload,
                headers=headers,
                timeout=30
            )
            response.raise_for_status()
            
            result = response.json()
            logger.info(f"STK Query result: {result}")
            
            return {
                'success': True,
                'result_code': result.get('ResultCode'),
                'result_desc': result.get('ResultDesc'),
                'checkout_request_id': result.get('CheckoutRequestID'),
                'merchant_request_id': result.get('MerchantRequestID')
            }
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying STK status: {e}")
            return {'success': False, 'message': f'Request error: {str(e)}'}
        except Exception as e:
            logger.error(f"Unexpected error in STK query: {e}")
            return {'success': False, 'message': f'Unexpected error: {str(e)}'}
    
    def process_callback(self, callback_data):
        """
        Process M-Pesa callback data
        
        Args:
            callback_data (dict): Callback data from M-Pesa
            
        Returns:
            dict: Processed callback information
        """
        try:
            stk_callback = callback_data.get('Body', {}).get('stkCallback', {})
            
            result = {
                'checkout_request_id': stk_callback.get('CheckoutRequestID'),
                'merchant_request_id': stk_callback.get('MerchantRequestID'),
                'result_code': stk_callback.get('ResultCode'),
                'result_desc': stk_callback.get('ResultDesc')
            }
            
            # If payment was successful, extract transaction details
            if result['result_code'] == 0:
                callback_metadata = stk_callback.get('CallbackMetadata', {})
                items = callback_metadata.get('Item', [])
                
                for item in items:
                    name = item.get('Name')
                    value = item.get('Value')
                    
                    if name == 'Amount':
                        result['amount'] = value
                    elif name == 'MpesaReceiptNumber':
                        result['mpesa_receipt_number'] = value
                    elif name == 'TransactionDate':
                        # Convert timestamp to datetime
                        if value:
                            result['transaction_date'] = datetime.fromtimestamp(value / 1000)
                    elif name == 'PhoneNumber':
                        result['phone_number'] = value
            
            return result
            
        except Exception as e:
            logger.error(f"Error processing M-Pesa callback: {e}")
            return None


# Utility functions
def format_phone_number(phone):
    """Format phone number for M-Pesa API"""
    if not phone:
        return None
    
    # Remove any non-digit characters except +
    phone = ''.join(char for char in phone if char.isdigit() or char == '+')
    
    # Remove + if present
    phone = phone.replace('+', '')
    
    # Handle Kenyan phone numbers
    if phone.startswith('0'):
        phone = '254' + phone[1:]
    elif not phone.startswith('254'):
        phone = '254' + phone
    
    # Validate length (should be 12 digits for Kenyan numbers)
    if len(phone) != 12:
        return None
    
    return phone


def validate_amount(amount):
    """Validate payment amount"""
    try:
        amount = float(amount)
        if amount <= 0:
            return False, "Amount must be greater than 0"
        if amount > 150000:  # M-Pesa transaction limit
            return False, "Amount exceeds M-Pesa transaction limit (150,000 KSh)"
        return True, amount
    except (ValueError, TypeError):
        return False, "Invalid amount format"