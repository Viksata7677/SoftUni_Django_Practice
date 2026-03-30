from django.urls import path, include

from forum_app.posts.views import edit_post, delete_post, IndexView, MyRedirectHomeView, \
    DashboardView, AddPostView

urlpatterns = [
    path('', IndexView.as_view(), name='homepage'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('<int:pk>/', include([
        path('edit-post/', edit_post, name='edit-post'),
        path('delete-post/', delete_post, name='delete-post')
    ])),
    path('redirect-home/', MyRedirectHomeView.as_view(), name='redirect-home')
]