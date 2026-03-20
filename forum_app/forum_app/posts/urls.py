from django.urls import path

from forum_app.posts.views import index, dashboard

urlpatterns = [
    path('', index, name='homepage'),
    path('dashboard/', dashboard, name='dashboard')
]