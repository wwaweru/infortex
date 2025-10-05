from django.db import models
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from wagtail import blocks
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from modelcluster.fields import ParentalKey


class ServicesIndexPage(Page):
    intro = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]
    
    def get_context(self, request):
        context = super().get_context(request)
        services = self.get_children().live().order_by('-first_published_at')
        context['services'] = services
        return context


class ServicePage(Page):
    description = RichTextField()
    service_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    price_starting_from = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    duration = models.CharField(max_length=100, blank=True, help_text="e.g., 1-3 days, Same day delivery")
    coverage_area = models.CharField(max_length=200, blank=True, help_text="e.g., Nairobi, Kenya, East Africa")
    
    # Features list
    features = StreamField([
        ('feature', blocks.CharBlock(max_length=100)),
    ], blank=True, use_json_field=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('service_image'),
        FieldPanel('price_starting_from'),
        FieldPanel('duration'),
        FieldPanel('coverage_area'),
        FieldPanel('features'),
    ]
    
    parent_page_types = ['services.ServicesIndexPage']


class ServiceFeature(Orderable):
    page = ParentalKey(ServicePage, on_delete=models.CASCADE, related_name='service_features')
    feature = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    
    panels = [
        FieldPanel('feature'),
        FieldPanel('description'),
    ]
