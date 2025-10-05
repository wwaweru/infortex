from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def contact_form_submission(request):
    """Handle contact form submissions"""
    if request.method == 'POST':
        try:
            # Get form data
            name = request.POST.get('name', '').strip()
            email = request.POST.get('email', '').strip()
            phone = request.POST.get('phone', '').strip()
            service = request.POST.get('service', '').strip()
            subject = request.POST.get('subject', '').strip()
            message = request.POST.get('message', '').strip()
            
            # Basic validation
            if not all([name, email, subject, message]):
                messages.error(request, 'Please fill in all required fields.')
                return redirect('/contact/')
            
            # Create email content
            email_subject = f"Contact Form: {subject}"
            email_message = f"""
New contact form submission from {name}

Name: {name}
Email: {email}
Phone: {phone or 'Not provided'}
Service Interest: {service or 'Not specified'}
Subject: {subject}

Message:
{message}

---
This message was sent from the Infortex Solutions website contact form.
            """
            
            # Send email
            try:
                send_mail(
                    email_subject,
                    email_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.ADMIN_EMAIL],
                    fail_silently=False,
                )
                
                # Send confirmation email to user
                confirmation_subject = "Thank you for contacting Infortex Solutions"
                confirmation_message = f"""
Dear {name},

Thank you for contacting Infortex Solutions Limited. We have received your message and will get back to you within 24 hours.

Your inquiry details:
Subject: {subject}
Service Interest: {service or 'General inquiry'}

We appreciate your interest in our logistics services.

Best regards,
Infortex Solutions Limited Team
                """
                
                send_mail(
                    confirmation_subject,
                    confirmation_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=True,
                )
                
                messages.success(request, 'Thank you! Your message has been sent successfully. We will get back to you soon.')
                
            except Exception as e:
                messages.error(request, 'Sorry, there was an error sending your message. Please try again or contact us directly.')
                print(f"Email error: {e}")  # For debugging
                
        except Exception as e:
            messages.error(request, 'Sorry, there was an error processing your request. Please try again.')
            print(f"Form processing error: {e}")  # For debugging
            
        return redirect('/contact/')
    
    return redirect('/contact/')
