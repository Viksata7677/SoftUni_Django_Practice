from django.urls import path, include

from exam_preparation.album.views import AlbumAddPage, AlbumEditPage, AlbumDetailPage, AlbumDeletePage

urlpatterns = [
    path('add/', AlbumAddPage.as_view(), name='album_add'),
    path('<int:id>/', include([
        path('edit/', AlbumEditPage.as_view(), name='album_edit'),
        path('details/', AlbumDetailPage.as_view(), name='album_details'),
        path('delete/', AlbumDeletePage.as_view(), name='album_delete'),
    ]))
]