from rest_framework import serializers
from .models import Deal, Client

class DealSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    date = serializers.DateField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    status = serializers.CharField(max_length=20)
    class Meta:
        model = Deal
        fields = '__all__'
    def create(self, validated_data):
        return Deal.objects.create(**validated_data)


