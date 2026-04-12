from django.urls import path, include

from exam_preparation.album.views import AlbumAddPage, AlbumEditPage

urlpatterns = [
    path('add/', AlbumAddPage.as_view(), name='album_add'),
    path('<int:id>/', include([
        path('edit/', AlbumEditPage.as_view(), name='album_edit')
    ]))

]