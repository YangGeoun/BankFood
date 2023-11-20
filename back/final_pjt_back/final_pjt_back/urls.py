from django.contrib import admin
from django.urls import path, include
# .model

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('daily/', include('daily.urls')),
    path('finances/', include('finances.urls')),
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/signup/', include('accounts.urls')),
]
