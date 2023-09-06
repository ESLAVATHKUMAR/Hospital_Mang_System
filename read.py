import mysql.connector
conn = mysql.connector.connect(
    host = 'localhost',
    database='hospital_management_system',
    user='root',
    password='Kumar@9948'
)

cur=conn.cursor()

class read:

    def apptread(x):
        cur.execute('select * from  appointments')
        print(cur.fetchall())

    def billread(x):
        cur.execute('select * from billing')
        print(cur.fetchall())
    
    def doctorread(x):
        cur.execute('select * from doctors')
        print(cur.fetchall())

    def medicationsread(x):
        cur.execute('select * from medications')
        print(cur.fetchall())

    def patientsread(x):
        cur.execute('select * from patients')
        print(cur.fetchall())

    def prescriptionsread(x):
        cur.execute('select * from prescriptions')
        print(cur.fetchall())