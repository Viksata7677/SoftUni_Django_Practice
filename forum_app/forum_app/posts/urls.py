from django.urls import path

from forum_app.posts.views import index, dashboard, add_post, edit_post

urlpatterns = [
    path('', index, name='homepage'),
    path('dashboard/', dashboard, name='dashboard'),
    path('add-post/', add_post, name='add-post'),
    path('<int:pk>/edit-post/', edit_post, name='edit-post')
]