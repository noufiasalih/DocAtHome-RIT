from django.shortcuts import render
from Accounts.models import Hospital
from MasterEntry.models import Place
from django.shortcuts import redirect

def Homepage(request):
    if 'sessionHospitalId' not in request.session:
        return redirect('/accounts/hospitalLogin')
    else :
        return render(request,"Hospital/HomePage.html",{})

def ViewProfile(request):
    if 'sessionHospitalId' not in request.session:
        return redirect('/accounts/hospitalLogin')
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

    
