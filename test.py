# import cx_Oracle
# from flask import jsonify 
# from models.doctor import Doctor
# from utils.dbconn import connection
# from utils.db_helper import get_dictformat, get_listformat

# import datetime

# host_name = 'localhost'
# port_number = 1521
# service_name = 'doc_consult_db'

# user = 'admin_user'
# pcode = 'Admin$12345'

# connection = None

# def get_data():
#     try:
        
#         data = []

#         with connection.cursor() as cur:
        
#             cur.execute('select * from doctor')
#             # for col, description in enumerate(cur):
#             records = cur.fetchall()
#             if len(records) == 0:
#                 print('No results')
#             for row in records:
        
#                 obj = Doctor(*list(row))
#                 data.append(obj.data)
                
#             print(data)


#     except Exception as ex:
#         print("Message : {0}".format(ex))


#         # data = {
#         #     'first_name': 'fist_kapriri',
#         #     'last_name': 'lst_kap',
#         #     'mobile_number': 723567894,
#         #     'email_address': 'kaprii@gamil.com',
#         #     'specialization': 'nothing',
#         #     'qualification': 'Jobless',
#         #     'resid_address': 'colombo',
#         #     'username': 'kapiri'
#         # }

#         # doctor = Doctor( 0,'fist_kapriri','lst_kap',723567894,'kaprii@gamil.com','nothing','Jobless','colombo','kapiri')
#         # data = doctor.data
#         #  """
#         #     DECLARE
#         #         new_id doctor.doctor_id%TYPE
#         #     BEGIN
                
                
#         #         INSERT INTO doctor (first_name, last_name, mobile_number, email_address, specialization, qualification, resid_address, username) 
#         #         VALUES 
#         #         ( 'test2_fname', 'test2_lname', 745689878, 'test2@gmail.com', 'test2_spec', 'test2_qual', 'NONE', 'kapiri')
#         #         RETURNING doctor_id INTO :doctor_id;
#         #         COMMIT;
#         #     END;

#         #     """

#         # qeury = """
#         #     BEGIN
#         #         INSERT INTO doctor (first_name, last_name, mobile_number, email_address, specialization, qualification, resid_address, username) 
#         #         VALUES 
#         #         ( :first_name, :last_name, :mobile_number, :email_address, :specialization, :qualification, :resid_address, :username)
#         #         RETURNING doctor_id INTO :doctor_id;
#         #         COMMIT;
#         #     END;
        
#         # """

# def procedure_test():

#     doctor = None
#     with connection.cursor() as cur:
#         cur.execute('read_doctor_by_id',[2])
#         records = cur.fetchall()

#         if len(records) == 0:   print("No DATA FOUND")
#         else:   print(list(*records))        
#         for row in records:
#             print(row[0])
#             doctor = Doctor(*list(row))

#     connection.close()

#     # print(doctor.data)        

# def insert_data(doctor_id):
    
#     try:
        
#         doctor = None
#         with connection.cursor() as cur:
#             cur.execute('select * from doctor where doctor_id = :id', {'id' : doctor_id})
#             records = cur.fetchone()
#             if records is None:
#                 print('Not rec')   
            
#             doctor = Doctor(*records)

        
#         print(doctor.data)
   
#     except Exception as ex:
#         print("Message : {0}".format(ex))

# def function_test(doctor_id):
    
#     currentDT = datetime.datetime.now()
    
#     consult = {
#             'consult_date' : currentDT.strftime("%Y-%m-%d"),
#             'consult_time' : currentDT.strftime("%H:%M:%S"),
#             'status' : 'pending',
#             'receptionist_id' : 1,
#             'doctor_id': 2
#         }
#     with connection.cursor() as cur:
#         # cur.callproc("doctor_pkg.read_doctor_id", [doctor_id,])
#         cur.callfunc("consultdatetime_pkg.write_consulttimedate",int,consult)

#         d = get_listformat(cur)
#         if d:
#             [d] = d
#             print(*d)

    

#         # if len(records) == 0:   print("No DATA FOUND")
#         # else:   print(list(*records))        
#         # for row in records:
#         #     print(row[0])
#         #     doctor = Doctor(*list(row))

#     connection.close()
from flask import request 
from flask_restful import Resource
from http import HTTPStatus

from utils.dbconn import connection
from predict_model.disease_list import DISEASE_LIST

import numpy as np 
import pandas as pd
import pickle


def test():
    
    model = pickle.load(open("predict_model\model.pkl", 'rb'))
    # model.predict(x_train[:1])


    # data = request.get_json()
    data = {
            "symptom1": "agitation",
            "symptom2": "cardiovascular event",
            "symptom3": "cardiovascular finding",
            "symptom4": "cough",
            "symptom5": "dyspnea",
            "symptom6": "haemoptysis",
            "symptom7": "hypercapnia",
            "symptom8": "prostatism",
            "symptom9": "soft tissue swelling"
        }
    symptoms = [ data[sym] for sym in data ]

    symptom_record = np.zeros(len(DISEASE_LIST))
    for symptom in symptoms:
        if symptom in DISEASE_LIST:
            ind = DISEASE_LIST.index(symptom)
            symptom_record[ind] = 1
    symptom_record = [list(symptom_record)]
    data_record = pd.DataFrame(list(symptom_record), columns=DISEASE_LIST)
    m = model.predict(data_record)
    print(list(m))

if __name__ == "__main__":
    test()