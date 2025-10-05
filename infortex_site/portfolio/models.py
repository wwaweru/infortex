from django.db import models
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from modelcluster.fields import ParentalKey


class PortfolioIndexPage(Page):
    intro = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]
    
    def get_context(self, request):
        context = super().get_context(request)
        projects = self.get_children().live().order_by('-first_published_at')
        context['projects'] = projects
        return context


class PortfolioPage(Page):
    client_name = models.CharField(max_length=200)
    project_type = models.CharField(max_length=100, help_text="e.g., Freight Transport, Warehousing, Last Mile Delivery")
    project_duration = models.CharField(max_length=100, blank=True)
    completion_date = models.DateField()
    
    description = RichTextField()
    challenge = RichTextField(blank=True, help_text="What challenges did this project address?")
    solution = RichTextField(blank=True, help_text="How did we solve the challenge?")
    results = RichTextField(blank=True, help_text="What were the outcomes?")
    
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('client_name'),
            FieldPanel('project_type'),
            FieldPanel('project_duration'),
            FieldPanel('completion_date'),
        ], heading="Project Details"),
        
        FieldPanel('featured_image'),
        FieldPanel('description'),
        FieldPanel('challenge'),
        FieldPanel('solution'),
        FieldPanel('results'),
        InlinePanel('gallery_images', label="Gallery Images"),
    ]
    
    parent_page_types = ['portfolio.PortfolioIndexPage']


class PortfolioGalleryImage(Orderable):
    page = ParentalKey(PortfolioPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+'
    )
    caption = models.CharField(max_length=250, blank=True)
    
    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]


class TestimonialSnippet(models.Model):
    client_name = models.CharField(max_length=200)
    client_position = models.CharField(max_length=200, blank=True)
    client_company = models.CharField(max_length=200, blank=True)
    testimonial = models.TextField()
    client_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    panels = [
        FieldPanel('client_name'),
        FieldPanel('client_position'),
        FieldPanel('client_company'),
        FieldPanel('testimonial'),
        FieldPanel('client_image'),
    ]
    
    def __str__(self):
        return f"{self.client_name} - {self.client_company}"
    
    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
