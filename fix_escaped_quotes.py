#!/usr/bin/env python3

def fix_escaped_quotes():
    template_path = '/home/ubuntu/infortex/main/templates/index.html'
    
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix escaped quotes in static tags
    content = content.replace("\\'", "'")
    
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Fixed escaped quotes in index.html template")

if __name__ == '__main__':
    fix_escaped_quotes()