from django.urls import path,include
from Hospital import views

app_name="Hospital"
urlpatterns = [
    path('HomePage/',views.Homepage,name="hospital-homepage"),
    path('ViewProfile/',views.ViewProfile,name="hospital-profile"),
   
]
