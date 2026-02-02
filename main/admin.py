from django.contrib import admin
from .models import BlogPost, Project, Tag

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'tag', 'created_at')
    list_filter = ('tag',)
    search_fields = ('text',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'created_at')
    search_fields = ('title', 'description', 'tech_stack')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Tag, TagAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Project, ProjectAdmin)
