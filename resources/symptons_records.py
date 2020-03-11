from flask import request 
from flask_restful import Resource
from http import HTTPStatus

from utils.dbconn import connection

from models.symptoms_record import Symptoms_record


class SymptomsRecordsResource(Resource):

    def get(self):
        
        if connection is None:  return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        data =[]
        
        with connection.cursor() as cur:
            cur.execute('SELECT DISTINCT symptom FROM symptons_record')
            records = cur.fetchall()

            if len(records) == 0:   return {'message':"Not Found"}, HTTPStatus.NOT_FOUND
            
            for row in records:
                data.append(str(row[0]))

        connection.close()
        
        return {'data': data }, HTTPStatus.OK


class SymptomsRecordsMedicalResource( Resource ):

    def get(self, medical_record_id):
        
        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        data =[]
        
        with connection.cursor() as cur:
            cur.execute('SELECT * FROM symptons_record WHERE medical_record_id = :id', { 'id': medical_record_id } )
            records = cur.fetchall()

            if len(records) == 0:   return {'message':"Not Found"}, HTTPStatus.NOT_FOUND
            
            for row in records:
                symptomsRecord = Symptoms_record(*list(row))
                data.append(symptomsRecord.data)

        connection.close()
        
        return {'data': data }, HTTPStatus.OK

    def delete(self, medical_record_id):
        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        with connection.cursor() as cur:
            if cur.execute('DELETE FROM symptons_record WHERE medical_record_id = :id',{'id':medical_record_id }):
                return {}, HTTPStatus.NO_CONTENT

            else:
                return {'message': 'Operation error' }, HTTPStatus.BAD_REQUEST
                    
        connection.close()


