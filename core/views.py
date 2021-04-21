from django.shortcuts import render, get_object_or_404
from .serializers import EmployeeSerializers
from rest_framework import generics
from .models import Employee 
from rest_framework.views import APIView
from rest_framework import viewsets

# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    http_methods = ["get", "update", "delete"]

# class EmployeeDetail(APIView):
#     def get_object(self, id):
#         try:
#             return Employee.objects.get(id = id)
#         except:
#             pass
    
#     def delete(self, request, id, format=None):
#         employee = self.get_object(id)
#         employee.delete()

