from django.urls import path

from exam_preparation.common.views import Homepage

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
]