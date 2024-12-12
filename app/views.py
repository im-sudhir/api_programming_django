from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import EmployeeSerializer,UserSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.

@csrf_exempt
def employeeListView(request):
    if request.method=='GET':
        employees=Employee.objects.all()
        serializer=EmployeeSerializer(employees, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method=='POST':
        jsonData= JSONParser().parse(request)
        serializer= EmployeeSerializer(data=jsonData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,safe=False)
        else:
            return JsonResponse(serializer.errors,safe=False)


@csrf_exempt
def userListView(request):
    if request.method=='GET':
        users= User.objects.all()
        serializer= UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method=='POST':
        jsondata=JSONParser().parse(request)
        serializer=UserSerializer(data=jsondata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors,safe=False)
