from django.db import models
from django.core.validators import RegexValidator


isalphanumericValidation = RegexValidator(r'^[a-zA-Z ]*$', 'Only alphabetic characters are allowed.')

class District(models.Model):
    district_name=models.CharField("District",max_length=20,null=False,unique=True,validators=[isalphanumericValidation])

    def __str__(self):
        return self.district_name

class Place(models.Model):
    PlaceDistrict=models.ForeignKey(District,on_delete=models.SET_NULL,null=True,related_name="Places",verbose_name="Select District")
    place_name=models.CharField("Place",max_length=50,validators=[isalphanumericValidation],unique=True)
    
    
    def __str__(self):
        return self.place_name

class HospitalType(models.Model):
    hospitaltype_name=models.CharField("Hospital Type",max_length=20,null=False,unique=True,validators=[isalphanumericValidation])

    def __str__(self):
        return self.hospitaltype_name

class ComplaintType(models.Model):
    complainttype_name=models.CharField("Complaint Type",max_length=20,null=False,unique=True,validators=[isalphanumericValidation])

    def __str__(self):
        return self.complainttype_name

class ServiceType(models.Model):
    servicetype_name=models.CharField("Service Type",max_length=20,null=False,unique=True,validators=[isalphanumericValidation])

    def __str__(self):
        return self.servicetype_name

class ServiceDesignation(models.Model):
    service_designation=models.CharField("Service Designation",max_length=20,null=False,unique=True,validators=[isalphanumericValidation])

    def __str__(self):
        return self.service_designation
    