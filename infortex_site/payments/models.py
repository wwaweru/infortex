from django.db import models
from django.contrib.auth.models import User
import uuid


class MpesaPayment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('cancelled', 'Cancelled'),
    ]
    
    TRANSACTION_TYPE_CHOICES = [
        ('service_payment', 'Service Payment'),
        ('booking_payment', 'Booking Payment'),
        ('quote_payment', 'Quote Payment'),
    ]
    
    # Primary identifiers
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transaction_id = models.CharField(max_length=100, unique=True, blank=True)
    checkout_request_id = models.CharField(max_length=100, blank=True)
    
    # User and payment details
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    phone_number = models.CharField(max_length=15, help_text="Format: 254XXXXXXXXX")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPE_CHOICES, default='service_payment')
    description = models.CharField(max_length=200)
    
    # M-Pesa response fields
    mpesa_receipt_number = models.CharField(max_length=50, blank=True)
    transaction_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    result_code = models.CharField(max_length=10, blank=True)
    result_description = models.TextField(blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Additional data
    metadata = models.JSONField(default=dict, blank=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "M-Pesa Payment"
        verbose_name_plural = "M-Pesa Payments"
    
    def __str__(self):
        return f"Payment {self.transaction_id} - {self.amount} KSh"
    
    @property
    def is_successful(self):
        return self.status == 'completed' and self.result_code == '0'
    
    @property
    def formatted_phone(self):
        """Format phone number for M-Pesa API"""
        phone = self.phone_number.replace('+', '').replace(' ', '').replace('-', '')
        if phone.startswith('0'):
            phone = '254' + phone[1:]
        elif not phone.startswith('254'):
            phone = '254' + phone
        return phone


class PaymentService(models.Model):
    """Define services available for payment"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - KSh {self.base_price}"


class PaymentCallback(models.Model):
    """Store M-Pesa callback responses for debugging"""
    payment = models.ForeignKey(MpesaPayment, on_delete=models.CASCADE, related_name='callbacks')
    callback_type = models.CharField(max_length=20)  # 'confirmation' or 'validation'
    raw_data = models.JSONField()
    processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Callback {self.callback_type} for {self.payment.transaction_id}"
