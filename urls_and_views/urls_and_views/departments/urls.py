from django.urls import path

from urls_and_views.departments import views

urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.view_with_int_pk),
    path('<slug:slug>/', views.view_with_slug),
    path('<variable>/', views.view_with_name),
    path('<path:variable>/', views.view_with_name)
]