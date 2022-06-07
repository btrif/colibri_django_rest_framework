from rest_framework import viewsets, renderers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

import colibri_django_rest_framework.settings
from .models import Employee
from .serializers import EmployeeSerializer

from django_pandas.io import read_frame
from tools.utils import get_age_from_birthday


# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('id')
    serializer_class = EmployeeSerializer


@api_view(['GET'])
def apiOverview(request):
    server_url = colibri_django_rest_framework.settings.LOCALHOST
    api_urls = {
        'Api Overview': server_url + '/',
        'CRUD operations on Employee': server_url + '/employee',
        'Average Age per Industry': server_url + '/average-age-industry/',
        'Average Salary Industry': server_url + '/average-salary-industry/',
        'Average Salary per Years of Experience': server_url + '/average-salary-experience/',
    }

    return Response(api_urls)


@api_view(['GET'])
def averageAgeIndustry(request):
    ''' View for Average age per Industry'''
    queryset = Employee.objects.all().order_by('id')
    df = read_frame(queryset, fieldnames=['industry', 'date_of_birth'])
    dobs = [get_age_from_birthday(str(i)) for i in df['date_of_birth']]
    df['age'] = dobs
    industry_age = df.groupby('industry')['age'].mean().round(2)

    return Response(industry_age.to_dict())


@api_view(['GET'])
def averageSalaryIndustry(request):
    queryset = Employee.objects.all().order_by('id')
    df = read_frame(queryset, fieldnames=['salary', 'industry'])
    industry_mean_salary = df.groupby('industry')['salary'].mean().round(2)

    return Response(industry_mean_salary.to_dict())


@api_view(['GET'])
def averageSalaryExperience(request):
    ''' View for Average age per Industry'''
    queryset = Employee.objects.all()
    df = read_frame(queryset, fieldnames=['years_of_experience', 'salary'])
    df.dropna(subset='salary', inplace=True)
    salary_experience = df.groupby('years_of_experience')['salary'].mean().round(2)

    return Response(salary_experience.to_dict())
