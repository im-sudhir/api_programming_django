from django.shortcuts import render
from .models import *
from .serializers import EmployeeSerializer,UserSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET','POST'])
def employeeListView(request):
    if request.method=='GET':
        employees=Employee.objects.all()
        serializer=EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer= EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['DELETE', 'GET', 'PUT'])     
def employeeDetailView(request,pk):

    try:
        employee=Employee.objects.get(id=pk)

    except:
        return Response(status=404)
    
    if request.method=="GET":
        serializer=EmployeeSerializer(employee)
        return Response(serializer.data)
        
    elif request.method=="DELETE":
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method=="PUT":
        serializer= EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET', 'POST'])
def userListView(request):
    if request.method=='GET':
        users= User.objects.all()
        serializer= UserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

