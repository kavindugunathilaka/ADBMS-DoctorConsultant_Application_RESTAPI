import cx_Oracle
from flask import jsonify 

from models.doctor import Doctor
from utils.dbconn import connection


# host_name = 'localhost'
# port_number = 1521
# service_name = 'doc_consult_db'

# user = 'admin_user'
# pcode = 'Admin$12345'

# connection = None

def get_data():
    try:
        
        data = []

        with connection.cursor() as cur:
        
            cur.execute('select * from doctor')
            # for col, description in enumerate(cur):
            records = cur.fetchall()
            if len(records) == 0:
                print('No results')
            for row in records:
        
                obj = Doctor(*list(row))
                data.append(obj.data)
                
            print(data)


    except Exception as ex:
        print("Message : {0}".format(ex))

def insert_data():
    
    try:
        
        # data = {
        #     'first_name': 'fist_kapriri',
        #     'last_name': 'lst_kap',
        #     'mobile_number': 723567894,
        #     'email_address': 'kaprii@gamil.com',
        #     'specialization': 'nothing',
        #     'qualification': 'Jobless',
        #     'resid_address': 'colombo',
        #     'username': 'kapiri'
        # }

        doctor = Doctor( 0,'fist_kapriri','lst_kap',723567894,'kaprii@gamil.com','nothing','Jobless','colombo','kapiri')
        data = doctor.data
        del data['doctor_id']
        print(data)
        sql_query = """INSERT INTO doctor (first_name, last_name, mobile_number, email_address, specialization, qualification, resid_address, username) 
            VALUES 
            ( :first_name, :last_name, :mobile_number, :email_address, :specialization, :qualification, :resid_address, :username)"""

        with connection.cursor() as cur:
            cur.execute("""INSERT INTO doctor (first_name, last_name, mobile_number, email_address, specialization, qualification, resid_address, username) 
            VALUES 
            ( :first_name, :last_name, :mobile_number, :email_address, :specialization, :qualification, :resid_address, :username)""", data)
            connection.commit()
            # records = cur.fetchall()
            
            # print(records)
                

    except Exception as ex:
        print("Message : {0}".format(ex))

if __name__ == "__main__":
    
    insert_data()
