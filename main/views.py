from django.shortcuts import render
from .models import BlogPost
from django.views.generic import ListView, DetailView

# Create your views here.
def home(request):
    return render(request, 'main/home.html')  # For now, just rendering base.html

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contacts.html')


def projects(request):
    return render(request, 'main/projects.html')

class BlogListView(ListView):
    model = BlogPost
    template_name = 'main/blog.html'
    context_object_name = 'blog_posts'

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'main/blog_detail.html'
    context_object_name = 'post'

