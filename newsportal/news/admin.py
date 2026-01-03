from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "published_at")
    list_filter = ("category",)
    search_fields = ("title", "description")
    ordering = ("-published_at",)
