from flask import request 
from flask_restful import Resource
from http import HTTPStatus

from utils.dbconn import connection

from models.patient_medical_records import Patient_medical_records




class PatientMedicalRecordsResource( Resource ):

    def get(self, patient_id):
        
        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        data =[]
        
        with connection.cursor() as cur:
            cur.execute('SELECT * FROM patient_medical_records WHERE patient_id = :id', { 'id': patient_id } )
            records = cur.fetchall()

            if len(records) == 0:   return {'message':"Not Found"}, HTTPStatus.NOT_FOUND
            
            for row in records:
                patientMedicalRecords = Patient_medical_records(*list(row))
                data.append(patientMedicalRecords.data)

        connection.close()
        
        return {'data': data }, HTTPStatus.OK

    def delete(self, patient_id):
        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        with connection.cursor() as cur:
            if cur.execute('DELETE FROM patient_medical_records WHERE patient_id = :id',{'id':patient_id}):
                return {}, HTTPStatus.NO_CONTENT

            else:
                return {'message': 'Operation error' }, HTTPStatus.BAD_REQUEST
                    
        connection.close()


