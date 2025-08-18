from django.contrib import admin
from blog.models import Post


@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'views_count', 'is_published')
    search_fields = ('title',)
    list_filter = ('is_published', 'created_at')
    ordering = ('-created_at',)
