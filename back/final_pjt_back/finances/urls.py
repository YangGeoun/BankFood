from django.urls import path
from . import views

urlpatterns = [
    path('', views.getdeposit),
    path('do/', views.getdeopsitoption),
    path('sa/', views.getsaving),
    path('so/', views.getsavingoption),
]
