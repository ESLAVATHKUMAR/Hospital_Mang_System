import mysql.connector
conn = mysql.connector.connect(
    host = 'localhost',
    database='hospital_management_system',
    user='root',
    password='Kumar@9948'
)
cur=conn.cursor()
   
class updated:

    def apptupdate(x, colname, newval, oldval):
        cur.execute(f"UPDATE appointments SET {colname} = '{newval}' WHERE {colname} = '{oldval}'")
        conn.commit()
        print('The data has been successfully updated ')

    def billupdate(x, colname, newval, oldval):
        cur.execute(f"UPDATE billing SET {colname} = '{newval}' WHERE {colname} = '{oldval}'")
        conn.commit()
        print('The data has been successfully updated ')

    def doctorupdate(x, colname, newval, oldval):
        cur.execute(f"UPDATE doctors SET {colname} = '{newval}' WHERE {colname} = '{oldval}'")
        conn.commit()
        print('The data has been successfully updated ')

    def medicationsupdate(x, colname, newval, oldval):
        cur.execute(f"UPDATE medications SET {colname} = '{newval}' WHERE {colname} = '{oldval}'")
        conn.commit()
        print('The data has been successfully updated ')

    def patientsupdate(x, colname, newval, oldval):
        cur.execute(f"UPDATE patients SET {colname} = '{newval}' WHERE {colname} = '{oldval}'")
        conn.commit()
        print('The data has been successfully updated ')

    def prescriptionsupdate(x, colname, newval, oldval):
        cur.execute(f"UPDATE prescriptions SET {colname} = '{newval}' WHERE {colname} = '{oldval}'")
        conn.commit()
        print('The data has been successfully updated ')

     

    
    





