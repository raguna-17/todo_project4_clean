from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from config.settings.base import BASE_DIR

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls', namespace='todo')),
    path('api/', include('todo.api_urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=BASE_DIR / "static")
#config/urls.py