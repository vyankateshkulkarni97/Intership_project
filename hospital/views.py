from django.shortcuts import render , redirect ,HttpResponse
from abc import ABC , abstractmethod
import xlwt
# Create your views here.
from .models import Patients , Doctors , Patient_Pay_Tran , Room , Appointment
#-----------------------------------------------------------------------------------------------
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .form import Hospital_user
#--------------------------------------------------------------------------------------------------

import random
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import csv
#------------------------------------------------------------------------------------
from reportlab.pdfgen import canvas  
from django.http import FileResponse
import io  
#-------------------------------------------------------------------------------------------

# -------------------- Main Page---------------------------------------
@login_required
def BASE(request):
    return render(request, 'base.html')  # , {"Appoints":Appointment.objects.all()}

# def Dashboard(request):
#     return render(request, "Dashboard.html")

#------------------------------------------------------------------------------
class File(ABC):

    @abstractmethod
    def csv_create(self, *args):
        pass

    @abstractmethod
    def excel_create(self, *args):
        pass


# -------------------- Patients information add on database---------------------------------------
@login_required
def home(request):
    # print(request.method)
    if request.method =="POST":
        data = request.POST
        Pid = data.get("id")
        name = data.get("name")  
        age = data.get("age") 
        phone = data.get("phone")
        date_of_birth = data.get("date_of_birth")
        last_visit = data.get("last_visit")
        gender = data.get("gender")
        email = data.get("email")
        address = data.get("address")
        status = data.get("status")
        if not Pid:
            Patients.objects.create(Name = name ,Age = age , Phone = phone , Date_of_birth = date_of_birth , Last_visit = last_visit ,  Gender = gender , Email = email , Address = address , Status = status)
        else:
            patients = Patients.objects.get(id=Pid)
            patients.Name = name
            patients.Age = age
            patients.Phone = phone
            patients.Date_of_birth = date_of_birth
            patients.Last_visit = last_visit
            patients.Gender = gender
            patients.Email = email
            patients.Address = address 
            patients.Status = status
            patients.save()
        return redirect("home_page")

    elif request.method == "GET":
        return render (request ,"home.html" , context={"person":"vyankatesh"})
            

    return render(request, "home.html")

# -------------------- Show all Patients---------------------------------------
def show_patients(request):
    return render(request, "show_patients.html", {"patient": Patients.objects.all()})

#-------------------Edit Patients --------------------------------------------

def edit_patients(request , pk):
    patients = Patients.objects.get(id = pk)
    return render(request,"home.html", context={"edit_patient":patients})

# ---------------------- Delete Patients --------------------------------------
def delete_patients(request , pk):
    Patients.objects.get(id=pk).delete()
    return redirect("show_patients")


class P_details(File):

    def csv_create(request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="patient.csv"'
        writer = csv.writer(response)
        writer.writerow(['name','age', 'phone', 'date_of_birth', 'last_visit', 'gender', 'email', 'address', 'status' ])

        patients = Patients.objects.all().values_list('Name', 'Age', 'Phone', 'Date_of_birth', 'Last_visit', 'Gender', 'Email', 'Address', 'Status')
        for pt in patients:  # he Patients use kela hota ithe -- ata apan pt use krtoy
            writer.writerow(pt)
        return response

    def excel_create(request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="Patient_details.xls"'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Patient Data') # this will make a sheet named Book Data

        row_num = 0
        columns = ['name','age', 'phone', 'date_of_birth', 'last_visit', 'gender', 'email', 'address', 'status' ]
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num]) 
        rows = Patients.objects.all().values_list('Name', 'Age', 'Phone', 'Date_of_birth', 'Last_visit', 'Gender', 'Email', 'Address', 'Status')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num])
        wb.save(response)
        return response



