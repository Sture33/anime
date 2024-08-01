from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from anime_app.views import *

urlpatterns = [
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)