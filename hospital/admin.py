from django.contrib import admin
from .models import Patients, Doctors, Patient_Pay_Tran, Room, Appointment
# Register your models here.
admin.site.register(Patients)
admin.site.register(Doctors)
admin.site.register(Patient_Pay_Tran)
admin.site.register(Room)
admin.site.register(Appointment)
#admin login:- kulkarni password :- Python@123