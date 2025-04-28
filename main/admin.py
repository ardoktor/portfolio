from django.contrib import admin
from .models import BlogPost, Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'created_at')
    search_fields = ('title', 'description', 'tech_stack')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(BlogPost)
admin.site.register(Project, ProjectAdmin)
# Register your models here.
