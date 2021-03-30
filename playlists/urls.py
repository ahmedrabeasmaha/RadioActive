from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adnum/', views.adnum, name='adnum'),
    path('play/', views.play, name='play'),
    path('end/', views.end, name='end'),
    path('ad/', views.ad, name='ad'),
]