from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.
class BlogPost(models.Model):
    text = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        # Generate a slug if one doesn't exist
        if not self.slug:
            self.slug = slugify(self.text[:50])
            
            # Ensure the slug is unique
            original_slug = self.slug
            counter = 1
            while BlogPost.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
                
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.slug])
    
    def __str__(self):
        return self.text[:50]

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    year = models.CharField(max_length=20)
    image_url = models.URLField(blank=True, null=True, help_text="URL to project image")
    tech_stack = models.CharField(max_length=255, help_text="Comma-separated list of technologies")
    demo_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    other_link = models.URLField(blank=True, null=True)
    other_link_text = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            
            # Ensure the slug is unique
            original_slug = self.slug
            counter = 1
            while Project.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
                
        super().save(*args, **kwargs)
    
    def get_tech_stack_list(self):
        return [tech.strip() for tech in self.tech_stack.split(',')]
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-year', '-created_at']