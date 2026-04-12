from django.urls import path

from exam_preparation.profiles.views import ProfileDetailsPage

urlpatterns = [
    path('details/', ProfileDetailsPage.as_view(), name='profile_details')
]