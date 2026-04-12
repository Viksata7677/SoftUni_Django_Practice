from django.shortcuts import render
from django.views.generic import DetailView

from exam_preparation.profiles.models import Profile
from exam_preparation.utils import get_user_obj


# Create your views here.

class ProfileDetailsPage(DetailView):
    template_name = 'profile/profile-details.html'

    def get_object(self, queryset = None):
        return get_user_obj()