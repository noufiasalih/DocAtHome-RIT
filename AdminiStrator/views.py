from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from Accounts.models import Hospital
from Hospital.models import Complaints
from user.models import UserComplaints

def Homepage(request):
    return render(request,"Administrator/HomePage.html",{})

def PendingHospitalVerification(request):
    recordSet=Hospital.objects.filter(hospital_status=0)
    return render(request,"AdminiStrator/HospitalVerifications.html",{"HospitalData":recordSet})

def AcceptHospital(request,id):
    hospitalData=Hospital.objects.get(id=id)
    hospitalData.hospital_status=1
    hospitalData.save()
    return redirect("/administrator/HospitalVerification")

def RejectHospital(request,id):
    hospitalData=Hospital.objects.get(id=id)
    hospitalData.hospital_status=2
    hospitalData.save()
    return redirect("/administrator/HospitalVerification")

def AcceptedHospitalList(request):
    recordSet=Hospital.objects.filter(hospital_status=1)
    return render(request,"AdminiStrator/AcceptedHospitals.html",{"HospitalData":recordSet})


def RejectedHospitalList(request):
    recordSet=Hospital.objects.filter(hospital_status=2)
    return render(request,"AdminiStrator/RejectedHospitals.html",{"HospitalData":recordSet})

def ManageStaffs(request):
    pass

def ManageMobileServices(request):
    pass

def ManageServicesPackages(request):
    pass

def ViewHospitalComplaints(request):
    if request.method=="POST":
        print(request.POST.get("hiddenHospitalId"))
        return redirect('/administrator/HomePage')
    else :
        recordSet=Complaints.objects.filter(hcomplaint_isfix="No")
        return render(request,"AdminiStrator/ViewHospitalComplants.html",{"hospitalComplaints":recordSet})

def ViewUsersComplaints(request):
    recordSet=UserComplaints.objects.filter(ucomplaint_isfix="No")
    return render(request,"AdminiStrator/ViewUsersComplaints.html",{"userComplaints":recordSet})

def ReplyHospitalComplaints(request):
    #recordSet=Complaints.objects.filter(hcomplaint_isfix="No")
    return redirect('/administrator/HomePage')


    






