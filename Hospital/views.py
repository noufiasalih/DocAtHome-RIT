from django.db.models.fields import DateField, TimeField
from django.shortcuts import render
from django.shortcuts import redirect
from Accounts.models import Hospital
from MasterEntry.models import Place,ServiceDesignation,ServiceType,ComplaintType
from .models import dailyservice, servicespackage, servicestaff,Complaints


def Homepage(request):
    if 'sessionHospitalId' not in request.session:
        return redirect('/accounts/login')
    else :
        return render(request,"Hospital/HomePage.html",{})

def ViewProfile(request):
    if 'sessionHospitalId' not in request.session:
        return redirect('/accounts/login')
    else :
        HospitalData=Hospital.objects.get(id=request.session["sessionHospitalId"])
        placeData=Place.objects.get(id=HospitalData.hospital_place_id)
    
        context={
            "HospitalName":HospitalData.hospital_name,
            "HospitalContact":HospitalData.hospital_contact,
            "HospitalEmail":HospitalData.hospital_email,
            "HospitalAddress":HospitalData.hospital_address,
            "HospitalDistrict":placeData.PlaceDistrict,
            "HospitalPlace":HospitalData.hospital_place,
            "HopitalImage":HospitalData.hospital_image,
        }
        return render(request,"Hospital/ViewProfile.html",context)

def DailyService(request):
   
    hospitalObj=Hospital.objects.get(id=request.session["sessionHospitalId"])
  
    allServices=dailyservice.objects.filter(service_hospital=hospitalObj)
    if request.method=="POST":
        
        dailyservice.objects.create(
                service_code=request.POST.get("txtServiceCode"),
                service_type=request.POST.get("slctServiceType"),
                service_rate=request.POST.get("txtServiceRate"),
                service_description=request.POST.get("txtDescription"),
                service_facilities=request.POST.get("txtFacilitites"),
                service_kmrate=request.POST.get("txtKmRate"),
                service_hospital=hospitalObj
            )
        return render(request,"Hospital/ManageDailyServices.html",{"allServices":allServices})
    else:
        return render(request,"Hospital/ManageDailyServices.html",{"allServices":allServices})
    

def ServicePackage(request):
    hospitalObj=Hospital.objects.get(id=request.session["sessionHospitalId"])
    serviceTypeRecords=ServiceType.objects.all()
    if request.method=="POST":
        servicespackage.objects.create(
            sp_code=request.POST.get("txtPackageCode"),
            sp_rate=request.POST.get("txtPackageRate"),
            sp_duration=request.POST.get("txtDuration"),
            sp_facilitites=request.POST.get("txtFacilitites"),
            sp_type=ServiceType.objects.get(id=request.POST.get("slctServiceType")),
            sp_hospital= hospitalObj
        )
        return render(request,"Hospital/ManagePackages.html",{"ServiceTypes":serviceTypeRecords})
    else:
        return render(request,"Hospital/ManagePackages.html",{"ServiceTypes":serviceTypeRecords})


def ServiceStaff(request):
    hospitalObj=Hospital.objects.get(id=request.session["sessionHospitalId"])
    serviceDesignationRecords=ServiceDesignation.objects.all()
    if request.method=="POST" and request.FILES:
        servicestaff.objects.create(
            
            staff_name=request.POST.get("txtStaffName"),
            staff_designation=ServiceDesignation.objects.get(id=request.POST.get("slctDesignation")),
            staff_gender=request.POST.get("rdbGender"),
            staff_contact=request.POST.get("txtContact"),
            staff_email=request.POST.get("txtEmail"),
            staff_photo=request.FILES.get("fileStaffPhoto"),
            staff_username=request.POST.get("txtUsername"),
            staff_password=request.POST.get("txtPassword"),
            staff_unitcode=request.POST.get("txtStaffCode"),
            staff_hospital=hospitalObj
        )
        return render(request,"Hospital/ManageStaffs.html",{"ServiceDesignations":serviceDesignationRecords})
    else:
        return render(request,"Hospital/ManageStaffs.html",{"ServiceDesignations":serviceDesignationRecords})

def ViewDailyService(request):
    if 'sessionHospitalId' not in request.session:
        return redirect('/accounts/login')
    else :
        ServiceData=dailyservice.objects.get(service_hospital=request.session["sessionHospitalId"])
    
        context={
            "ServiceCode":ServiceData.service_code,
            "ServiceType":ServiceData.service_type,
            "ServiceRate":ServiceData.service_rate,
            "Description":ServiceData.service_description,
            "Facilities":ServiceData.service_facilities,
            "KMRate":ServiceData.service_kmrate,
           
        }
        return render(request,"Hospital/ViewDailyService.html",context)

def ViewPackages(request):
    if 'sessionHospitalId' not in request.session:
        return redirect('/accounts/login')
    else :
        PackageData=servicespackage.objects.get(sp_hospital=request.session["sessionHospitalId"])
        
        context={
            "PackageCode":PackageData.sp_code,
            "PackageType":PackageData.sp_type,
            "PackageRate":PackageData.sp_rate,
            "Duration":PackageData.sp_duration,
            "Facilities":PackageData.sp_facilitites,
            "KMRate":PackageData.sp_rate,
        }
        return render(request,"Hospital/ViewPackages.html",context)

def ViewStaffs(request):
    if 'sessionHospitalId' not in request.session:
        return redirect('/accounts/login')
    else :
        StaffData=servicestaff.objects.get(staff_hospital=request.session["sessionHospitalId"])
    
        context={
            "StaffCode":StaffData.staff_unitcode,
            "Name":StaffData.staff_name,
            "Contact":StaffData.staff_contact,
            "Gender":StaffData.staff_gender,
            "Email":StaffData.staff_email,
            "Designation":StaffData.staff_designation,
            "StaffImage":StaffData.staff_photo,
        }
        return render(request,"Hospital/ViewStaffs.html",context)

def AddComplaints(request):
    hospitalObj=Hospital.objects.get(id=request.session["sessionHospitalId"])
    ComplaintTypeRecords = ComplaintType.objects.all()
    if request.method=="POST":
        Complaints.objects.create(
            hcomplaint_hospital=hospitalObj,
            hcomplaint_type=ComplaintType.objects.get(id=request.POST.get("slctComplaintType")),
            hcomplaint_content=request.POST.get("txtcontent")
        )
        return render(request,"Hospital/ComplaintBox.html",{"Complainttype":ComplaintTypeRecords})
    else:
        return render(request,"Hospital/complaintBox.html",{"Complainttype":ComplaintTypeRecords})

def UserComplaints(request):
    recordSet=UserComplaints.objects.filter(ucomplaint_mobile_hospital_id=request.session["sessionHospitalId"])
    return render(request,"Hospital/ViewUsersComplaints.html",{"usersComplaints":recordSet})


