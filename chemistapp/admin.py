from django.contrib import admin

# Register your models here.
from chemistapp.models import *

admin.site.register(Chemist)
admin.site.register(Medicine)
admin.site.register(MedicalDetails)
admin.site.register(Staff)
admin.site.register(Customer)
admin.site.register(Bill)
admin.site.register(StaffSalary)
admin.site.register(BillDetails)
admin.site.register(CustomerRequest)
admin.site.register(ChemistAccount)
admin.site.register(ChemistBank)
admin.site.register(StaffBank)