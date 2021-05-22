from django.db import models
from MasterEntry.models import Place,HospitalType

class Hospital(models.Model):
    hospital_name=models.CharField(max_length=20)
    hospital_contact=models.CharField(max_length=15)
    hospital_email=models.EmailField(default=True)
    hospital_address=models.TextField(blank=True)
    hospital_place=models.ForeignKey(Place,on_delete=models.SET_NULL,null=True)
    hospital_type=models.ForeignKey(HospitalType,on_delete=models.SET_NULL,null=True)
    hospital_proof=models.FileField(upload_to='HospitalProof/')
    hospital_image=models.ImageField(upload_to="HospitalImage/")
    hospital_username=models.CharField(max_length=15,default=True)
    hospital_password=models.CharField(max_length=15,default=True)
    hospital_status=models.IntegerField(default=0)
    hospital_doj=models.DateField(auto_now_add=True)

class Users(models.Model):
    user_name=models.CharField(max_length=10,default=True)
    user_contact=models.CharField(max_length=20,default=True)
    user_email=models.EmailField(default=True)
    user_place=models.ForeignKey(Place,on_delete=models.SET_NULL,null=True)
    user_gender=models.CharField(max_length=20,default=True)
    user_username=models.CharField(max_length=20,default=True)
    user_password=models.CharField(max_length=20,default=True)
    user_status=models.IntegerField(default=0)

    
