from flask import request 
from flask_restful import Resource
from http import HTTPStatus

from utils.dbconn import connection
from utils.db_helper import get_dictformat, get_listformat

from models.doctor import Doctor 

import cx_Oracle



class DoctorListResource( Resource ):

    def get(self):
        
        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        data =[]
        
        with connection.cursor() as cur:
            cur.execute('select * from doctor')
            records = cur.fetchall()

            if len(records) == 0:   

                return {'message':"Not Found"}, HTTPStatus.NOT_FOUND
            
            for row in records:
                doctor = Doctor(*list(row))
                data.append(doctor.data)

        
        return {'data': data }, HTTPStatus.OK

    def post(self):

        if connection is None:  return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE

        data = request.get_json()
        if data is None:    return {'message' : 'No Data'}, HTTPStatus.BAD_REQUEST
        # doctor = Doctor(
        #     data['first_name'],
        #     data['last_name'],
        #     data['mobile_number'],
        #     data['email_address'],
        #     data['specialization'],
        #     data['qualification'],
        #     data['resid_address'],
        #     data['username']
        #     )

        sql_query = """
            BEGIN
                INSERT INTO doctor (first_name, last_name, mobile_number, email_address, specialization, qualification, resid_address, username) 
                VALUES 
                ( :first_name, :last_name, :mobile_number, :email_address, :specialization, :qualification, :resid_address, :username)
                RETURNING doctor_id INTO :doctor_id;
                COMMIT;
            END;
            """

        with connection.cursor() as cur:
            data['doctor_id'] = cur.var(cx_Oracle.NUMBER)
            cur.execute(sql_query, data )
            data['doctor_id'] = int(data['doctor_id'].getvalue())
        
        return {'data': data }, HTTPStatus.OK


class DoctorResource( Resource ):

    def get(self, doctor_id):
        
        doctor = None
        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        data =[]
        
        with connection.cursor() as cur:
            # cur.execute('select * from doctor where doctor_id = :id',{'id':doctor_id})
            cur.callproc("doctor_pkg.read_doctor_id", [doctor_id,])

            record = get_listformat(cur)

            if record is None:
                return {'message':"Not Found"}, HTTPStatus.NOT_FOUND
            else:
                [record] = record
                doctor = Doctor(*record)

        return {'data': doctor.data }, HTTPStatus.OK
        
    # def put(self, doctor_id):

        # data = request.get_json()
        
        # doctor = Doctor(
        #     data['first_name'],
        #     data['last_name'],
        #     data['mobile_number'],
        #     data['email_address'],
        #     data['specialization'],
        #     data['qualification'],
        #     data['resid_address'],
        #     data['username']
        #     )
        # update_list = [k for k,v in doctor.data if v == '']

        

        # update_query = """
        #     BEGIN
        #         UPDATE doctor SET


        #         INSERT INTO doctor (first_name, last_name, mobile_number, email_address, specialization, qualification, resid_address, username) 
        #         VALUES 
        #         ( :first_name, :last_name, :mobile_number, :email_address, :specialization, :qualification, :resid_address, :username)
        #         RETURNING doctor_id INTO :doctor_id;
        #         COMMIT;
        #     END;
        #     """



    def delete(self, doctor_id):

        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        with connection.cursor() as cur:
            if cur.execute('DELETE FROM doctor WHERE doctor_id = :id',{'id':doctor_id}):
                return {}, HTTPStatus.NO_CONTENT

            else:
                return {'message': 'Operation error' }, HTTPStatus.BAD_REQUEST
                    

class DoctorSpecializationResource( Resource ):

    def get(self, specialization):
        
        data = []
        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        data =[]
        
        with connection.cursor() as cur:
            cur.callproc("doctor_pkg.read_doctor_specialization", [specialization,])
            records = get_listformat(cur)

            if records is None:   return {'message':"Not Found"}, HTTPStatus.NOT_FOUND
            
            for row in records:
                doctor = Doctor(*list(row))
                data.append(doctor.data)
                    
        return {'data': data }, HTTPStatus.OK