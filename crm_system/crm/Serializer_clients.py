from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    surname = serializers.CharField(max_length=255, default='неизвестно')
    birth_date = serializers.DateField(allow_null=True)
    email = serializers.EmailField( allow_null=True, default="example@example.com")  # Добавлено default
    phone = serializers.CharField(max_length=15, allow_null=True)
    address = serializers.CharField(allow_null=True)
    class Meta:
        model = Client
        fields = '__all__'
