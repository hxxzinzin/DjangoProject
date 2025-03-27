from django.contrib import admin
from django.urls import path, include
from cafeMain import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name = "home"),
    path("FromL/", include("FromLove.urls")),
    path("TOL/", include("ToLove.urls")),

    path("create/", views.create, name = "create"),
]
