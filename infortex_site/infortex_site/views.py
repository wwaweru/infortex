from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.conf import settings


@require_GET
def robots_txt(request):
    """Generate robots.txt file"""
    lines = [
        "User-agent: *",
        "Allow: /",
        "",
        "# Disallow admin areas",
        "Disallow: /admin/",
        "Disallow: /django-admin/", 
        "Disallow: /accounts/",
        "",
        "# Sitemap",
        f"Sitemap: {request.build_absolute_uri('/sitemap.xml')}",
        "",
        "# Crawl delay",
        "Crawl-delay: 1",
    ]
    
    return HttpResponse("\n".join(lines), content_type="text/plain")


@require_GET
def security_txt(request):
    """Generate security.txt file for security researchers"""
    lines = [
        "Contact: mailto:security@infortexsolutionsltd.co.ke",
        "Expires: 2025-12-31T23:59:59.000Z",
        "Preferred-Languages: en",
        "Policy: https://infortexsolutionsltd.co.ke/security-policy/",
    ]
    
    return HttpResponse("\n".join(lines), content_type="text/plain")