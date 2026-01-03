from django.apps import AppConfig


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'

    def ready(self):
        from .fetch_news import fetch_news
        try:
            fetch_news()
        except:
            pass
