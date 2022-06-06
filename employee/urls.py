#  Created by btrif Trif on 03-06-2022 , 2:24 PM.

from django.urls import path, include
from rest_framework import routers
from . import views
import django

router = routers.DefaultRouter()

router.register('employee', views.EmployeeView)
router.register('industry', views.EmployeeIndustryView, basename='industry')

urlpatterns = [
    # path('', include(router.urls)),
    # path('', views.apiOverview, name="api-overview"),
    # path('employee-list/', views.employeeList, name="employee-list"),
    # path('employee-detail/', views.employeeDetail, name="employee-detail"),

]

# no Pain, no Gain - ModelViewSets
urlpatterns += router.urls


