# exec(open(r'D:\python_program\hospital\hospital_mangement\hospital\db_shell.py').read())
from hospital.models import Patient_Pay_Tran

payment = Patient_Pay_Tran.objects.all().value()
# print(payment.value())
# for i in payment:
#     print(i)
# print({'payment':payment})

payment = Patient_Pay_Tran.objects.filter(1)
print(payment)