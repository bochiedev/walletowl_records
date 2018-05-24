from django.conf.urls import url
from django.contrib import admin
from .views import *
from rest_framework import routers

urlpatterns = [
    url(r'^invoice/$', CreateInvoiceAPIView.as_view(), name='invoice'),
    url(r'^receipt/$', CreateReceiptAPIView.as_view(), name='receipt'),
    url(r'^get_receipts/$', ListReceiptAPIView.as_view(), name='get_receipt'),



]
