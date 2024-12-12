from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User

class EmployeeSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=30)
    email=serializers.EmailField()
    password=serializers.CharField(max_length=30)
    phone=serializers.CharField(max_length=10)

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

class UserSerializer(serializers.Serializer):
    username= serializers.CharField(max_length=30)
    first_name=serializers.CharField(max_length=30)
    last_name=serializers.CharField(max_length=30)
    email=serializers.EmailField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)