#-------------------------------------------------------------------------------------------------------------
#----------------- Doctors --------------------------------------------- 
@login_required
def doctors(request):
    if request.method == "POST":
        data = request.POST
        Drid = data.get("id")
        name = data.get("name")
        age = data.get("age")
        experience = data.get("experience")
        phone = data.get("phone")
        email = data.get("email")
        gender = data.get("gender")
        specialization = data.get("specialization")
        availability = data.get("availability")
        visit_date = data.get("visit_date")
        problem = data.get("problem")  
        if not Drid:
            Doctors.objects.create(Doctors_N =name, Doctors_Age=age, Experience=experience, Phone=phone, Email=email, Gender=gender, Specialization=specialization, Availability=availability, Visit_date=visit_date, Problem=problem)
        else:
            doctor_s = Doctors.objects.get(id=Drid)
            doctor_s.Doctors_N = name
            doctor_s.Doctors_Age= age
            doctor_s.Experience = experience
            doctor_s.Phone = phone
            doctor_s.Email = email
            doctor_s.Gender = gender
            doctor_s.Specialization = specialization
            doctor_s.Availability = availability
            doctor_s.Visit_date = visit_date
            doctor_s.Problem = problem
            doctor_s.save()
        return redirect( "Add_Doctor")
    
    elif request.method == "GET":
        return render(request, "doctor.html", context={"person":"vyankatesh"})
    
    return render(request, "doctor.html")


def doctor_details(request):
    return render(request, "show_doctor.html",  {"Doctor": Doctors.objects.all()})

def edit_doctor(request , pk):
    doctor_s = Doctors.objects.get(id = pk)
    return render(request,"doctor.html", context={"doctors":doctor_s})

def delete_doctors(request , pk):
    Doctors.objects.get(id=pk).delete()
    return redirect("all_doctor")


class Doctor(File):

    def csv_create(request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Doctor.csv"'
        writer = csv.writer(response)
        
        writer.writerow(['Doctors_N', 'Doctors_Age', 'Experience', 'Phone', 'Email', 'Gender', 'Specialization', 'Availability', 'Visit_date', 'Problem' ])
        doctor = Doctors.objects.all().values_list('Doctors_N', 'Doctors_Age', 'Experience', 'Phone', 'Email', 'Gender', 'Specialization', 'Availability', 'Visit_date', 'Problem')
        for dr in doctor: 
            writer.writerow(dr)
        return response

    def excel_create(request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="Doctor_details.xls"'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Doctor Data') # this will make a sheet named Book Data

        row_num = 0
        columns = ['Doctor_Name', 'Doctor_Age', 'Experience', 'Phone', 'Email', 'Gender', 'Specialization', 'Available', 'Visit_date', 'Problem']
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num]) 
        rows = Doctors.objects.all().values_list('Doctors_N', 'Doctors_Age', 'Experience', 'Phone', 'Email', 'Gender', 'Specialization', 'Availability', 'Visit_date', 'Problem')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num])
        wb.save(response)
        return response



#-------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
@login_required
def Payment(request): # Service_Name  Date Cost Payment_type  Payment_Status
    if request.method == "POST":
        data = request.POST
        pay_id = data.get("id")
        service = data.get("service")
        s_date = data.get("s_date")
        cost = data.get("cost")
        payment_type = data.get("payment_type")
        pay_status = data.get("pay_status")
        if not pay_id:
            Patient_Pay_Tran.objects.create(Service_Name=service,  Date=s_date, Cost=cost, Payment_type=payment_type,  Payment_Status=pay_status)
        else:
            pay = Patient_Pay_Tran.objects.get(id = pay_id)
            pay.Service_Name = service
            pay.Date = s_date
            pay.Cost = cost
            pay.Payment_type=payment_type  
            pay.Payment_Status=pay_status
            pay.save()
        return render(request, "payment.html")
    elif request.method == "GET":
        return render (request ,"payment.html" , context={"person":"vyankatesh"})
#---------------------------show payment---------------------------------------------
def show_payment(request):
    return render(request, "show_payment.html", {"payment":Patient_Pay_Tran.objects.all()})

def edit_payment(request, pk):
    pay = Patient_Pay_Tran.objects.get(id=pk)
    return render(request, "payment.html", {"payments": pay})

