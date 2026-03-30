from django.urls import path, include

from forum_app.posts.views import dashboard, add_post, edit_post, delete_post, IndexView, MyRedirectHomeView

urlpatterns = [
    path('', IndexView.as_view(), name='homepage'),
    path('dashboard/', dashboard, name='dashboard'),
    path('add-post/', add_post, name='add-post'),
    path('<int:pk>/', include([
        path('edit-post/', edit_post, name='edit-post'),
        path('delete-post/', delete_post, name='delete-post')
    ])),
    path('redirect-home/', MyRedirectHomeView.as_view(), name='redirect-home')
]