from django.urls import path,include
from user import views

app_name="user"
urlpatterns = [
    path('Homepage',views.Homepage,name="user-homepage"),
    path('ViewProfile',views.ViewProfile,name="user-profile")
   
]
