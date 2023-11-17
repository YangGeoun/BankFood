from django.urls import path
from . import views

urlpatterns = [
    path('youtube/', views.youtube),
    path('getyoutube/', views.getYoutube),
]
