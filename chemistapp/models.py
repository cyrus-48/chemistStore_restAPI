
from django.db import models

# Create your models here.
class Chemist(models.Model):
    chemist_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    license_no=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    contact_no=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    added_on=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Medicine(models.Model):
    medicine_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    medical_typ=models.CharField(max_length=255)
    buy_price=models.CharField(max_length=255)
    sell_price=models.CharField(max_length=255)
    expire_date=models.DateField()
    chemist_id=models.ForeignKey(Chemist,on_delete=models.CASCADE)
    description=models.CharField(max_length=255)
    in_stock_total=models.IntegerField()
    added_on=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class MedicalDetails(models.Model):
    details_id=models.AutoField(primary_key=True)
    medicine_id=models.ForeignKey(Medicine,on_delete=models.CASCADE)
    salt_name=models.CharField(max_length=255)
    salt_qty=models.CharField(max_length=255)
    salt_qty_type=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    added_on=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Staff(models.Model):
    staff_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    joining_date=models.DateField()
    phone=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    added_on=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Customer(models.Model):
    customer_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    contact=models.CharField(max_length=255)
    added_on=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Bill(models.Model):
    bill_id=models.AutoField(primary_key=True)
    customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    added_on=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class StaffSalary(models.Model):
    salary_id=models.AutoField(primary_key=True)
    staff_id=models.ForeignKey(Staff,on_delete=models.CASCADE)
    salary_date=models.DateField()
    salary_amount=models.CharField(max_length=255)
    added_on=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class BillDetails(models.Model):
    billdetail_id=models.AutoField(primary_key=True)
    bill_id=models.ForeignKey(Bill,on_delete=models.CASCADE)
    medicine_id=models.ForeignKey(Medicine,on_delete=models.CASCADE)
    qty=models.IntegerField()
    added_on=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class CustomerRequest(models.Model):
    request_id=models.AutoField(primary_key=True)
    customer_name=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    medicine_details=models.CharField(max_length=255)
    status=models.BooleanField(default=False)
    added_on=models.DateTimeField(auto_now_add=True)
    prescription=models.FileField(default="")
    objects=models.Manager()

class ChemistAccount(models.Model):
    choices=((1,"Debit"),(2,"Credit"))
    payment_mode =((1,"Cash"),(2,"Mpesa"))
    account_id=models.AutoField(primary_key=True)
    chemist_id=models.ForeignKey(Chemist,on_delete=models.CASCADE)
    transaction_type=models.CharField(choices=choices,max_length=255)
    transaction_amt=models.CharField(max_length=255)
    transaction_date=models.DateField()
    payment_mode=models.CharField(choices=payment_mode,max_length=255)
    added_on=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class ChemistBank(models.Model):
    bank_id=models.AutoField(primary_key=True)
    bank_account_no=models.CharField(max_length=255)
    chemist_id=models.ForeignKey(Chemist,on_delete=models.CASCADE)
    added_on=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class StaffBank(models.Model):
    bank_id=models.AutoField(primary_key=True)
    bank_account_no=models.CharField(max_length=255)
    staff_id=models.ForeignKey(Staff,on_delete=models.CASCADE)
    added_on=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()




