from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/home.html')  # For now, just rendering base.html

def about(request):
    return render(request, 'main/about.html')
