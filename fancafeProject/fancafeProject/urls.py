from django.contrib import admin
from django.urls import path, include
from cafeMain import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name = "home"),
    path("FromL/", include("FromLove.urls")),
    path("TOL/", include("ToLove.urls")),
  
    path("create/", views.create, name = "create"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)