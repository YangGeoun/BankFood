from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.detail),
    path('<int:article_pk>/comments/', views.comments),
    path('<int:article_pk>/comments/<int:comment_pk>/', views.comment_detail),
]
