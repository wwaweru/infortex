#!/usr/bin/env python3

import os
import re
from pathlib import Path

def update_index_template():
    """
    Update the index.html Django template with content from the updated root index.html
    while preserving Django template structure
    """
    
    project_root = Path('/home/ubuntu/infortex')
    root_index = project_root / 'index.html'
    template_index = project_root / 'main' / 'templates' / 'index.html'
    
    # Read the updated HTML content
    with open(root_index, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Extract the navigation menu
    nav_match = re.search(r'<ul id="mainmenu">(.*?)</ul>', html_content, re.DOTALL | re.MULTILINE)
    if nav_match:
        nav_content = nav_match.group(1).strip()
        # Convert static links to Django URL tags
        nav_content = re.sub(r'href="index\.html"', 'href="{% url \'home\' %}"', nav_content)
        nav_content = re.sub(r'href="services\.html"', 'href="{% url \'services\' %}"', nav_content)
        nav_content = re.sub(r'href="about\.html"', 'href="{% url \'about\' %}"', nav_content)
        nav_content = re.sub(r'href="contact\.html"', 'href="{% url \'contact\' %}"', nav_content)
        nav_content = re.sub(r'href="booking\.html"', 'href="{% url \'booking\' %}"', nav_content)
    else:
        nav_content = ""
    
    # Extract the main content section
    content_match = re.search(r'<div class="no-bottom no-top" id="content">(.*)', html_content, re.DOTALL)
    if content_match:
        main_content = content_match.group(1)
        # Remove the closing wrapper divs and script tags from the end
        main_content = re.sub(r'</div>\s*<!-- wrapper end -->\s*<!-- Javascript Files[^<]*$', '', main_content, flags=re.DOTALL)
        main_content = re.sub(r'</div>\s*<script[^<]*$', '', main_content, flags=re.DOTALL)
        main_content = main_content.strip()
        
        # Convert static file references
        main_content = re.sub(r'src="images/', 'src="{% static \'images/', main_content)
        main_content = re.sub(r'href="css/', 'href="{% static \'css/', main_content)
        main_content = re.sub(r'href="images/', 'href="{% static \'images/', main_content)
        main_content = re.sub(r'data-bgimage="url\(images/', 'data-bgimage="url({% static \'images/', main_content)
        main_content = re.sub(r'url\(images/', 'url({% static \'images/', main_content)
        
        # Close the static tags properly - be very careful with regex to avoid nested tags
        main_content = re.sub(r'{% static \'([^\']+)\'/([^}])', r'{% static \'\1\' %}/\2', main_content)
        main_content = re.sub(r'{% static \'([^\']+)\'(["\)])', r'{% static \'\1\' %}\2', main_content)
        
    else:
        main_content = ""
    
    # Create the Django template content
    django_template = '''{% extends 'base.html' %}
{% load static %}

{% block title %}Infortex Solution Limited | Customs Clearing & Freight Forwarding Kenya{% endblock %}

{% block header_content %}
<!-- mainemenu begin -->
<ul id="mainmenu">
''' + nav_content + '''
</ul>
<!-- mainmenu end -->
{% endblock %}

{% block content %}
<div class="no-bottom no-top" id="content">
''' + main_content + '''
</div>
{% endblock %}'''
    
    # Write the updated template
    with open(template_index, 'w', encoding='utf-8') as f:
        f.write(django_template)
    
    print("Successfully updated index.html template")

def main():
    update_index_template()

if __name__ == '__main__':
    main()