from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pybo.urls')),
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
]
