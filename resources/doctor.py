from flask import request 
from flask_restful import Resource
from http import HTTPStatus

from utils.dbconn import connection

from models.doctor import Doctor 




class DoctorListResource( Resource ):

    def get(self):
        
        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        data =[]
        
        with connection.cursor() as cur:
            cur.execute('select * from doctor')
            records = cur.fetchall()

            if len(records) == 0:   return {'message':"Not Found"}, HTTPStatus.NOT_FOUND
            
            for row in records:
                doctor = Doctor(*list(row))
                data.append(doctor.data)

        connection.close()
        
        return {'data': data }, HTTPStatus.OK

    def post(self):

        data = request.get_json()

        doctor = Doctor(
            data['first_name'],
            data['last_name'],
            data['mobile_number'],
            data['email_address'],
            data['specialization'],
            data['qualification'],
            data['resid_address'],
            data['username']
            )
        sql_query = """INSERT INTO doctor values 
        (:doctor_id, :first_name, :last_name, :mobile_number, :email_address, :specialization, :qualification, :resid_address, :username)"""

        del data['doctor_id']
        print(data)

        with connection.cursor() as cur:
            cur.execute("""INSERT INTO doctor (first_name, last_name, mobile_number, email_address, specialization, qualification, resid_address, username) 
            VALUES 
            ( :first_name, :last_name, :mobile_number, :email_address, :specialization, :qualification, :resid_address, :username)""", data)
            connection.commit()

        