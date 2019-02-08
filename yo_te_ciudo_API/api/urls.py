# api/urls.py

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import Dangers_Create_View, Dangers_Update_View, Danger_Details_View
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = {

    url(r'^dangers/$', Dangers_Create_View.as_view(), name="create"),

    url(r'^update_danger/(?P<danger_id>[\w\ ]+)/(?P<new_danger_state>[\w\ ]+)/$', Dangers_Update_View.as_view(), name="update"),

    url(r'^danger_details/(?P<danger_id>[\w\ ]+)/$', Danger_Details_View.as_view(), name="danger_details"),
    
}

urlpatterns = format_suffix_patterns(urlpatterns)

# Add for media files
if settings.DEBUG:

    # La siguiente es para que Django sirva los archivos subidos por el usuario (Esto solo es para desarrollo)

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)