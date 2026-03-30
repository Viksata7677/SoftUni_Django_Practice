from django.urls import path, include

from forum_app.posts.views import IndexView, MyRedirectHomeView, \
    DashboardView, AddPostView, EditPostView, DeletePostView, PostDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='homepage'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('<int:pk>/', include([
        path('edit-post/', EditPostView.as_view(), name='edit-post'),
        path('details-post/', PostDetailView.as_view(), name='details-post'),
        path('delete-post/', DeletePostView.as_view(), name='delete-post')
    ])),
    path('redirect-home/', MyRedirectHomeView.as_view(), name='redirect-home')
]