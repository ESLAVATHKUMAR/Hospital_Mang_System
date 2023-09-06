import mysql.connector
conn = mysql.connector.connect(
    host = 'localhost',
    database='hospital_management_system',
    user='root',
    password='Kumar@9948'
)
cur=conn.cursor()
class delete:
    def apptdelete(x,columnname,value):
        cur.execute(f"delete from appointments where {columnname}='{value}'")
        conn.commit()
        print("Data entered successfully")

    def billdelete(x,columnname,value):
        cur.execute(f"delete from Billing where {columnname}='{value}'")
        conn.commit()
    print("Data entered successfully")


    def doctordelete(x,columnname,value):
        cur.execute(f"delete from doctors where {columnname}='{value}'")
        conn.commit()
    print("Data entered successfully")


    def medicationsdelete(x,columnname,value):
        cur.execute(f"delete from medications where {columnname}='{value}'")
        conn.commit()
        print("Data entered successfully")

    def patientsdelete(x,columnname,value):
        cur.execute(f"delete from patients where {columnname}='{value}'")
        conn.commit()
        print("Data entered successfully")

    def prescriptionsdelete(x,columnname,value):
        cur.execute(f"delete from prescriptions where {columnname}='{value}'")
        conn.commit()
        print("Data entered successfully")