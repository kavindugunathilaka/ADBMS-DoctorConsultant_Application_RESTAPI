from flask import request 
from flask_restful import Resource
from http import HTTPStatus

from utils.dbconn import connection

from models.medical_records import Medical_records 



class MedicalRecordsResource( Resource ):

    def get(self, medical_record_id):
        
        Medical_records = None
        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        data =[]
        
        with connection.cursor() as cur:
            cur.execute('select * from medical_records where medical_record_id = :id',{'id':medical_record_id})
            record = cur.fetchone()

            if record is None:
                connection.close()
                return {'message':"Not Found"}, HTTPStatus.NOT_FOUND
            else:
                medicalRecord = Medical_records(*record)
                    
        connection.close()
        return {'data': medicalRecord.data }, HTTPStatus.OK
        


    def put(self, medical_record_id):
        pass


    def delete(self, medical_record_id):
        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        
        with connection.cursor() as cur:
            if cur.execute('DELETE FROM medical_records WHERE medical_record_id = :id',{ 'id':medical_record_id }):
                return {}, HTTPStatus.NO_CONTENT

            else:
                return {'message': 'Operation error' }, HTTPStatus.BAD_REQUEST
                    
        connection.close()


