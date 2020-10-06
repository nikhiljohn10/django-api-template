from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers
from api.views import UserViewSet, MySampleView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
	path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path('sam/', MySampleView.as_view()),

]