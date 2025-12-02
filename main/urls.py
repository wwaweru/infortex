from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('team/', views.team, name='team'),
    path('careers/', views.careers, name='careers'),
    path('certifications/', views.certifications, name='certifications'),
    path('booking/', views.booking, name='booking'),
    path('gallery/', views.gallery, name='gallery'),
    path('faq/', views.faq, name='faq'),
    path('track/', views.track, name='track'),
    path('testimonials/', views.testimonials, name='testimonials'),
]