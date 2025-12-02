from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def team(request):
    return render(request, 'team.html')

def careers(request):
    return render(request, 'careers.html')

def certifications(request):
    return render(request, 'certifications.html')

def booking(request):
    return render(request, 'booking.html')

def gallery(request):
    return render(request, 'gallery.html')

def faq(request):
    return render(request, 'faq.html')

def track(request):
    return render(request, 'track.html')

def testimonials(request):
    return render(request, 'testimonials.html')
