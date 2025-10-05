from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail import blocks
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.images.blocks import ImageChooserBlock


class HomePage(Page):
    # Hero Section
    hero_title = models.CharField(max_length=200, default="Professional Logistics & Cargo Services in Kenya")
    hero_subtitle = models.CharField(max_length=300, default="Your trusted partner for reliable transportation and delivery solutions across Kenya and East Africa.")
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    hero_cta_text = models.CharField(max_length=50, default="Get Quote")
    hero_cta_url = models.URLField(blank=True, default="#contact")
    
    # Services Overview Section
    services_title = models.CharField(max_length=200, default="Our Services")
    services_subtitle = models.CharField(max_length=300, default="Comprehensive logistics solutions tailored to your business needs")
    
    # About Section
    about_title = models.CharField(max_length=200, default="About Infortex Solutions")
    about_content = RichTextField(
        default="At Infortex Solutions Limited, we are dedicated to providing exceptional logistics and cargo services throughout Kenya. With years of experience in the industry, we understand the unique challenges of transportation and delivery in East Africa."
    )
    about_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    # Statistics Section
    years_experience = models.IntegerField(default=10)
    satisfied_clients = models.IntegerField(default=500)
    deliveries_completed = models.IntegerField(default=10000)
    coverage_areas = models.IntegerField(default=47)
    
    # Call to Action Section
    cta_title = models.CharField(max_length=200, default="Ready to Get Started?")
    cta_subtitle = models.CharField(max_length=300, default="Contact us today for a free quote and discover how we can help streamline your logistics needs.")
    cta_button_text = models.CharField(max_length=50, default="Contact Us")
    
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('hero_title'),
            FieldPanel('hero_subtitle'),
            FieldPanel('hero_image'),
            FieldPanel('hero_cta_text'),
            FieldPanel('hero_cta_url'),
        ], heading="Hero Section"),
        
        MultiFieldPanel([
            FieldPanel('services_title'),
            FieldPanel('services_subtitle'),
        ], heading="Services Section"),
        
        MultiFieldPanel([
            FieldPanel('about_title'),
            FieldPanel('about_content'),
            FieldPanel('about_image'),
        ], heading="About Section"),
        
        MultiFieldPanel([
            FieldPanel('years_experience'),
            FieldPanel('satisfied_clients'),
            FieldPanel('deliveries_completed'),
            FieldPanel('coverage_areas'),
        ], heading="Statistics"),
        
        MultiFieldPanel([
            FieldPanel('cta_title'),
            FieldPanel('cta_subtitle'),
            FieldPanel('cta_button_text'),
        ], heading="Call to Action"),
    ]
    
    class Meta:
        verbose_name = "Home Page"
