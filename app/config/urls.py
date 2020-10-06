from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', RedirectView.as_view(url='/'+settings.API_ROOT_URL)),
	path('api/', RedirectView.as_view(url='/'+settings.API_ROOT_URL)),
	# TODO: Improve root redirection method
	path(settings.API_ROOT_URL, include('api.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
