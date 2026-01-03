from django.db import models

class Article(models.Model):
    CATEGORY_CHOICES = [
    ("general", "General"),
    ("technology", "Technology"),
    ("politics", "Politics"),
    ("sports", "Sports"),
    ("business", "Business"),
    ("entertainment", "Entertainment"),
]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    article_url = models.URLField(unique=True)
    image_url = models.URLField(blank=True, null=True)
    published_at = models.DateTimeField()
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="general"   # IMPORTANT
    )

    def __str__(self):
        return self.title
