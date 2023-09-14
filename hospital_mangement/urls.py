"""hospital_mangement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hospital import views
# from .views import Patient 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.hospital_login),
    path('base/', views.BASE, name="BASE"),

    # --------- main page--------------------------
    # path('welcome/', views.Dashboard, name="Dashboard"),

    # ----------add patients ------------------------
    path('Add-patient/', views.home , name="home_page"),

    # ----------- Show all Patients-------------------
    path('show-paitanse/', views.show_patients, name="show_patients"),
    path('csvcreate-paitanse/', views.P_details.csv_create, name="csv_create"),
    path('excelcreate-paitanse/', views.P_details.excel_create, name="excel_create"),


    #------------ Edit patients --------------------
    path('edit-paitanse/<int:pk>/', views.edit_patients, name="edit_patients"),

    # ------------ delete patients---------------------------
    path('delete-paitanse/<int:pk>/', views.delete_patients, name="delete_patients"),

    #------------------add doctors --------------------------- show_patient
    path('doctor/', views.doctors, name="Add_Doctor"),

#----------------------- show doctors -------------------------------------
    path('all-doctor/', views.doctor_details, name="all_doctor"),

    path('edit-doctors/<int:pk>/', views.edit_doctor, name="edit_doctor"),
    path('delete-doctors/<int:pk>/', views.delete_doctors, name="delete_doctors"),

    path('csvcreate-doctor/', views.Doctor.csv_create, name="csv_create_doctor"),
    path('excelcreate-doctor/', views.Doctor.excel_create, name="excel_create_doctor"),


#-----------------------payment-----------------------------
    path('Payment/', views.Payment, name="Payment"),

#------------------------show payment---------------------------------------
    path('show-payment/', views.show_payment, name="show_payment"),
    path('edit-payment/<int:pk>/', views.edit_payment, name="edit_payment"),
    path('delete-payment/<int:pk>/', views.delete_payment, name="delete_payment"),
    path('csvcreate-payment/', views.Transaction.csv_create, name="csv_create_payment"),
    path('excelcreate-payment/', views.Transaction.excel_create, name="excel_create_payment"),
    path("binomial_graph/", views.binomial_graph, name="binomial_graph"),
    path('payment-pdf/', views.getid, name = 'getid'),

#-------------------------Room--------------------------------------------------
    path('room/', views.room, name="room"),
#-------------------------show room----------------------------------------------------------- Room
    path('show-room/', views.show_room, name="show_room"),
    path('edit-room/<int:pk>/', views.edit_room, name="edit_room"),
    path('delete-room/<int:pk>/', views.delete_room, name="delete_room"),
    path('csvcreate-room/', views.PRoom.csv_create, name="csv_create_Room"),
    path('excelcreate-room/', views.PRoom.excel_create, name="excel_create_Room"),

#-----------------------------------------------------------------------------------------------

    path('Appointment/', views.appointment, name="Appointment"),
    path('show-appointment/', views.show_appointment, name="show_appointment"),
    path('edit-appointment/<int:pk>/', views.edit_appointment, name="edit_appointment"),
    path('delete-appointment/<int:pk>/', views.delete_appointment, name="delete_appointment"),



    path('csvcreate-apt/', views.PApointment.csv_create, name="csv_create_apointment"),
    path('excelcreate-apt/', views.PApointment.excel_create, name="excel_create_apointment"),




    path('h_form/', views.hospital_form , name = "user_form"),
    path('h_login/', views.hospital_login , name = "user_login"),
    path('logout/',views.logout_user , name = "user_logout"),


]
