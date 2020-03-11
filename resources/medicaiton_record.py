from flask import request 
from flask_restful import Resource
from http import HTTPStatus

from utils.dbconn import connection

from models.medication_record import Medication_record 




class MedicationRecordsListResource( Resource ):

    def get(self):
        
        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        data =[]
        
        with connection.cursor() as cur:
            cur.execute('SELECT * from medication_record')
            records = cur.fetchall()

            if len(records) == 0:   return {'message':"Not Found"}, HTTPStatus.NOT_FOUND
            
            for row in records:
                medicationRecord = Medication_record(*list(row))
                data.append(medicationRecord.data)

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
                INSERT INTO medication_record (prescription, date_prescribed, medication_issued, doctor_id, patient_id, pharmacist_id) 
                VALUES 
                ( :prescription, TO_DATE(:date_prescribed), TO_DATE(:medication_issued), :doctor_id, :patient_id, :pharmacist_id)
                RETURNING med_record_id INTO :med_record_id;
                COMMIT;
            END;
            """

        with connection.cursor() as cur:
            data['med_record_id'] = cur.var(cx_Oracle.NUMBER)
            cur.execute(sql_query, data )
            data['med_record_id'] = int(data['med_record_id'].getvalue())
        
        connection.close()

        return {'data': data }, HTTPStatus.OK



class MedicationRecordResource( Resource ):

    def get(self, med_record_id):
        
        medicationRecord = None
        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        with connection.cursor() as cur:
            cur.execute('SELECT * FROM medication_record where med_record_id = :id',{'id':med_record_id})
            record = cur.fetchone()

            if record is None:
                connection.close()
                return {'message':"Not Found"}, HTTPStatus.NOT_FOUND
            else:
                medicationRecord = Medication_record(*record)
                    
        connection.close()
        return {'data': medicationRecord.data }, HTTPStatus.OK
        

    def put(self, med_record_id):
        pass


    def delete(self, med_record_id):
        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        
        with connection.cursor() as cur:
            if cur.execute('DELETE FROM medication_record WHERE med_record_id = :id',{'id':med_record_id }):
                return {}, HTTPStatus.NO_CONTENT

            else:
                return {'message': 'Operation error' }, HTTPStatus.BAD_REQUEST
                    
        connection.close()



# class MedicaitonRecordPatientResource( Resource ):

#     def get(self, patient_id):
        
#         patient = None
#         if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
#         with connection.cursor() as cur:
#             cur.execute('SELECT * FROM medication_record WHERE patient_id = :id',{'id':patient_id})
#             record = cur.fetchone()

#             if record is None:
#                 connection.close()
#                 return {'message':"Not Found"}, HTTPStatus.NOT_FOUND
#             else:
#                 patient = Patient(*record)
                    
#         connection.close()
#         return {'data': patient.data }, HTTPStatus.OK
        

#     def put(self, mobile_number):



#     def delete(self, mobile_number):
#         if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        
#         with connection.cursor() as cur:
#             if cur.execute('DELETE FROM patient WHERE mobile_number = :mob',{'mob':mobile_number}):
#                 return {}, HTTPStatus.NO_CONTENT

#             else:
#                 return {'message': 'Operation error' }, HTTPStatus.BAD_REQUEST
                    
#         connection.close()


