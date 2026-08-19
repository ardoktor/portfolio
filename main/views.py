from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Project
from django.views.generic import ListView, DetailView

# Create your views here.
def home(request):
    return render(request, 'main/home.html', {
        'current_project': Project.objects.filter(status='active').first(),
        'work_projects': Project.objects.filter(status='work'),
        'archived_projects': Project.objects.filter(status='archived'),
        'recent_posts': BlogPost.objects.filter(is_published=True)[:3],
    })

def about(request):
    return render(request, 'main/about.html')


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