def delete_payment(request , pk):
    Patient_Pay_Tran.objects.get(id=pk).delete()
    return redirect("show_payment")


from numpy import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

def binomial_graph(request):
    pay = Patient_Pay_Tran.objects.all().values_list("Cost", flat=True)
    print(pay)
    if pay:
        n = len(pay)
        x = np.arange(0, max(pay) + 1)
        pmf = binom.pmf(x, n, np.mean(pay) / max(pay))

        plt.bar(x, pmf)
        plt.xlabel("X")
        plt.ylabel("Probability")
        plt.title("Binomial Distribution")
        plt.grid(True)

        plt.savefig("binomial_graph.png")
        plt.close()
        return render(request,"binomial_graph.html")
    else:
        return render(request, "binomial_graph.html", {"error_message": "No data available."})

class Transaction(File):

    def csv_create(request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Payment_info.csv"'
        writer = csv.writer(response)
        writer.writerow(['Service_Name', 'Date', 'Cost', 'type', 'Status'])

        payment = Patient_Pay_Tran.objects.all().values_list('Service_Name', 'Date', 'Cost', 'Payment_type', 'Payment_Status')
        for pay in payment: 
            writer.writerow(pay)
        return response

    def excel_create(request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="Payment_details.xls"'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Payment Data') # this will make a sheet named Book Data

        row_num = 0
        columns = ['Service_Name', 'Date', 'Cost', 'type', 'Status']
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num]) 
        rows = Patient_Pay_Tran.objects.all().values_list('Service_Name', 'Date', 'Cost', 'Payment_type', 'Payment_Status')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num])
        wb.save(response)
        return response
#------------------------------------------------------------------------------------------------

def getid(request):
    if request.method == "POST":
        data = request.POST
        Pdid = data.get('id')
        return Pdid
    return render(request, "pay_pdf.html")

def payment(request):
    return render(request, "show_payment.html", {"payment":Patient_Pay_Tran.objects.filter(getid(request))})

def getpdf(request):
    if request.method == "POST":
        data = request.POST
        Pdid = data.get('id')


    # return render(request, "pay_pdf.html")



#--------------------------------------------------------------------------------------------------------------
#---------------------------------Room-----------------------------------------------------------------------
@login_required
def room(request):#  Room_No Room_Type Alt_dt Dis_dt Room_Status
    if request.method == "POST":
        data = request.POST
        rid = data.get("id")
        room_no = data.get("room_no") 
        room_type = data.get("room_type")
        alt_dt = data.get("alt_dt")
        dis_dt = data.get("dis_dt")
        r_status = data.get("r_status")
        if not rid:
            Room.objects.create(Room_No=room_no, Room_Type=room_type, Alt_dt=alt_dt, Dis_dt=dis_dt, Room_Status=r_status)
        else:
           room_p = Room.objects.get(id=rid)
           room_p.Room_No = room_no
           room_p.Room_Type = room_type
           room_p.Alt_dt = alt_dt
           room_p.Dis_dt = dis_dt
           room_p.Room_Status = r_status
           room_p.save()
        return render(request, "room.html")
    elif request.method == "GET":
        return render (request ,"room.html" , context={"person":"vyankatesh"})

#-----------------------------show Room ------------------------------------                       
def show_room(request):
    return render(request, "show_room.html", {"room":Room.objects.all()})

def edit_room(request,pk):
    room_p = Room.objects.get(id=pk)
    return render(request, "room.html", {"Rooms_p":room_p})

def delete_room(request,pk):
    Room.objects.get(id=pk).delete()
    return redirect("show_room")


class PRoom(File):

    def csv_create(request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Room_info.csv"'
        writer = csv.writer(response)
        writer.writerow(['Room_No', 'Room_Type', 'Alt_dt', 'Dis_dt', 'Room_Status'])

        room = Room.objects.all().values_list('Room_No', 'Room_Type', 'Alt_dt', 'Dis_dt', 'Room_Status')
        for Rooms in room: 
            writer.writerow(Rooms)
        return response

    def excel_create(request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="Room_details.xls"'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Room Data') # this will make a sheet named Room Data

        row_num = 0
        columns = ['Room_No', 'Room_Type', 'Alt_dt', 'Dis_dt', 'Room_Status']
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num]) 
        rows = Room.objects.all().values_list('Room_No', 'Room_Type', 'Alt_dt', 'Dis_dt', 'Room_Status')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num])
        wb.save(response)
        return response


