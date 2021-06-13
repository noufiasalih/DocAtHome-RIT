from django.urls import path,include
from AdminiStrator import views

app_name="AdminiStrator"
urlpatterns = [
    path('HomePage/',views.Homepage,name="admin-homepage"),
    path("HospitalVerification/",views.PendingHospitalVerification,name="pending-hospital-verification"),
    path("AcceptingHospital/<int:id>",views.AcceptHospital,name="accept-hospitals"),
    path("RejectingingHospital/<int:id>",views.RejectHospital,name="reject-hospitals"),
    path("ViewAcceptedHospitals/",views.AcceptedHospitalList,name="accepted-hospital-list"),
    path("ViewRejectedHospitals/",views.RejectedHospitalList,name="rejected-hopital-list"),
    path("ViewUsersComplaints/",views.ViewUsersComplaints,name="view-user-complaints"),
    path("ViewHospitalComplaints/",views.ViewHospitalComplaints,name="view-hospital-complaints")
]
