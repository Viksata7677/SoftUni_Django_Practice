from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from exam_preparation.album.forms import AlbumCreateForm, AlbumDeleteForm, AlbumEditForm
from exam_preparation.album.models import Album
from exam_preparation.utils import get_user_obj


# Create your views here.


class AlbumAddPage(CreateView):
    form_class = AlbumCreateForm
    success_url = reverse_lazy('homepage')
    template_name = 'album/album-add.html'

    def form_valid(self, form):
        profile = get_user_obj()
        form.instance.owner = profile
        return super().form_valid(form)


class AlbumDeletePage(DeleteView):
    form_class = AlbumDeleteForm
    success_url = reverse_lazy('homepage')



class AlbumEditPage(UpdateView):
    model = Album
    form_class = AlbumEditForm
    pk_url_kwarg = 'id'
    template_name = 'album/album-edit.html'
    success_url = reverse_lazy('homepage')
