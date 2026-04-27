from django.db import models

from forum_app.posts.choices import LanguageChoice


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    languages = models.CharField(max_length=20, choices=LanguageChoice.choices, default=LanguageChoice.OTHER)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    approved = models.BooleanField(default=False)

    class Meta:
        permissions = [
            ('can_approve_posts', 'Can approve posts'),
        ]


class Comment(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)