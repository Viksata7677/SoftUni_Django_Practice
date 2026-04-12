from django.urls import path

from exam_preparation.profiles.views import ProfileDetailsPage, ProfileDeletePage

urlpatterns = [
    path('details/', ProfileDetailsPage.as_view(), name='profile_details'),
    path('delete/', ProfileDeletePage.as_view(), name='profile_delete')
]