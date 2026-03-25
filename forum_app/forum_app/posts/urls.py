from django.urls import path, include

from forum_app.posts.views import index, dashboard, add_post, edit_post, delete_post

urlpatterns = [
    path('', index, name='homepage'),
    path('dashboard/', dashboard, name='dashboard'),
    path('add-post/', add_post, name='add-post'),
    path('<int:pk>/', include([
        path('edit-post/', edit_post, name='edit-post'),
        path('delete-post/', delete_post, name='delete-post')
    ]))
]