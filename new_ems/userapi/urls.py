from django.urls import path

from userapi import views

urlpatterns = [
    path("rt/", views.UserAPIView.as_view({'post': 'register', 'get': "login"}))
]
