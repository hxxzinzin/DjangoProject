from django.contrib import admin
from django.urls import path
from ToLove import views

urlpatterns = [
    path("", views.toL, name = "toL"),
]