from django.shortcuts import redirect, render
from Accounts.models import Users,Hospital
from MasterEntry.models import Place,ComplaintType
from .models import UserComplaints
from Hospital.models import Mobilehospital

def Homepage(request):
    if 'userid' not in request.session:
        return redirect('/accounts/userLogin')
    else :
        return render(request,"user/HomePage.html",{})

def ViewProfile(request):
    if 'userid' not in request.session:
        return redirect('/accounts/userLogin')
    else :
        UserData=Users.objects.get(id=request.session["userid"])
        context={
            "UserName":UserData.user_name,
            "UserContact":UserData.user_contact,
            "UserEmail":UserData.user_email,
            "UserGender":UserData.user_gender,
            "UserUserName":UserData.user_username,
            "UserPlace":UserData.user_place
        }
        return render(request,"user/ViewProfile.html",context)

def AddComplaints(request):
    userObj=Users.objects.get(id=request.session["userid"])
    ComplainttypeRecords = ComplaintType.objects.all()
    mobileHospitalData = Mobilehospital.objects.all()
    print(request.POST.get("slctMobileHospital"))
    if request.method=="POST":
        UserComplaints.objects.create(
            ucomplaint_user=userObj,
            ucomplaint_mobile_hospital=Mobilehospital.objects.get(id=request.POST.get("slctMobileHospital")),
            ucomplaint_type=ComplaintType.objects.get(id=request.POST.get("slctComplaintType")),
            ucomplaint_content=request.POST.get("txtcontent")
        )
        return render(request,"user/ComplaintBox.html",{"ComplaintType":ComplainttypeRecords,"mobileHospitalData":mobileHospitalData})
    else:
        return render(request,"user/ComplaintBox.html",{"ComplaintType":ComplainttypeRecords,"mobileHospitalData":mobileHospitalData})

    