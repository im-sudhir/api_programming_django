from django.urls import path
from .views import *

urlpatterns = [
    path('employees',employeeListView),
    path('users', userListView),
]
