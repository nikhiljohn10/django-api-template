from django.urls import path, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'manufacturers', views.ManufacturerViewSet)
router.register(r'cars', views.CarViewSet)
router.register(r'ownerships', views.OwnershipViewSet)
router.register(r'owners', views.OwnerViewSet)

urlpatterns = [
	path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]
