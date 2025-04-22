from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/home.html')  # For now, just rendering base.html

def about(request):
    return render(request, 'main/about.html')

def blog(request):
    return render(request, 'main/blog.html')

def contact(request):
    return render(request, 'main/contacts.html')


def projects(request):
    return render(request, 'main/projects.html')