#-------------------------------------------------------------------------------------------------

def number():
    for i in range(1 , random.randrange(100)):
        num = i
    return num

@login_required
def appointment(request): # Appointment
    if request.method =="POST":
        data = request.POST
        apt_id = data.get("id")
        dr_name = data.get("dr_name")
        dr_dept = data.get("dep_name")
        Name = data.get("p_name")
        Apoint_date = data.get("apoint_date")
        time_slot = data.get("time_slot")
        token = number()
        problem = data.get("problem")
        if not apt_id:
            Appointment.objects.create(Dr_name=dr_name , Dr_dep=dr_dept, Cust_name=Name ,Apptment_Date = Apoint_date , Time_slot = time_slot , Token = token, Problem = problem)
        else:
            apt = Appointment.objects.get(id=apt_id)
            apt.Dr_name=dr_name
            apt.Dr_dep=dr_dept
            apt.Cust_name=Name
            apt.Apptment_Date = Apoint_date
            apt.Time_slot = time_slot
            apt.Problem = problem
            apt.save()

        return render(request, "appointment.html")
    elif request.method == "GET":
        return render (request ,"appointment.html" , context={"person":"vyankatesh"})

def show_appointment(request):
    return render (request , "show_appointment.html", {"appoints":Appointment.objects.all()})

def edit_appointment(request, pk):
    apt = Appointment.objects.get(id=pk)
    return render(request, "appointment.html", {"appoints":apt})

def delete_appointment(request, pk):
    Appointment.objects.get(id=pk).delete()
    return redirect("show_appointment")

class PApointment(File):

    def csv_create(request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Appointment_info.csv"'
        writer = csv.writer(response)
        writer.writerow(['Dr_name', 'Dr_dep', 'Cust_name', 'Apptment_Date', 'Time_slot', 'Token', 'Problem'])

        booked = Appointment.objects.all().values_list('Dr_name', 'Dr_dep', 'Cust_name', 'Apptment_Date', 'Time_slot', 'Token', 'Problem')
        for apt in booked: 
            writer.writerow(apt)
        return response

    def excel_create(request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="Appointment_details.xls"'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Appointment Data') # this will make a sheet named Room Data

        row_num = 0
        columns = ['Dr_name', 'Dr_dep', 'Cust_name', 'Apptment_Date', 'Time_slot', 'Token', 'Problem']
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num]) 
        rows = Appointment.objects.all().values_list('Dr_name', 'Dr_dep', 'Cust_name', 'Apptment_Date', 'Time_slot', 'Token', 'Problem')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num])
        wb.save(response)
        return response


# patient name  -- @  # name gheut
# Doctor name -- @ Doctors.objects.filter(Name=Ture)
# Department  -- @ Doctors.objects.filter(Department)
# Appointment date 
# time slot
# Token no.  -- autogenerate
# Problem   -- @



#------------------------------------ login requried -----------------------------------------------------------
def hospital_form(request):
    if request.method == "POST":
        form = Hospital_user(request.POST)
        if form.is_valid():
            user = form.save()
            login(request , user)
            return redirect("user_login")
    form = Hospital_user()
    return render (request=request , template_name="h_form.html",context={"Admin_form":form} )

#------------------------------------- create login --------------------------------------------------------
def hospital_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request , data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username , password=password)
            if user is not None:
                login(request , user)
                return redirect("BASE")
            else:
                return redirect("user_login")
        else:
            return redirect("BASE")
    form = AuthenticationForm()
    return render(request=request , template_name="h_login.html", context={"Admin_login":form})

# ---------------------------------------------- logut --------------------------------------------------------

def logout_user(request):
    logout(request)
    return redirect("user_login") 