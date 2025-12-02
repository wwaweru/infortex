#!/usr/bin/env python3
import os
import re

def fix_all_template_issues(filepath):
    """Comprehensive fix for Django template syntax issues"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix all malformed static tag references - more comprehensive patterns
    fixes = [
        # Fix the specific issue: href="images/icon.webp\' %}" -> href="{% static 'images/icon.webp' %}"
        (r'href="images/([^"]+\.(webp|png|jpg|svg|css|js|ico|gif))\\\' %}"', r'href="{% static \'images/\1\' %}"'),
        (r'src="images/([^"]+\.(webp|png|jpg|svg|js))\\\' %}"', r'src="{% static \'images/\1\' %}"'),
        
        # Fix broken CSS/JS references
        (r'href="(css|js|fonts)/([^"]+\.(css|js|woff|eot|ttf|svg))\\\' %}"', r'href="{% static \'\1/\2\' %}"'),
        (r'src="(css|js|fonts)/([^"]+\.(css|js|woff|eot|ttf|svg))\\\' %}"', r'src="{% static \'\1/\2\' %}"'),
        
        # Fix broken data-bgimage references  
        (r'data-bgimage="url\(images/([^"]+\.(webp|png|jpg))\\\' %}\)"', r'data-bgimage="url({% static \'images/\1\' %})"'),
        
        # Clean up any remaining malformed tags
        (r'images/([^"\']+\.(webp|png|jpg|svg|css|js|ico|gif))\\\' %}"', r'{% static \'images/\1\' %}"'),
        
        # Fix unclosed background image URLs
        (r'url\(images/([^)]+\.(webp|png|jpg))\\\' %}\)', r'url({% static \'images/\1\' %})'),
        
        # Fix any remaining broken static references
        (r'(href|src)="([^"]*)\\\' %}"', r'\1="{% static \'\2\' %}"'),
    ]
    
    for pattern, replacement in fixes:
        content = re.sub(pattern, replacement, content)
    
    # Write back the fixed content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Fix all template files
template_dir = '/home/ubuntu/infortex/main/templates'
html_files = [f for f in os.listdir(template_dir) if f.endswith('.html') and f != 'base.html']

for html_file in html_files:
    filepath = os.path.join(template_dir, html_file)
    print(f"Comprehensive fix for {html_file}...")
    fix_all_template_issues(filepath)
    
print(f"Comprehensively fixed {len(html_files)} template files!")