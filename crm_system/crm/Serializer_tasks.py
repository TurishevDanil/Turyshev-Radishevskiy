from rest_framework import serializers
from .models import Task    

class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(default="", max_length=200)
    description = serializers.CharField(default="")
    deadline = serializers.DateField()
    is_completed = serializers.BooleanField()
    class Meta:
        model = Task
        fields = '__all__'


