from flask import request 
from flask_restful import Resource
from http import HTTPStatus

from utils.dbconn import connection

from models.doctor_consult_details import Doctor_consult_details




class DoctorConsultDetailsResource( Resource ):

    def get(self, doctor_id):
        
        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        data =[]
        
        with connection.cursor() as cur:
            cur.execute('SELECT * FROM doctor_consult_details WHERE doctor_id = :id', { 'id': doctor_id})
            records = cur.fetchall()

            if len(records) == 0:   return {'message':"Not Found"}, HTTPStatus.NOT_FOUND
            
            for row in records:
                doctorConsultDetail = Doctor_consult_details(*list(row))
                data.append(doctorConsultDetail.data)

        connection.close()
        
        return {'data': data }, HTTPStatus.OK

    def delete(self, doctor_id):
        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        with connection.cursor() as cur:
            if cur.execute('DELETE FROM doctor_consult_details WHERE doctor_id = :id',{'id':doctor_id}):
                return {}, HTTPStatus.NO_CONTENT

            else:
                return {'message': 'Operation error' }, HTTPStatus.BAD_REQUEST
                    
        connection.close()


