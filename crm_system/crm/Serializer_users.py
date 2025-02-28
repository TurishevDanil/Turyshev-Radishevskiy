from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = User
        fields = ['id','login', 'first_name', 'last_name', 'email', 'password', 'owner']


