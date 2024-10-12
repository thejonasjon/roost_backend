from rest_framework.response import Response
from rest_framework import generics, authentication, permissions

from django.contrib.auth import get_user_model

from users.serializers import (
    CustomUserSerializer
    )

class CreateUserView(generics.ListCreateAPIView):
    """Create user view"""
    serializer_class = CustomUserSerializer

    queryset = get_user_model().objects.all()
