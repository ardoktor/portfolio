from django.contrib import admin
from django import forms
from .models import BlogPost, Project, Tag


# Custom admin site configuration
admin.site.site_header = "Arda's Notes"
admin.site.site_title = "Notes"
admin.site.index_title = "Dashboard"


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'post_count')
    search_fields = ('name',)

    def post_count(self, obj):
        return obj.blog_posts.count()
    post_count.short_description = 'Posts'


class BlogPostForm(forms.ModelForm):
    """Ergonomic form for mobile posting"""

    # Large text area - main focus
    text = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 15,
            'style': 'width:100%; font-size:16px; padding:15px; line-height:1.7; border-radius:8px; border:2px solid #ccc;',
            'placeholder': 'Paste or write your note here...',
            'autofocus': 'autofocus',
        }),
        label='Note Content'
    )

    # Simple title input
    title = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'style': 'width:100%; font-size:16px; padding:12px; border-radius:8px; border:2px solid #ccc;',
            'placeholder': 'Title (optional - auto-generated if empty)',
        }),
        label='Title'
    )

    # Tag as radio buttons for easy mobile selection
    tag = forms.ModelChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=forms.RadioSelect(attrs={
            'style': 'margin-right:10px;',
        }),
        label='Tag',
        empty_label='No tag'
    )

    class Meta:
        model = BlogPost
        fields = ['text', 'title', 'tag', 'is_published']


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostForm
    list_display = ('title_short', 'tag', 'status_badge', 'created_at')
    list_filter = ('is_published', 'tag')
    search_fields = ('title', 'text')
    list_editable = ('is_published',)
    ordering = ('-created_at',)
    list_per_page = 20

    # Simple layout - text first, then options
    fieldsets = (
        ('Write Your Note', {
            'fields': ('text',),
            'classes': ('wide',),
        }),
        ('Options', {
            'fields': ('title', 'tag', 'is_published'),
            'classes': ('wide',),
        }),
    )

    exclude = ('slug',)

    actions = ['publish_selected', 'draft_selected']

    def title_short(self, obj):
        title = obj.title or obj.text[:40]
        return title[:35] + '...' if len(title) > 35 else title
    title_short.short_description = 'Note'

    def status_badge(self, obj):
        if obj.is_published:
            return '✓ Live'
        return '○ Draft'
    status_badge.short_description = 'Status'

    def publish_selected(self, request, queryset):
        count = queryset.update(is_published=True)
        self.message_user(request, f'{count} note(s) published!')
    publish_selected.short_description = '✓ Publish selected'

    def draft_selected(self, request, queryset):
        count = queryset.update(is_published=False)
        self.message_user(request, f'{count} note(s) moved to draft.')
    draft_selected.short_description = '○ Move to draft'

    class Media:
        css = {
            'all': ('main/css/admin_mobile.css',)
        }


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'is_featured', 'order')
    list_editable = ('is_featured', 'order')
    search_fields = ('title', 'description')
    list_filter = ('is_featured', 'year')
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'year', 'tech_stack')
        }),
        ('Links', {
            'fields': ('demo_link', 'github_link', 'other_link', 'other_link_text'),
            'classes': ('collapse',)
        }),
        ('Display', {
            'fields': ('image_url', 'is_featured', 'order'),
            'classes': ('collapse',)
        }),
    )


admin.site.register(Tag, TagAdmin)
