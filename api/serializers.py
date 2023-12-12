from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User
from datetime import datetime


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = '__all__'
