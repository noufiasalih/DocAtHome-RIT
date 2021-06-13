from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from MasterEntry.models import District,Place,HospitalType
from .models import Hospital, Users
from MasterEntry.models import Place
from django.template import loader

# ------------------------------------------------------------------

def AjaxPalce(request):
    district=request.GET.get("districtid")
    placeList=Place.objects.filter(PlaceDistrict=district[0])
    return render(request,"Accounts/AjaxPlace.html",{"placeList":placeList})

# ----------------------------------------------------------------------





#------------------------------------------------------------------------


def Login(request):
    if request.method=='POST':
        hospitalDataCount=Hospital.objects.filter(hospital_username=request.POST.get("txtUsername"),hospital_password=request.POST.get("txtPassword")).count()
        usersDataCount=Users.objects.filter(user_username=request.POST.get("txtUsername"),user_password=request.POST.get("txtPassword")).count()
        print(hospitalDataCount)
        if hospitalDataCount>0:
     
            hospitalobj = get_object_or_404(Hospital, hospital_username=request.POST.get("txtUsername"),hospital_password=request.POST.get("txtPassword"))
            request.session["sessionHospitalId"]=hospitalobj.id
            request.session["sessionHospitalname"]=hospitalobj.hospital_name
            return redirect('/hospital/HomePage')
   
        elif usersDataCount>0:
            usersobj = get_object_or_404(Users, user_username=request.POST.get("txtUsername"),user_password=request.POST.get("txtPassword"))
            request.session["userid"]=usersobj.id
            request.session["username"]=usersobj.user_name
            return redirect('/user/Homepage')
        else: 
            return HttpResponse("Invalid Data")
    return render(request,"Accounts/Login.html",{})

#-------------------------------------------------------------------------------------------------

def  allDistricts():
    disitrictData=District.objects.all()
    return disitrictData
def allHospitalTypes():
    hospitalTypeData=HospitalType.objects.all()
    return hospitalTypeData

def RegisterHospital(request):
    DistrictRecords=allDistricts()
    HospitalTypeRecords=allHospitalTypes()

    if request.method=="POST" and request.FILES :
        hospitalObj=J=Hospital()
        hospitalObj.hospital_name=request.POST.get("txtHname")
        hospitalObj.hospital_contact=request.POST.get("txtHcontact")
        hospitalObj.hospital_email=request.POST.get("txtHemail")
        hospitalObj.hospital_address=request.POST.get("txtHospitalAddress")
        
        hospitaltypeObj=HospitalType.objects.get(id=request.POST.get("slctHtype"))
        hospitalObj.hospital_type=hospitaltypeObj

        hospitalPlaceObj=Place.objects.get(id=request.POST.get("slctPlace"))
        hospitalObj.hospital_place=hospitalPlaceObj
        
        hospitalObj.hospital_proof=request.FILES.get("fileHProof")
        hospitalObj.hospital_image=request.FILES.get("fileHImage")
        hospitalObj.hospital_username=request.POST.get("txtUsername")
        hospitalObj.hospital_password=request.POST.get("txtPassword")
        #hospitalObj.hospital_status=1
        hospitalObj.save()
        return redirect('/accounts/login')
    else:
        return render(request,"Accounts/NewHospital.html",{'DistrictRecords':DistrictRecords,'HospitalTypeRecords':HospitalTypeRecords})
        
        
        
     #----------------------------------------------------------------------------------------------------------------------------
        
def RegisterUser(request):
    if request.method=="POST" :
        usersObj=J=Users()
        usersObj.user_name=request.POST.get("txtUname")
        usersObj.user_contact=request.POST.get("txtUcontact")
        usersObj.user_email=request.POST.get("txtUemail")
        usersObj.user_place=request.POST.get("txtUPlace")
        usersObj.user_gender=request.POST.get("Ugender")
        usersObj.user_username=request.POST.get("txtUsername")
        usersObj.user_password=request.POST.get("txtPassword")
        usersObj.user_status=1
        usersObj.save()
        return redirect('/accounts/userLogin')
    else:
        return render(request,"Accounts/NewUser.html")   

def Registration(request) :
    return render(request,"Accounts/Registration.html")