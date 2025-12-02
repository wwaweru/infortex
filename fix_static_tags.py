#!/usr/bin/env python3

import re

def fix_static_tags():
    template_path = '/home/ubuntu/infortex/main/templates/index.html'
    
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix broken static tag references
    fixes = [
        # Fix missing closing quotes and %} for images
        (r'{% static \'([^\']+\.(?:webp|png|jpg|svg))"', r'{% static \'\1\' %}"'),
        # Fix missing %} for other files
        (r'{% static \'([^\']+)\'"', r'{% static \'\1\' %}"'),
        # Fix data-bgimage attributes specifically
        (r'data-bgimage="url\({% static \'([^\']+)\.webp\)"', r'data-bgimage="url({% static \'\1.webp\' %})"'),
        # Fix remaining unclosed static tags
        (r'{% static \'([^\']+)\'([^}])', r'{% static \'\1\' %}\2'),
    ]
    
    for pattern, replacement in fixes:
        content = re.sub(pattern, replacement, content)
    
    # Write back the fixed content
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Fixed broken static tags in index.html")

if __name__ == '__main__':
    fix_static_tags()