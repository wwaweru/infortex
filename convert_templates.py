#!/usr/bin/env python3
import os
import re

def convert_html_to_django_template(filepath):
    """Convert static HTML to Django template format"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add Django template header
    content = '{% load static %}\n' + content
    
    # Replace static file references
    replacements = [
        # CSS files
        (r'href="css/', r'href="{% static \'css/'),
        (r'\.css"', r'.css\' %}"'),
        
        # JS files  
        (r'src="js/', r'src="{% static \'js/'),
        (r'\.js"', r'.js\' %}"'),
        
        # Images
        (r'src="images/', r'src="{% static \'images/'),
        (r'data-bgimage="url\(images/', r'data-bgimage="url({% static \'images/'),
        (r'\.webp"', r'.webp\' %}"'),
        (r'\.png"', r'.png\' %}"'),
        (r'\.jpg"', r'.jpg\' %}"'),
        (r'\.svg"', r'.svg\' %}"'),
        (r'\.webp\)"', r'.webp\' %})"'),
        (r'\.png\)"', r'.png\' %})"'),
        (r'\.jpg\)"', r'.jpg\' %})"'),
        
        # Fonts
        (r'href="fonts/', r'href="{% static \'fonts/'),
    ]
    
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)
    
    # Replace navigation URLs with Django URL tags
    url_replacements = [
        (r'href="index\.html"', r'href="{% url \'home\' %}"'),
        (r'href="about\.html"', r'href="{% url \'about\' %}"'),
        (r'href="services\.html"', r'href="{% url \'services\' %}"'),
        (r'href="contact\.html"', r'href="{% url \'contact\' %}"'),
        (r'href="blog\.html"', r'href="{% url \'blog\' %}"'),
        (r'href="team\.html"', r'href="{% url \'team\' %}"'),
        (r'href="careers\.html"', r'href="{% url \'careers\' %}"'),
        (r'href="certifications\.html"', r'href="{% url \'certifications\' %}"'),
        (r'href="booking\.html"', r'href="{% url \'booking\' %}"'),
        (r'href="gallery\.html"', r'href="{% url \'gallery\' %}"'),
        (r'href="faq\.html"', r'href="{% url \'faq\' %}"'),
        (r'href="track\.html"', r'href="{% url \'track\' %}"'),
    ]
    
    for pattern, replacement in url_replacements:
        content = re.sub(pattern, replacement, content)
    
    # Write back the converted content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Convert all template files
template_dir = '/home/ubuntu/infortex/main/templates'
html_files = [f for f in os.listdir(template_dir) if f.endswith('.html') and f != 'base.html']

for html_file in html_files:
    filepath = os.path.join(template_dir, html_file)
    print(f"Converting {html_file}...")
    convert_html_to_django_template(filepath)
    
print(f"Converted {len(html_files)} template files!")