from django.urls import path
from . import views

urlpatterns = [
    path('getdeposit/', views.getdeposit),
    path('deposit/', views.deposit),
    path('do/', views.getdeopsitoption),
    path('getsaving/', views.getsaving),
    path('saving/', views.saving),
    path('so/', views.getsavingoption),
    path('card/', views.getcard),
    path('fund/', views.getfund),
    path('test/', views.test),
]
