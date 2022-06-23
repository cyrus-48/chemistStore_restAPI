"""chemiststore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.contrib import admin
from chemistapp import views

router = routers.DefaultRouter()
router.register("chemist",views.ChemistViewSet,basename="chemist")
router.register("medicine",views.MedicineViewSet, basename= "medicine")
router.register("customer",views.CustomerViewSet, basename= "customer")
router.register("bill",views.BillViewSet,basename= "bill")
router.register("billdetails",views.BillDetailsViewSet, basename= "billdetails")
router.register("staff",views.StaffViewSet, basename= "staff")
router.register("medicaldetails",views.MedicalDetailsViewSet,basename= "medicaldetails")
router.register("customerrequest",views.CustomerRequestViewSet, basename="customerrequest")
router.register("chemistaccount",views.ChemistAccountViewSet, basename= "chemistaccount")
router.register("staffSalary",views.StaffSalaryViewSet, basename= "staffsalary")
router.register("staffbank",views.StaffBankViewSet, basename= "staffbank")
router.register("chemistbank",views.ChemistBankViewSet, basename= "chemistbank")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)) 
]
