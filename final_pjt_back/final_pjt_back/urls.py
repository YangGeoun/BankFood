from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('daily/', include('daily.urls')),
    path('finances/', include('finances.urls')),
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/signup/', views.signup),
    path('accounts/userinfo/', views.userinfo),
    path('accounts/userinfo/<int:article_pk>/', views.article_userinfo),
    path('accounts/userproducts/', views.user_products),
    path('accounts/userarticles/', views.user_articles),
    path('test/', views.dummy),
]
