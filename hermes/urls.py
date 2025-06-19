from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('authentication.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
