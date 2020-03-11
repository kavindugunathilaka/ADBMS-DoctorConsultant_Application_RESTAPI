from flask import request 
from flask_restful import Resource
from http import HTTPStatus

from utils.dbconn import connection

from models.patient import Patient 




class PatientListResource( Resource ):

    def get(self):
        
        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        data =[]
        
        with connection.cursor() as cur:
            cur.execute('select * from patient')
            records = cur.fetchall()

            if len(records) == 0:   return {'message':"Not Found"}, HTTPStatus.NOT_FOUND
            
            for row in records:
                patient = Patient(*list(row))
                data.append(patient.data)

        connection.close()
        
        return {'data': data }, HTTPStatus.OK

    def post(self):

        if connection is None:  return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE

        data = request.get_json()
        # patient = Patient(
        #     data['patient_id'],
        #     data['first_name'],
        #     data['last_name'],
        #     data['age'],
        #     data['mobile_number'],
        #     data['email_address'],
        #     data['guardian_name'],
        #     data['guardian_mobile']
        #     )

        sql_query = """
            BEGIN
                INSERT INTO patient (first_name, last_name, age, mobile_number, email_address, guardian_name, guardian_mobile) 
                VALUES 
                ( :first_name, :last_name, :age, :mobile_number, :email_address, :guardian_name, :guardian_mobile)
                RETURNING patient_id INTO :patient_id;
                COMMIT;
            END;
            """

        with connection.cursor() as cur:
            data['patient_id'] = cur.var(cx_Oracle.NUMBER)
            cur.execute(sql_query, data )
            data['patient_id'] = int(data['patient_id'].getvalue())
        
        connection.close()

        return {'data': data }, HTTPStatus.OK



class PatientResource( Resource ):

    def get(self, patient_id):
        
        patient = None
        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        data =[]
        
        with connection.cursor() as cur:
            cur.execute('select * from patient where patient_id = :id',{'id':patient_id})
            record = cur.fetchone()

            if record is None:
                connection.close()
                return {'message':"Not Found"}, HTTPStatus.NOT_FOUND
            else:
                patient = Patient(*record)
                    
        connection.close()
        return {'data': patient.data }, HTTPStatus.OK
        

    def put(self, patient_id):
        pass


    def delete(self, patient_id):
        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        
        with connection.cursor() as cur:
            if cur.execute('DELETE FROM patient WHERE patient_id = :id',{'id':patient_id}):
                return {}, HTTPStatus.NO_CONTENT

            else:
                return {'message': 'Operation error' }, HTTPStatus.BAD_REQUEST
                    
        connection.close()



class PatientMobileNumberResource( Resource ):

    def get(self, mobile_number):
        
        patient = None
        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        with connection.cursor() as cur:
            cur.execute('select * from patient where mobile_number = :mob',{'mob':mobile_number})
            record = cur.fetchone()

            if record is None:
                connection.close()
                return {'message':"Not Found"}, HTTPStatus.NOT_FOUND
            else:
                patient = Patient(*record)
                    
        connection.close()
        return {'data': patient.data }, HTTPStatus.OK
        

    def put(self, mobile_number):
        pass


    def delete(self, mobile_number):
        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        
        with connection.cursor() as cur:
            if cur.execute('DELETE FROM patient WHERE mobile_number = :mob',{'mob':mobile_number}):
                return {}, HTTPStatus.NO_CONTENT

            else:
                return {'message': 'Operation error' }, HTTPStatus.BAD_REQUEST
                    
        connection.close()


