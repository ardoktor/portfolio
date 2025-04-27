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