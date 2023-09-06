import mysql.connector
conn = mysql.connector.connect(
    host = 'localhost',
    database='hospital_management_system',
    user='root',
    password='Kumar@9948'
)

cur = conn.cursor()

class inserted:

    def apptinsert(x,appointment_id,patient_id,doctor_id):
        cur.execute(f"insert into  appointments values({ appointment_id},{patient_id},{doctor_id})")
        conn.commit()
        print('The data has sucessfully inserted')


    def billinsert(x,bill_id,patient_id,total_amount,payment_status):
        cur.execute(f"insert into billing values ({bill_id},{patient_id},{total_amount},{payment_status})")
        conn.commit()
        print('The data has sucessfully inserted ')


    def doctorinsert(x,doctor_id,first_name,last_name,specialization,phone_number,email):
        cur.execute(f"insert into doctors values({doctor_id},{first_name},{last_name},{specialization},{phone_number},{email})")
        conn.commit()
        print('The data has sucessfully inserted ')


    def medicationsinsert(x,Medication_ID,Medication_Name,Description):
        cur.execute(f"insert into medications  values({Medication_ID},{Medication_Name},{Description })")
        conn.commit()
        print('The data has sucessfully inserted ')
  

    def patientsinsert(x,Patient_ID,First_Name,Last_Name,Gender,Phone_number,Adress,Email,Emergency_Contact):
        cur.execute(f"insert into patients values ({Patient_ID},{First_Name},{Last_Name},{Gender},{Phone_number},{Adress},{Email},{Emergency_Contact})")
        conn.commit()
        print('The data has sucessfully inserted ')


    def prescriptionsinsert(x,prescription_ID,Patient_ID,Doctor_ID,Medication_ID,Dosage,Instructions):
        cur.execute(f"insert into  prescriptions values({prescription_ID},{Patient_ID},{Doctor_ID},{Medication_ID},{Dosage},{Instructions}) ")
        conn.commit()
        print('The  data has sucessfully inserted ')

 


        
