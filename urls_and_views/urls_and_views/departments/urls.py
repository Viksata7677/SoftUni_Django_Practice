from django.urls import path

from urls_and_views.departments.views import index

urlpatterns = [
    path('', index)
]