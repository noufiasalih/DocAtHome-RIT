from django.db import models
from MasterEntry.models import ComplaintType
from Accounts.models import Users
from Hospital.models import Mobilehospital

class UserComplaints(models.Model):
    ucomplaint_user=models.ForeignKey(Users,on_delete=models.SET_NULL,null=True)
    ucomplaint_type=models.ForeignKey(ComplaintType,on_delete=models.SET_NULL,null=True)
    ucomplaint_mobile_hospital=models.ForeignKey(Mobilehospital,on_delete=models.SET_NULL,null=True)
    ucomplaint_content=models.TextField(null=False)
    ucomplaint_date=models.DateField(auto_now_add=True)
    ucomplaint_time=models.TimeField(auto_now_add=True)
    ucomplaint_isfix=models.CharField(max_length=5,default="No")
