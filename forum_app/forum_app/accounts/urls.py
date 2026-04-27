from django.urls import path

from forum_app.accounts.views import UserRegisterView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register')
]