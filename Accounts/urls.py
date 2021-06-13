from django.urls import path,include
from Accounts import views

app_name="Accounts"
urlpatterns = [
    path("login/",views.Login,name="login"),
    path("HospitalRegistration/",views.RegisterHospital,name="HospitalSignup"),
    path("Ajax_load_place/",views.AjaxPalce,name="AjaxPlaces"),
    path("UserRegistration/",views.RegisterUser,name="UserSignup"),
    path("Registration/",views.Registration,name="Registration")
]


# Accounts URLS

# http://127.0.0.1:8000/accounts/Registration/

# http://127.0.0.1:8000/accounts/HospitalRegistration/
# http://127.0.0.1:8000/accounts/login/

# http://127.0.0.1:8000/accounts/UserRegistration/
# http://127.0.0.1:8000/accounts/userLogin/

