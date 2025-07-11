# services/serializers.py
from rest_framework import serializers
from .models import Service

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'slug', 'description', 'icon', 'created_at']
        read_only_fields = ['slug', 'created_at']
