
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload, name = "upload"), 
    path('', views.upload, name = "upload"), 
    path('update_img/', views.update_img, name = "update_img"), 
    path('post_img/', views.post_img, name = "post_img"), 

]
