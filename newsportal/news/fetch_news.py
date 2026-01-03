import requests
from .models import Article
from django.utils.dateparse import parse_datetime

API_KEY = "37c57f995f1f4cc78a868ce2657d086b"

CATEGORIES = ["politics", "sports", "technology", "business", "entertainment"]

def fetch_news():
    for category in CATEGORIES:
        url = (
            f"https://newsapi.org/v2/everything?"
            f"q={category}&language=en&sortBy=publishedAt&apiKey={API_KEY}"
        )

        response = requests.get(url)
        data = response.json()
        articles = data.get("articles", [])

        for item in articles:
            if not item.get("title") or not item.get("url"):
                continue

            Article.objects.get_or_create(
                article_url=item["url"],
                defaults={
                    "title": item["title"],
                    "description": item.get("description", ""),
                    "image_url": item.get("urlToImage", ""),
                    "category": category,
                    "published_at": parse_datetime(item["publishedAt"]),
                }
            )

    print("News fetched and categorized successfully")
