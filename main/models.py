import html
import re

from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.text import slugify, Truncator
from django.utils import timezone


def _plain_text(markdown):
    """Strip markdown and HTML down to readable prose."""
    text = re.sub(r'<[^>]+>', ' ', markdown)                  # raw HTML
    text = html.unescape(text)                                # &middot; etc.
    text = re.sub(r'!\[([^\]]*)\]\([^)]*\)', r'\1', text)      # images
    text = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', text)       # links
    text = re.sub(r'^\s{0,3}#{1,6}\s*', '', text, flags=re.M)  # headings
    text = re.sub(r'^\s{0,3}>\s?', '', text, flags=re.M)       # quotes
    text = re.sub(r'^\s{0,3}[-*+]\s+', '', text, flags=re.M)   # bullets
    text = re.sub(r'[*_`]', '', text)                         # emphasis
    return ' '.join(text.split())


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class BlogPost(models.Model):
    title = models.CharField(max_length=200, blank=True, help_text="Optional title (auto-generated from text if empty)")
    text = models.TextField(help_text="Your note content")
    slug = models.SlugField(unique=True, blank=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True, blank=True, related_name='blog_posts')
    is_published = models.BooleanField(default=True, help_text="Uncheck to save as draft")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Auto-generate title from text if not provided
        if not self.title:
            self.title = self.text[:100].split('\n')[0][:100]

        # Generate a slug if one doesn't exist
        if not self.slug:
            self.slug = slugify(self.title[:50]) or slugify(self.text[:50])

            # Ensure the slug is unique
            original_slug = self.slug
            counter = 1
            while BlogPost.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.slug])

    @property
    def summary(self):
        """The note's opening as plain text, for meta descriptions.

        Share cards and search results want prose, so markdown and any raw
        HTML (a video embed, say) are stripped rather than rendered.
        Paragraphs are taken in order until there is enough to read: stopping
        at the first one would cut a short opening line off from the sentence
        that completes it, and taking the whole note drags in captions and
        list fragments that read as noise once the markup is gone.
        """
        lede = []
        for block in (self.text or '').split('\n\n'):
            cleaned = _plain_text(block)
            if len(cleaned) < 15:          # a heading, a caption, stray markup
                continue
            lede.append(cleaned)
            if sum(len(part) for part in lede) >= 80:
                break
        return Truncator(' '.join(lede)).chars(200)

    def __str__(self):
        return self.title or self.text[:50]

    class Meta:
        ordering = ['-created_at']

class ContactMessage(models.Model):
    email = models.EmailField()
    message = models.TextField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.email} - {self.message[:30]}..."

    class Meta:
        ordering = ['-created_at']


class Project(models.Model):
    STATUS_CHOICES = [
        ("active", "Active — currently building"),
        ("work", "Day job / internal"),
        ("archived", "Archived — stopped"),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="archived")
    description = models.TextField()
    short_description = models.CharField(max_length=280, blank=True,
                                         help_text="2-3 sentences for the projects index; "
                                                   "the detail page keeps the long description.")
    year = models.CharField(max_length=20)
    metrics = models.CharField(max_length=200, blank=True,
                               help_text="Comma-separated proof points. e.g. "
                                         "'12 dentists in cohort, live on App Store, payments active'")
    postmortem = models.CharField(max_length=200, blank=True,
                                  help_text="One sentence: why this stopped. Shown on archived projects.")
    app_store_link = models.URLField(blank=True)
    image_url = models.URLField(blank=True, null=True, help_text="URL to project image")
    tech_stack = models.CharField(max_length=255, help_text="Comma-separated list of technologies")
    demo_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    other_link = models.URLField(blank=True, null=True)
    other_link_text = models.CharField(max_length=50, blank=True, null=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # The homepage design assumes a single lead project
        if self.status == "active":
            clash = Project.objects.filter(status="active").exclude(pk=self.pk)
            if clash.exists():
                raise ValidationError(
                    {"status": f'Only one project can be active at a time — "{clash.first()}" already is.'}
                )

    def save(self, *args, **kwargs):
        self.clean()
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

    def get_metrics_list(self):
        return [m.strip() for m in self.metrics.split(',') if m.strip()]

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order', '-year', '-created_at']