from rest_framework import serializers
from .models import User

# class UserSerializer(serializers.ModelSerializer):
#     login = serializers.CharField(max_length=150, default="Ваш уникальный логин")
#     first_name = serializers.CharField(max_length=30)
#     last_name = serializers.CharField(max_length=30)
#     email = serializers.EmailField()
#     password = serializers.CharField(max_length=128)  # Рекомендуется использовать Django встроенные функции для хеширования паролей
#     class Meta:
#         model = User
#         fields = '__all__'
#     def create(self, validated_data):
#         return User.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.login = validated_data.get('login', instance.login )
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.email = validated_data.get('email', instance.email)
#         instance.password = validated_data.get('password', instance.password)
#         instance.save()
#         return instance
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('login', 'first_name', 'last_name', 'email', 'password')


