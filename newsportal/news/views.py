from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q
from .models import Article
from .fetch_news import fetch_news


def news_api(request):
    category = request.GET.get("category")
    search = request.GET.get("search")

    articles = Article.objects.all().order_by("-published_at")

    if category and category != "all":
        articles = articles.filter(category=category)

    if search:
        articles = articles.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search)
        )

    data = []
    for article in articles:
        data.append({
            "title": article.title,
            "description": article.description,
            "image": article.image_url,
            "url": article.article_url,
            "category": article.category,
            "published_at": article.published_at,
        })

    return JsonResponse(data, safe=False)


def refresh_news(request):
    fetch_news()
    return JsonResponse({"status": "News refreshed successfully"})


def home(request):
    return render(request, "news/index.html")
