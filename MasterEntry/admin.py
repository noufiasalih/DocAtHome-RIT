from django.contrib import admin

from .models import District,Place,ServiceType,ServiceDesignation,HospitalType,ComplaintType

admin.site.register(District)
admin.site.register(Place)
admin.site.register(ServiceType)
admin.site.register(ServiceDesignation)
admin.site.register(HospitalType)
admin.site.register(ComplaintType)
