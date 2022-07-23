from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from chemistapp.models import Chemist, Medicine, Customer, Bill, Staff, MedicalDetails, CustomerRequest, ChemistAccount, \
    StaffBank, StaffSalary, BillDetails, ChemistBank
from chemistapp.serializers import ChemistSerializer, MedicineSerializer, CustomerSerializer, BillSerializer, \
    StaffSerializer, MedicalDetailsSerializer, CustomerRequestSerializer, ChemistAccountSerializer, StaffBankSerializer, \
    StaffSalarySerializer, BillDetailsSerializer, ChemistBankSerializer


class ChemistViewSet(viewsets.ViewSet):

    def list(self, request):
        try:
            chemist = Chemist.objects.all()
            serializer = ChemistSerializer(chemist, many=True, context={"request": request})
            response_dict = {"error": False, "message": "All chemist details", "data": serializer.data}
            return Response(response_dict)
        except:
            response_dict = {"error": True, "message": "Error while fetching details chemist details"}
            return Response(response_dict)

    # method for updating
    def create(self, request):
        try:
            serializer = ChemistSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "data saved successfully"}
            return Response(dict_response)

        except:
            dict_response = {"error": True, "message": "Error during saving chemist data"}
            return Response(dict_response)

    def update(self, request, pk=None):
        try:
            queryset = Chemist.objects.all()
            chemist = get_object_or_404(queryset, pk=pk)
            serializer = ChemistSerializer(data=request.data, context={"request": request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "chemist data update successfully"}
            return Response(dict_response)
        except:
            dict_response = {"error": True, "message": "Error during updating chemist data "}
            return Response(dict_response)


class MedicineViewSet(viewsets.ViewSet):

    def list(self, request):
        try:
            medicine = Medicine.objects.all()
            serializer = MedicineSerializer(medicine, many=True, context={"request": request})
            response_dict = {"error": False, "message": "All medicine details", "data": serializer.data}
            return Response(response_dict)
        except:
            response_dict = {"error": True, "message": "Error while medicine details"}
            return Response(response_dict)

    # method for updating
    def create(self, request):
        try:
            serializer = MedicineSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "data saved successfully"}
            return Response(dict_response)

        except:
            dict_response = {"error": True, "message": "Error during saving medicine  data"}
            return Response(dict_response)

    def update(self, request, pk=None):
        try:
            queryset = Medicine.objects.all()
            chemist = get_object_or_404(queryset, pk=pk)
            serializer = MedicineSerializer(data=request.data, context={"request": request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "Medicine data update successfully"}
            return Response(dict_response)
        except:
            dict_response = {"error": True, "message": "Error during updating Medicine  data "}
            return Response(dict_response)


class CustomerViewSet(viewsets.ViewSet):

    def list(self, request):
        try:
            customer = Customer.objects.all()
            serializer = CustomerSerializer(customer, many=True, context={"request": request})
            response_dict = {"error": False, "message": "All medicine details", "data": serializer.data}
            return Response(response_dict)
        except:
            response_dict = {"error": True, "message": "Error while medicine details"}
            return Response(response_dict)

    # method for updating
    def create(self, request):
        try:
            serializer = CustomerSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "data saved successfully"}
            return Response(dict_response)

        except:
            dict_response = {"error": True, "message": "Error during saving medicine  data"}
            return Response(dict_response)

    def update(self, request, pk=None):
        try:
            queryset = Customer.objects.all()
            customer = get_object_or_404(queryset, pk=pk)
            serializer = CustomerSerializer(data=request.data, context={"request": request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "Customer data update successfully"}
            return Response(dict_response)
        except:
            dict_response = {"error": True, "message": "Error during updating Customer  data "}
            return Response(dict_response)


class ChemistBankViewSet(viewsets.ViewSet):

    def list(self, request):
        try:
            bank = ChemistBank.objects.all()
            serializer = ChemistBankSerializer(bank, many=True, context={"request": request})
            response_dict = {"error": False, "message": "All  chemist bank details", "data": serializer.data}
            return Response(response_dict)
        except:
            response_dict = {"error": True, "message": "Error while medicine details"}
            return Response(response_dict)

    # method for updating
    def create(self, request):
        try:
            serializer = ChemistBankSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "data saved successfully"}
            return Response(dict_response)

        except:
            dict_response = {"error": True, "message": "Error during saving  cheist bank  data"}
            return Response(dict_response)

    def update(self, request, pk=None):
        try:
            queryset = ChemistBank.objects.all()
            chemist = get_object_or_404(queryset, pk=pk)
            serializer = ChemistBankSerializer(data=request.data, context={"request": request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": " chemist bank data update successfully"}
            return Response(dict_response)
        except:
            dict_response = {"error": True, "message": "Error during updating chemist bank data "}
            return Response(dict_response)


class BillViewSet(viewsets.ViewSet):

    def list(self, request):
        try:
            bill = Bill.objects.all()
            serializer = BillSerializer(bill, many=True, context={"request": request})
            response_dict = {"error": False, "message": "All bill details", "data": serializer.data}
            return Response(response_dict)
        except:
            response_dict = {"error": True, "message": "Error while listing  medicine details"}
            return Response(response_dict)

    # method for updating
    def create(self, request):
        try:
            serializer = BillSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "data saved successfully"}
            return Response(dict_response)

        except:
            dict_response = {"error": True, "message": "Error during saving medicine  data"}
            return Response(dict_response)

    def update(self, request, pk=None):
        try:
            queryset = Bill.objects.all()
            chemist = get_object_or_404(queryset, pk=pk)
            serializer = BillSerializer(data=request.data, context={"request": request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "Medicine data update successfully"}
            return Response(dict_response)
        except:
            dict_response = {"error": True, "message": "Error during updating Medicine  data "}
            return Response(dict_response)


class StaffViewSet(viewsets.ViewSet):

    def list(self, request):
        try:
            staff = Staff.objects.all()
            serializer = ChemistSerializer(staff, many=True, context={"request": request})
            response_dict = {"error": False, "message": "All medicine details", "data": serializer.data}
            return Response(response_dict)
        except:
            response_dict = {"error": True, "message": "Error while medicine details"}
            return Response(response_dict)

    # method for updating
    def create(self, request):
        try:
            serializer = StaffSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "data saved successfully"}
            return Response(dict_response)

        except:
            dict_response = {"error": True, "message": "Error during saving medicine  data"}
            return Response(dict_response)

    def update(self, request, pk=None):
        try:
            queryset = Staff.objects.all()
            staff = get_object_or_404(queryset, pk=pk)
            serializer = StaffSerializer(data=request.data, context={"request": request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "Medicine data update successfully"}
            return Response(dict_response)
        except:
            dict_response = {"error": True, "message": "Error during updating Medicine  data "}
            return Response(dict_response)


class MedicalDetailsViewSet(viewsets.ViewSet):

    def list(self, request):
        try:
            medicaldetails = MedicalDetails.objects.all()
            serializer = MedicalDetailsSerializer(medicaldetails, many=True, context={"request": request})
            response_dict = {"error": False, "message": "All medicine details", "data": serializer.data}
            return Response(response_dict)
        except:
            response_dict = {"error": True, "message": "Error while listing medical details"}
            return Response(response_dict)

    # method for updating
    def create(self, request):
        try:
            serializer = MedicalDetailsSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "data saved successfully"}
            return Response(dict_response)

        except:
            dict_response = {"error": True, "message": "Error during saving medicine  data"}
            return Response(dict_response)

    def update(self, request, pk=None):
        try:
            queryset = MedicalDetails.objects.all()
            chemist = get_object_or_404(queryset, pk=pk)
            serializer = MedicalDetailsSerializer(data=request.data, context={"request": request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "Medicine data update successfully"}
            return Response(dict_response)
        except:
            dict_response = {"error": True, "message": "Error during updating Medicine  data "}
            return Response(dict_response)
        # viewset for the customer request serializer


class CustomerRequestViewSet(viewsets.ViewSet):

    def list(self, request):
        try:
            customerrequest = CustomerRequest.objects.all()
            serializer = ChemistSerializer(customerrequest, many=True, context={"request": request})
            response_dict = {"error": False, "message": "All medicine details", "data": serializer.data}
            return Response(response_dict)
        except:
            response_dict = {"error": True, "message": "Error while listing customer requests details"}
            return Response(response_dict)

    # method for updating
    def create(self, request):
        try:
            serializer = CustomerRequestSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "data saved successfully"}
            return Response(dict_response)

        except:
            dict_response = {"error": True, "message": "Error during saving customer requests  data"}
            return Response(dict_response)

    def update(self, request, pk=None):
        try:
            queryset = CustomerRequest.objects.all()
            chemist = get_object_or_404(queryset, pk=pk)
            serializer = CustomerRequestSerializer(data=request.data, context={"request": request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "Customer request updated  successfully"}
            return Response(dict_response)
        except:
            dict_response = {"error": True, "message": "Error during updating customer requests  data "}
            return Response(dict_response)


class ChemistAccountViewSet(viewsets.ViewSet):

    def list(self, request):
        try:
            account = ChemistAccount.objects.all()
            serializer = ChemistAccountSerializer(account, many=True, context={"request": request})
            response_dict = {"error": False, "message": "All chemist account details", "data": serializer.data}
            return Response(response_dict)
        except:
            response_dict = {"error": True, "message": "Error while listing chemist account  details"}
            return Response(response_dict)

    # method for updating
    def create(self, request):
        try:
            serializer = ChemistAccountSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "data saved successfully"}
            return Response(dict_response)

        except:
            dict_response = {"error": True, "message": "Error during saving chemist account  data"}
            return Response(dict_response)

    def update(self, request, pk=None):
        try:
            queryset = ChemistAccount.objects.all()
            chemist = get_object_or_404(queryset, pk=pk)
            serializer = ChemistAccountSerializer(data=request.data, context={"request": request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "chemist account  data updated successfully"}
            return Response(dict_response)
        except:
            dict_response = {"error": True, "message": "Error during updating chemist account  data "}
            return Response(dict_response)


class StaffBankViewSet(viewsets.ViewSet):

    def list(self, request):
        try:
            staffbank = StaffBank.objects.all()
            serializer = StaffBankSerializer(staffbank, many=True, context={"request": request})
            response_dict = {"error": False, "message": "All medicine details", "data": serializer.data}
            return Response(response_dict)
        except:
            response_dict = {"error": True, "message": "Error while  staf  bank details"}
            return Response(response_dict)

    # method for updating
    def create(self, request):
        try:
            serializer = StaffBankSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "data saved successfully"}
            return Response(dict_response)

        except:
            dict_response = {"error": True, "message": "Error during saving  staff bank  data"}
            return Response(dict_response)

    def update(self, request, pk=None):
        try:
            queryset = StaffBank.objects.all()
            bank = get_object_or_404(queryset, pk=pk)
            serializer = StaffBankSerializer(data=request.data, context={"request": request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "Staff bank data update successfully"}
            return Response(dict_response)
        except:
            dict_response = {"error": True, "message": "Error during updating staff bank  data "}
            return Response(dict_response)


class StaffSalaryViewSet(viewsets.ViewSet):

    def list(self, request):
        try:
            salary = StaffSalary.objects.all()
            serializer = StaffSalarySerializer(salary, many=True, context={"request": request})
            response_dict = {"error": False, "message": "All staff salary details", "data": serializer.data}
            return Response(response_dict)
        except:
            response_dict = {"error": True, "message": "Error while listing staff salary details"}
            return Response(response_dict)

    # method for updating
    def create(self, request):
        try:
            serializer = StaffSalarySerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "data saved successfully"}
            return Response(dict_response)

        except:
            dict_response = {"error": True, "message": "Error during saving staff salary  data"}
            return Response(dict_response)

    def update(self, request, pk=None):
        try:
            queryset = StaffSalary.objects.all()
            chemist = get_object_or_404(queryset, pk=pk)
            serializer = StaffSalarySerializer(data=request.data, context={"request": request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "Staff salary data update successfully"}
            return Response(dict_response)
        except:
            dict_response = {"error": True, "message": "Error during updating staff salary  data "}
            return Response(dict_response)


class BillDetailsViewSet(viewsets.ViewSet):

    def list(self, request):
        try:
            details = BillDetails.objects.all()
            serializer = BillDetailsSerializer(details, many=True, context={"request": request})
            response_dict = {"error": False, "message": "All details details", "data": serializer.data}
            return Response(response_dict)
        except:
            response_dict = {"error": True, "message": "Error while medicine details"}
            return Response(response_dict)

    # method for updating
    def create(self, request):
        try:
            serializer = BillDetailsSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "data saved successfully"}
            return Response(dict_response)

        except:
            dict_response = {"error": True, "message": "Error during saving  Bill details   data"}
            return Response(dict_response)

    def update(self, request, pk=None):
        try:
            queryset = BillDetails.objects.all()
            bill = get_object_or_404(queryset, pk=pk)
            serializer = BillDetailsSerializer(data=request.data, context={"request": request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "Bill Details data update successfully"}
            return Response(dict_response)
        except:
            dict_response = {"error": True, "message": "Error during updating Bill details  data "}
            return Response(dict_response)


chemist_list = ChemistViewSet.as_view({"get": "list"})
chemist_create = ChemistViewSet.as_view({"post": "create"})
chemist_update = ChemistViewSet.as_view({"put": "update"})
