from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from exam_preparation.album.forms import AlbumCreateForm
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