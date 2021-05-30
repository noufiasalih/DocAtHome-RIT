from django.urls import path,include
from Accounts import views

app_name="Accounts"
urlpatterns = [
    path("login/",views.Login,name="login"),
    path("HospitalRegistration/",views.RegisterHospital,name="HospitalSignup"),
    path("Ajax_load_place/",views.AjaxPalce,name="AjaxPlaces"),
    path("UserRegistration/",views.RegisterUser,name="UserSignup"),
    path("userLogin/",views.Userlogin,name="userLogin"),
    path("Registration/",views.Registration,name="Registration")
]
