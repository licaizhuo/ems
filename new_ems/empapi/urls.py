from django.urls import path

from empapi import views

urlpatterns = [
    path("emp/", views.EmpGenericAPIView.as_view()),
    path("emp/<str:id>/", views.EmpGenericAPIView.as_view())
]
