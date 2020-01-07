from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'writer', 'genre']
    list_display_links = ['id', 'title']