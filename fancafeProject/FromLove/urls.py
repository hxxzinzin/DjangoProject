from django.contrib import admin
from django.urls import path
from FromLove import views

urlpatterns = [
    path("", views.fromL, name = "fromL"),
]
