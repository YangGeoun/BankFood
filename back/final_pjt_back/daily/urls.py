from django.urls import path
from . import views

urlpatterns = [
    path('youtube/', views.youtube),
    path('getyoutube/', views.getYoutube),
    path('news/', views.news),
    path('getnews/', views.getnews),
    path('getexchange/', views.getexchange),
]
