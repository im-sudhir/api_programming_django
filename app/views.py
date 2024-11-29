from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import EmployeeSerializer
# Create your views here.

def employeeListView(request):
    employees=Employee.objects.all()
    serializer=EmployeeSerializer(employees, many=True)
    return JsonResponse(serializer.data, safe=False)
