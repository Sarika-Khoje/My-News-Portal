from django.urls import path
from .views import home, news_api, refresh_news

urlpatterns = [
    path("", home, name="home"),
    path("api/news/", news_api, name="news_api"),
    path("api/refresh/", refresh_news, name="refresh_news"),
]


