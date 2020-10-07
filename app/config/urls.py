from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	re_path(r'^(api/)?$', RedirectView.as_view(url='/'+settings.API_ROOT_URL)),
	path(settings.API_ROOT_URL, include('api.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
