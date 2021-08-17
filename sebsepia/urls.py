from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
#pour faire marcher ligne de code settings.debug
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('zblog.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
