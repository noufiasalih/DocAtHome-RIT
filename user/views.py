from django.shortcuts import redirect, render
from Accounts.models import Users


from MasterEntry.models import Place

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

    