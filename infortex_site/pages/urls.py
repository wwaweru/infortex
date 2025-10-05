from django.urls import path
from . import views

urlpatterns = [
    path('contact/submit/', views.contact_form_submission, name='contact_form_submission'),
]