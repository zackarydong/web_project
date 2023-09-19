from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='spotify-home'),
    path('about/', views.about, name='spotify-about')
]