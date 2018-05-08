from django.conf.urls import url
from django.contrib import admin
from .views import *
from rest_framework import routers

# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'user_profiles', UserProfileViewSet)

urlpatterns = [
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),

]
