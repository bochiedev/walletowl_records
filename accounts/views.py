# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.mixins import *
from rest_framework.generics import *
from .models import *
from django.shortcuts import get_object_or_404
from .serializers import *
from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class UserCreateAPIView(generics.ListCreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()

    def post(self, request, format=None):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer._errors,status=status.HTTP_400_BAD_REQUEST)
