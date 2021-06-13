from django.db import models
from Accounts.models import Hospital
from MasterEntry.models import ServiceType,ServiceDesignation,ComplaintType

class dailyservice(models.Model):
    service_code=models.CharField(max_length=10,null=False,unique=True)
    service_type=models.CharField(max_length=5,null=False)
    service_rate=models.CharField(max_length=5,null=False)
    service_description=models.TextField()
    service_facilities=models.TextField()
    service_kmrate=models.CharField(max_length=5,null=False)
    service_hospital=models.ForeignKey(Hospital,on_delete=models.SET_NULL,null=True)

class servicespackage(models.Model):
    sp_code=models.CharField(max_length=10,null=False,unique=True)
    sp_rate=models.CharField(max_length=10,null=False)
    sp_duration=models.CharField(max_length=10,null=False)
    sp_facilitites=models.TextField()
    sp_type=models.ForeignKey(ServiceType,on_delete=models.SET_NULL,null=True)
    sp_hospital=models.ForeignKey(Hospital,on_delete=models.SET_NULL,null=True)

class servicestaff(models.Model):
    staff_name=models.CharField(max_length=10,null=False,default=False)
    staff_designation=models.ForeignKey(ServiceDesignation,on_delete=models.SET_NULL,null=True)
    staff_gender=models.CharField(max_length=10,null=False)
    staff_contact=models.CharField(max_length=11,null=False)
    staff_email=models.EmailField(max_length=11,null=False,unique=True)
    staff_photo=models.ImageField(upload_to="StaffPhoto/")
    staff_username=models.CharField(max_length=11,null=False,unique=True)
    staff_password=models.CharField(max_length=11,null=False,unique=True)
    staff_isactive=models.CharField(max_length=11,null=False,default="Yes")
    staff_unitcode=models.CharField(max_length=11,null=False,unique=True)
    staff_hospital=models.ForeignKey(Hospital,on_delete=models.SET_NULL,null=True)

class Complaints(models.Model):
    hcomplaint_hospital=models.ForeignKey(Hospital,on_delete=models.SET_NULL,null=True)
    hcomplaint_type=models.ForeignKey(ComplaintType,on_delete=models.SET_NULL,null=True)
    hcomplaint_content=models.TextField()
    hcomplaint_date=models.DateField(auto_now_add=True)
    hcomplaint_time=models.TimeField(auto_now_add=True)
    hcomplaint_isfix=models.CharField(max_length=5,default="No")

class Mobilehospital(models.Model):
    service_no=models.CharField(max_length=10,null=False,unique=True)
    service_type=models.ForeignKey(ServiceType,on_delete=models.SET_NULL,null=True)
    service_rate=models.IntegerField(null=False,unique=True)
    service_image=models.ImageField(upload_to="MobileHospitalPhoto/")
    service_description=models.TextField(null=False)
    service_basicrate=models.IntegerField(null=False,unique=True)
    service_km_rate=models.IntegerField(null=False,unique=True)
    service_status=models.CharField(max_length=10,null=False,unique=True)

