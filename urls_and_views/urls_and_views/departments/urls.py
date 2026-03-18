from django.urls import path

from urls_and_views.departments import views

urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.view_with_int_pk),
    path('<variable>/', views.view_with_name),
]