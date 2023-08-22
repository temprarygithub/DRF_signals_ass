from django.shortcuts import render
from rest_framework import generics, permissions
from .models import User_Data
from .serializers import UserSerializer
from .permissions import AdminAuthenticationPermission

class user_lst(generics.ListCreateAPIView):
    data = User_Data.objects.all()
    serializer_data = UserSerializer
    permission_request = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class user_dtl(generics.RetrieveUpdateDestroyAPIView): 
    data = User_Data.objects.all()
    serializer_data = UserSerializer
    permission_request = [AdminAuthenticationPermission]
