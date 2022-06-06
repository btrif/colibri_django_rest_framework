from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import Employee
from .serializers import EmployeeSerializer, EmployeeIndustrySerializer
import pandas as pd

# Create your views here.

class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('id')
    serializer_class = EmployeeSerializer



class EmployeeIndustryView(viewsets.ModelViewSet):
    serializer_class = EmployeeIndustrySerializer
    queryset =  Employee.objects.values()


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/employee-list/',
        'Detail View':'/employee-detail/<str:pk>/',
        'Create':'/employee-create/',
        'Update':'/employee-update/<str:pk>/',
        'Delete':'/employee-delete/<str:pk>/',
    }

    return Response(api_urls)


class EmployeeItemMainView(APIView):
    def get(self, request):
        items = {}
        items['type'] = "Example"

        return Response(items)


@api_view(['GET'])
def employeeList(request):
    employees = Employee.objects.all().order_by('id')
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)





