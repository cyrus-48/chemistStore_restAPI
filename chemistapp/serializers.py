from rest_framework import serializers

from chemistapp.models import Chemist, ChemistBank, Medicine, MedicalDetails, Staff, Customer, Bill, CustomerRequest, \
    ChemistAccount, StaffSalary, BillDetails


class ChemistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chemist
        fields = "__all__"


class ChemistBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChemistBank
        fields = "__all__"


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['Chemist'] = ChemistSerializer(instance.chemist_id).data
        return response


class MedicalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalDetails
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['Medicine'] = MedicineSerializer(instance.medicine_id).data
        return response


class MedicalDetailsSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model = MedicalDetails
        fields = "__all__"


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['Customer'] = CustomerSerializer(instance.customer_id).data
        return response


class CustomerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerRequest
        fields = "__all__"


class ChemistAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChemistAccount
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['chemist'] = ChemistSerializer(instance.chemist_id).data
        return response


class StaffAccount:
    pass


class StaffBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffAccount
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['staff'] = StaffSerializer(instance.staff_id).data
        return response


class StaffSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffSalary
        fields = "__all__"


class BillDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillDetails
        fields = "__all__"
