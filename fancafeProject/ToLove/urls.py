from django.contrib import admin
from django.urls import path
from ToLove import views

urlpatterns = [
    path("", views.toL, name = "toL"),
    path("toL_list/", views.toL_list, name = "toL_list"),
    path("toL_detail/<int:letter_id>/", views.toL_detail, name = "toL_detail"),
    path("toL_update/<int:id>/", views.toL_update, name = "toL_update"),
    path("toL_delete/<int:id>/", views.toL_delete, name = "toL_delete"),

    path('create_comment/<int:id>/', views.create_comment, name = 'create_comment'),
    path('update_comment/<int:letter_id>/<int:com_id>/', views.update_comment, name = 'update_comment'),
    path('delete_comment/<int:letter_id>/<int:com_id>/', views.delete_comment, name = 'delete_comment'),
]