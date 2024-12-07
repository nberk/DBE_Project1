from django.conf import settings # Import the project's settings
from django.db import models
from django.utils import timezone # Timezone-aware format of the datetime.now method

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )

    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True) # Automatically set the field to now when the object is first created
    updated = models.DateTimeField(auto_now=True) # Automatically set the field to now every time the object is saved
    status = models.CharField(max_length=2, choices=Status, default=Status.DRAFT)

    # Defines metadata about the model
    class Meta:
        ordering = ['-publish'] # Order the results by the publish field in descending order
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title