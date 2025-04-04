from django.contrib import admin
from django.urls import path, include
from blog import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name = 'home'),
    path("posts/", include('posts.urls')),

    path('create/', views.create, name='create'),  # 새 글 작성 페이지 URL

    path('accounts/', include('accounts.urls', namespace = 'accounts')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)