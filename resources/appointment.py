
from flask import request 
from flask_restful import Resource
from http import HTTPStatus

from utils.dbconn import connection

from models.appointment import Appointment 




class AppointmentListResource( Resource ):

    def get(self):
        
        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        data =[]
        
        with connection.cursor() as cur:
            cur.execute('select * from appointment')
            records = cur.fetchall()

            if len(records) == 0:   return {'message':"Not Found"}, HTTPStatus.NOT_FOUND
            
            for row in records:
                appointment = Appointment(*list(row))
                data.append(appointment.data)

        connection.close()
        
        return {'data': data }, HTTPStatus.OK


    def post(self):

        if connection is None:  return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE

        data = request.get_json()
        # appointment = Appointment(
        #     data['appointment_date'],
        #     data['appointment_time'],
        #     data['status'],
        #     data['patient_id'],
        #     data['doctor_id'],
        #     )

        sql_query = """
            BEGIN
                INSERT INTO appointment (appointment_date, appointment_time, status, patient_id, doctor_id, receptionist_id) 
                VALUES 
                ( TO_DATE(:appointment_date,'yyyy/mm/dd'), TO_DATE(:appointment_time, 'hh:mm'), :status, :patient_id, :doctor_id, :receptionist_id)
                RETURNING appointment_id INTO :appointment_id;
                COMMIT;
            END;
            """

        with connection.cursor() as cur:
            data['receptionist_id'] = cur.var(cx_Oracle.NUMBER)
            cur.execute(sql_query, data )
            data['receptionist_id'] = int(data['receptionist_id'].getvalue())
        
        connection.close()

        return {'data': data }, HTTPStatus.OK


class AppointmentResource( Resource ):

    def get(self, appointment_id):
        
        appointment = None
        if connection is None: return { 'message' : 'No Connection' }, HTTPStatus.SERVICE_UNAVAILABLE

        with connection.cursor() as cur:
            cur.execute('select * from appointment where appointment_id = :id', { 'id':appointment_id } )
            record = cur.fetchone()

            if record is None:
                connection.close()
                return {'message':"Not Found"}, HTTPStatus.NOT_FOUND
            else:
                appointment = Appointment(*record)
                    
        connection.close()
        return {'data': appointment.data }, HTTPStatus.OK
        
    
    def put(self, appointment_id):
        pass


    
    def delete(self, appointment_id):
        
        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        with connection.cursor() as cur:
            if cur.execute('DELETE FROM appointment WHERE appointment_id = :id',{'id':appointment_id}):
                return {}, HTTPStatus.NO_CONTENT

            else:
                return {'message': 'Operation error' }, HTTPStatus.BAD_REQUEST
                    
        connection.close()


class AppointmentRecepResource(Resource):

    def put(self, appointment_id, receptionist_id):
        pass

class AppointmentPatientResource(Resource):

    def get(self, patient_id):
        appointment = None
        if connection is None: return { 'message' : 'No Connection' }, HTTPStatus.SERVICE_UNAVAILABLE

        data = []
        with connection.cursor() as cur:
            cur.execute('select * from appointment where patient_id = :id', { 'id':patient_id } )
            record = cur.fetchall()

            if len(record) == 0:
                connection.close()
                return {'message':"Not Found"}, HTTPStatus.NOT_FOUND
            else:
                for row in record:
                    appointment = Appointment(*row)
                    data.append(appointment)    
        connection.close()
        return {'data': data }, HTTPStatus.OK

    
    def put(self, patient_id):
        pass
    
    def delete(self, patient_id):    
        pass

class AppointmentsDoctorResource(Resource):

    def get(self, doctor_id):
        appointment = None
        if connection is None: return { 'message' : 'No Connection' }, HTTPStatus.SERVICE_UNAVAILABLE
        
        data = []
        with connection.cursor() as cur:
            cur.execute('select * from appointment where doctor_id = :id', { 'id':doctor_id } )
            record = cur.fetchall()

            if len(record) == 0:
                connection.close()
                return {'message':"Not Found"}, HTTPStatus.NOT_FOUND
            else:
                for row in record:
                    appointment = Appointment(*row)
                    data.append(appointment)   
        connection.close()
        return {'data': data }, HTTPStatus.OK
        
    
    def put(self, doctor_id):
        pass
    
    def delete(self, doctor_id):
        pass

class AppointmentStatusResource(Resource):

    def get(self, status):
        appointment = None
        if connection is None: return { 'message' : 'No Connection' }, HTTPStatus.SERVICE_UNAVAILABLE
        
        data =[]
        
        with connection.cursor() as cur:
            cur.execute('select * from appointment where status = :status', { 'status': status } )
            record = cur.fetchall()

            if len(record) == 0:
                connection.close()
                return {'message':"Not Found"}, HTTPStatus.NOT_FOUND
            else:
                for row in record:
                    appointment = Appointment(*row)
                    data.append(appointment)
        connection.close()
        return {'data': data }, HTTPStatus.OK
        

    def put(self, status):
        pass

    def delete(self, status):
        pass