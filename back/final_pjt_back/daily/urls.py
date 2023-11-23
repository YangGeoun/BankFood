from django.urls import path
from . import views

urlpatterns = [
    path('youtube/', views.youtube),
    path('getyoutube/', views.getYoutube),
    path('news/', views.news),
    path('getnews/', views.getnews),
    path('getexchange/', views.getexchange),
    path('exchange/', views.exchange),
    path('getindex/', views.getindex),
    path('index/', views.index),
    
]
