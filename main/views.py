from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import BlogPost, Project, Tag, ContactMessage
from django.views.generic import ListView, DetailView

# Create your views here.
def home(request):
    featured_projects = Project.objects.all()[:3]
    return render(request, 'main/home.html', {'featured_projects': featured_projects})

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        if email and message:
            ContactMessage.objects.create(email=email, message=message[:280])
            messages.success(request, 'Message sent! I\'ll get back to you soon.')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill in both fields.')

    return render(request, 'main/contacts.html')


def projects(request):
    projects_list = Project.objects.all()
    return render(request, 'main/projects.html', {'projects': projects_list})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'main/project_detail.html', {'project': project})


class BlogListView(ListView):
    model = BlogPost
    template_name = 'main/blog.html'
    context_object_name = 'blog_posts'

    def get_queryset(self):
        # Only show published posts on public site
        return BlogPost.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'main/blog_detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        # Only show published posts on public site
        return BlogPost.objects.filter(is_published=True)

