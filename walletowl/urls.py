from django.conf.urls import url, include
from django.contrib.auth.models import User
from django.contrib import admin
from rest_framework import routers, serializers, viewsets

from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views


# Routers provide an easy way of automatically determining the URL conf.


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

urlpatterns = [
    url(r'^login/', views.obtain_auth_token),
    url(r'^account/', include('accounts.urls', namespace='account')),
    url(r'^docs/', include('documents.urls', namespace='docs')),


]
