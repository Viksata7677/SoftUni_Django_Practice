from django.urls import path

from forum_app.posts.views import index

urlpatterns = [
    path('', index, name='homepage'),
]