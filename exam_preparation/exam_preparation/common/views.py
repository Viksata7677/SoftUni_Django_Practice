from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView

from exam_preparation.album.models import Album
from exam_preparation.profiles.forms import ProfileBaseForm, ProfileCreateForm
from exam_preparation.utils import get_user_obj


# Create your views here.

class Homepage(BaseFormView, ListView):
    model = Album
    form_class = ProfileCreateForm
    success_url = reverse_lazy('homepage')
    context_object_name = 'albums'

    def get_template_names(self):
        profile = get_user_obj()

        if profile:
            return ["common/home-with-profile.html"]

        return ["common/home-no-profile.html"]

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)