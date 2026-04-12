from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView

from exam_preparation.profiles.models import Profile
from exam_preparation.utils import get_user_obj


# Create your views here.

class ProfileDetailsPage(DetailView):
    template_name = 'profile/profile-details.html'

    def get_object(self, queryset = None):
        return get_user_obj()


class ProfileDeletePage(DeleteView):
    template_name = 'profile/profile-delete.html'
    success_url = reverse_lazy('homepage')

    def get_object(self, queryset = None):
        return get_user_obj()