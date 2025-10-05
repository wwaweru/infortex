from django.db import models
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from wagtail import blocks
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.panels import FormSubmissionsPanel
from modelcluster.fields import ParentalKey


class StandardPage(Page):
    """Standard content page with rich text and optional images."""
    body = RichTextField(blank=True)
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('featured_image'),
        FieldPanel('body'),
    ]


class AboutPage(Page):
    """About page with company information."""
    intro = RichTextField(blank=True)
    body = RichTextField(blank=True)
    
    # Mission, Vision, Values
    mission = RichTextField(blank=True)
    vision = RichTextField(blank=True)
    values = RichTextField(blank=True)
    
    # Company stats
    founded_year = models.IntegerField(null=True, blank=True)
    employees_count = models.IntegerField(null=True, blank=True)
    
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('featured_image'),
        FieldPanel('intro'),
        FieldPanel('body'),
        
        MultiFieldPanel([
            FieldPanel('mission'),
            FieldPanel('vision'),
            FieldPanel('values'),
        ], heading="Mission, Vision & Values"),
        
        MultiFieldPanel([
            FieldPanel('founded_year'),
            FieldPanel('employees_count'),
        ], heading="Company Information"),
        
        InlinePanel('team_members', label="Team Members"),
    ]


class TeamMember(Orderable):
    page = ParentalKey(AboutPage, on_delete=models.CASCADE, related_name='team_members')
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    panels = [
        FieldPanel('name'),
        FieldPanel('position'),
        FieldPanel('bio'),
        FieldPanel('image'),
    ]


class ContactFormField(AbstractFormField):
    page = ParentalKey('ContactPage', on_delete=models.CASCADE, related_name='form_fields')


class ContactPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)
    
    # Contact information
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    
    # Business hours
    business_hours = RichTextField(blank=True)
    
    # Map embed
    map_embed = models.TextField(blank=True, help_text="Google Maps embed code")
    
    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text'),
        FormSubmissionsPanel(),
        
        MultiFieldPanel([
            FieldPanel('address'),
            FieldPanel('phone'),
            FieldPanel('email'),
            FieldPanel('business_hours'),
        ], heading="Contact Information"),
        
        FieldPanel('map_embed'),
    ]


class FAQPage(Page):
    intro = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        InlinePanel('faq_items', label="FAQ Items"),
    ]


class FAQItem(Orderable):
    page = ParentalKey(FAQPage, on_delete=models.CASCADE, related_name='faq_items')
    question = models.CharField(max_length=300)
    answer = RichTextField()
    
    panels = [
        FieldPanel('question'),
        FieldPanel('answer'),
    ]
