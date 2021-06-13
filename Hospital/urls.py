from django.urls import path,include
from Hospital import views

app_name="Hospital"
urlpatterns = [
    path('HomePage/',views.Homepage,name="hospital-homepage"),
    path('ViewProfile/',views.ViewProfile,name="hospital-profile"),
    path('dailyservices/',views.DailyService,name="daily-services"),
    path('servicepackages/',views.ServicePackage,name="services-packages"),
    path('servicestaffs/',views.ServiceStaff,name="services-staffs"),
    path('ViewDailyService/',views.ViewDailyService,name="view-daily-services"),
    path('ViewPackages/',views.ViewPackages,name="view-packages"),
    path('ViewStaffs/',views.ViewStaffs,name="view-staffs"),
    path('UserComplaints/',views.UserComplaints,name="user-complaints"),
    path('AddComplaints/',views.AddComplaints,name="user-add-complaint"),
]
