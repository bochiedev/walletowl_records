from rest_framework import serializers
from .models import *

from django.contrib.contenttypes.models import ContentType
from .models import *
from django.contrib.auth import get_user_model

class InvoiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'
