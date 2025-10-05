from django.contrib import admin
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from .models import TestimonialSnippet


class TestimonialAdmin(SnippetViewSet):
    model = TestimonialSnippet
    menu_label = 'Testimonials'
    icon = 'openquote'
    list_display = ('client_name', 'client_company', 'created_at')
    list_filter = ('created_at', 'client_company')
    search_fields = ('client_name', 'client_company', 'testimonial')


register_snippet(TestimonialSnippet, TestimonialAdmin)
