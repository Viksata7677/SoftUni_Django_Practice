from django.urls import path

from exam_preparation.album.views import AlbumAddPage

urlpatterns = [
    path('add/', AlbumAddPage.as_view(), name='album_add'),

]