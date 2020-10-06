from rest_framework import viewsets
from django.contrib.auth.models import User
from api.serializers import UserSerializer

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MySampleView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(data={"status": True})