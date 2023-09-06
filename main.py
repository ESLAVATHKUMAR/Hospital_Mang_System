from insert import inserted
from update import updated
from delete import delete
from read import read

obj=inserted()
obj1=updated()
obj2=delete()
obj3=read()


print('----------------- This is HMS Project ------------------')
 
print('** you can do 4 operations on database **')
print('for adding the data write add')
print('for update the data write update')
print('for delete the data write delete')
print('for read the data write read')




opr = input('enter any operation :')
if opr=='add':
    print('for inserting data in Appointments table please press -- 1: ')
    print('for inserting data in Billing table please press -- 2: ')
    print('for inserting data in doctors table please press-- 3: ')
    print('for inserting data in medications table please press-- 4: ')
    print('for inserting data in patients table please press-- 5: ')
    print('for inserting data in prescriptions table please press-- 6: ')

tab = int(input('please insert data in  table :'))

if tab==1:
    appointment_id = int(input('please enter appointment_id :'))
    patient_id = int(input('please enter patitent_id :'))
    doctor_id = int(input('please enter dotor_id :'))
    obj.apptinsert(appointment_id,patient_id,doctor_id)

if tab==2:
    bill_id= int(input('please enter bill_id :'))
    patient_id= int(input('please enter patient_id :'))
    total_amount= int(input('please enter totalamount :'))
    payment_status =input('please enter payment_status :')
    obj.billinsert(bill_id,patient_id,total_amount,payment_status)
    
if tab==3:
    doctor_id= int(input('please enter doctors_id :'))
    first_name= input('please enter firstname :')
    last_name= input('please enter lastname:')
    specialization=input('please enter specilization:')
    phone_number = int(input('please enter a phone_number : '))
    email = input('please enter a email')
    obj.doctorinsert(doctor_id,first_name,last_name,specialization,phone_number,email) 

if tab==4:
    Medication_ID= int(input('please enter Medication_ID :'))
    Medication_Name= input('please enter  Medication_Name :')
    Description= input('please enterDescription:')
    obj.medicationsinsert(Medication_ID,Medication_Name,Description) 

if tab==5:

    Patient_ID= int(input('please enter  Patient_ID :'))
    First_Name= input('please enter  First_Name:')
    Last_Name= input('please enterLast_Name :')
    Gender= input('please enter Gender:')
    Phone_Number= int(input('please enter Phone_Number'))
    Address= input('please enter Address:')
    Email= input('please enter Email:')
    Emergency_Contact= input('please enter Emergency_Contact:')
    obj.patientsinsert(Patient_ID,First_Name,Last_Name,Gender,Phone_Number,Address,Email,Emergency_Contact)    


    
if tab==6:
    Prescription_ID= int(input('please enter Prescription_ID :'))
    Patient_ID= int(input('please enter  Patient_ID :'))
    Doctor_ID= int(input('please enter  Doctor_ID :'))
    Medication_ID= int(input('please enter Medication_ID:'))
    Dosage= input('please enter Dosage:')
    Instructions= input('please enter Instructions:')
    obj.prescriptionsinsert(Prescription_ID,Patient_ID,Doctor_ID,Medication_ID,Dosage,Instructions)

   





# ------------------------update function---------------------------
if opr=='update':
    print('for update data in Appointments table please press -- 1: ')
    print('for update  data in Billing table please press -- 2: ')
    print('for update data in doctors table please press-- 3: ')
    print('for update data in medications table please press-- 4: ')
    print('for updatedata in patients table please press-- 5: ')
    print('for update data in prescriptions table please press-- 6: ')
    tab=int(input('please enter the number to update data in table'))
    if tab==1 :    
        columnname=input('please enter the columnname:')
        oldvalue=input('please enter the old value:')
        newvalue=input('please enter the new value: ')
        obj1.apptupdate(columnname,newvalue,oldvalue)

    if tab==2 :
        columnname=input('please enter the columnname : ')
        oldvalue=input('please enter the old value : ')
        newvalue=input('please enter the new value : ')
        obj1.billupdate(columnname,newvalue,oldvalue)

    if tab==3 :
        columnname=input('please enter the columnname : ')
        oldvalue=input('please enter the old value : ')
        newvalue=input('please enter the new value : ')
        obj1.doctorupdate(columnname,newvalue,oldvalue)

    if tab==4 :
        columnname=input('please enter the columnname : ')
        oldvalue=input('please enter the old value : ')
        newvalue=input('please enter the new value : ')
        obj1.medicationsupdate(columnname,newvalue,oldvalue)
    
    if tab==5 :
        columnname=input('please enter the columnname : ')
        oldvalue=input('please enter the old value : ')
        newvalue=input('please enter the new value : ')
        obj1.patientsupdate(columnname,newvalue,oldvalue)

    if tab==6 :
        columnname=input('please enter the columnname : ')
        oldvalue=input('please enter the old value : ')
        newvalue=input('please enter the new value : ')
        obj1.prescriptionsupdate(columnname,newvalue,oldvalue)







# ------------------------delete function---------------------------
if opr=='delete':
    print('for delete data in Appointments table please press -- 1: ')
    print('for delete data in Billing table please press -- 2: ')
    print('for delete data in doctors table please press-- 3: ')
    print('for delete data in medications table please press-- 4: ')
    print('for delete data in patients table please press-- 5: ')
    print('for delete data in prescriptions table please press-- 6: ')
    tab=int(input('please enter the number to  delete data in table'))
    if tab==1 :    
        columnname=input('please enter the columnname:')
        value=input('please enter the value:')
        obj2.apptdelete(columnname,value)

    if tab==2 :
        columnname=input('please enter the columnname : ')
        value=input('please enter the  value : ')
        obj2.billdelete(columnname,value)

    if tab==3 :
        columnname=input('please enter the columnname : ')
        value=input('please enter the  value : ')
        obj2.doctordelete(columnname,value)

    if tab==4 :
        columnname=input('please enter the columnname : ')
        value=input('please enter the value : ')
        obj2.medicationsdelete(columnname,value)
    
    if tab==5 :
        columnname=input('please enter the columnname : ')
        value=input('please enter the value : ')
        obj2.patientsdelete(columnname,value)

    if tab==6 :
        columnname=input('please enter the columnname : ')
        value=input('please enter the  value : ')
        obj2.prescriptionsdelete(columnname,value)





# ------------------------read  function---------------------------
if opr=='read':
    print('please  enter the press 1 : ')
    print('please  enter the press 2 : ')
    print('please  enter the press 3 : ')
    print('please  enter the press 4 : ')
    print('please  enter the press 5 : ')
    print('please  enter the press 6 : ')



    tab=int(input('please enter the number to read the data : '))
    if tab==1:
        obj3.apptread()

    if tab==2:
        obj3.billread()
    
    if tab==3:
        obj3.doctorread()

    if tab==4:
        obj3.medicationsread()
    
    if tab==5:
        obj3.patientsread()
    
    if tab==6:
        obj3.prescriptionsread()
