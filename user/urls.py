from django.urls import path
from . import views

urlpatterns = [
    path('', views.SignView.as_view(), name="sign-view"),
]
