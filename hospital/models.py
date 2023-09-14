from django.db import models

# Create your models here.  Name, Age, Phone, Date_of_birth, Last_visit, Gender, Email, Address, Status
class Patients(models.Model):
    Name = models.CharField(max_length=200, null=True)
    Age = models.IntegerField()
    Phone = models.IntegerField()
    Date_of_birth = models.DateField(max_length=200, null=True)
    Last_visit = models.CharField(max_length=200, null=True)
    Gender = models.CharField(max_length=200, null=True)
    Email = models.CharField(max_length=200, null=True)
    Address = models.CharField(max_length=200, null=True)
    Status = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.Name}, {self.Age}, {self.Phone}, {self.Date_of_birth}, {self.Last_visit}, {self.Gender} "

    class Meta:
        db_table = "patients"


# ----------Doctors Information and Doctors Visit--------------------------------------
# Patient visit
#  department
#  visit date
#  Problem  'Doctors_N', 'Doctors_Age', 'Experience', 'Phone', 'Email', 'Gender', 'Specialization', 'Availability', 'Visit_date', 'Problem',
class Doctors(models.Model):
    Doctors_N = models.CharField(max_length=200)
    Doctors_Age = models.IntegerField()
    Experience = models.IntegerField()
    Phone = models.IntegerField()
    Email = models.CharField(max_length=200)
    Gender = models.CharField(max_length=100)
    Specialization = models.CharField(max_length=200)
    Availability = models.CharField(max_length=100)
    Visit_date = models.DateField()
    Problem = models.CharField(max_length=200 )
  
    def __str__(self):
        return f"{self.Doctors_N}"

    class Meta:
        db_table = "Doctors"




# ------------Patient Payment Transaction--------------------------------
# class Patient Payment Transaction
# service name
# date
# cost
# PaymentType
# Invoice --  @ @ @
# Status ---  # # # 'Service_Name', 'Date', 'Cost', 'Payment_type', 'Payment_Status'
class Patient_Pay_Tran(models.Model): # patient payment_ trans
    Service_Name = models.CharField(max_length=200)
    Date = models.DateField(null=True)
    Cost = models.FloatField()
    Payment_type = models.CharField(max_length=200)
    Payment_Status = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.Service_Name}"

    class Meta:
        db_table = "Payment"




# ----------------- Room All Information -----------------------------------------------
# class Room_Allotment
# Patient name
# room no
# Room type
# Allotment date
# Discharge date
# Doctor name
# status  'Room_No', 'Room_Type', 'Alt_dt', 'Dis_dt', 'Room_Status'
class Room(models.Model): #  Room_No Room_Type Alt_dt Dis_dt Room_Status
    Room_No = models.IntegerField()
    Room_Type = models.CharField(max_length=200)
    Alt_dt = models.DateField()
    Dis_dt = models.DateField()
    Room_Status = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.Room_No}"
    
    class Meta:
        db_table = "Room"



# ----------------------------- Patient Appointment -------------------------------------------
# class Add_appointment
# patient id  -- @  # name gheut  
# Doctor name -- @ Doctors.objects.filter(Name=Ture)
# Department  -- @ Doctors.objects.filter(Department)
# Appointment date 
# time slot
# Token no.  -- autogenerate
# Problem   -- @ Dr_name Dr_dep Cust_name 'Dr_name', 'Dr_dep', 'Cust_name', 'Apptment_Date', 'Time_slot', 'Token', 'Problem' 
class Appointment(models.Model):
    Dr_name = models.CharField(max_length=200)
    Dr_dep = models.CharField(max_length=200)
    Cust_name = models.CharField(max_length=200)
    Apptment_Date = models.DateField()
    Time_slot = models.TimeField()
    Token = models.IntegerField(null=True, blank=True)
    Problem = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.Cust_name}"
    class Meta:
        db_table = "Appointment"