from django.urls import path, include

from urls_and_views.departments import views

urlpatterns = [
    path('', views.index, name='home'),
    path('softuni/', views.redirect_to_softuni),
    path('redirect-to-view/', views.redirect_to_view),
    path('numbers/', include([
        path('<int:pk>/', views.view_with_int_pk, name='numbers'),
        path('<slug:slug>/', views.view_with_slug),
    ])),
    path('<variable>/', views.view_with_name),
    path('<path:variable>/', views.view_with_name),
]