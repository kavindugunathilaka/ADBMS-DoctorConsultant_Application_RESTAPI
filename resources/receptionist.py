
from flask import request 
from flask_restful import Resource
from http import HTTPStatus

from utils.dbconn import connection

from models.receptionist import Receptionist 




class ReceptionistListResource( Resource ):

    def get(self):
        
        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        data =[]
        
        with connection.cursor() as cur:
            cur.execute('select * from receptionist')
            records = cur.fetchall()

            if len(records) == 0:   return {'message':"Not Found"}, HTTPStatus.NOT_FOUND
            
            for row in records:
                receptionist = Receptionist(*list(row))
                data.append(receptionist.data)

        connection.close()
        
        return {'data': data }, HTTPStatus.OK


    def post(self):

        if connection is None:  return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE

        data = request.get_json()
        # receptionist = Receptionist(
        #     data['first_name'],
        #     data['last_name'],
        #     data['mobile_number'],
        #     data['email_address'],
        #     data['username']
        #     )

        sql_query = """
            BEGIN
                INSERT INTO receptionist (first_name, last_name, mobile_number, email_address, username) 
                VALUES 
                ( :first_name, :last_name, :mobile_number, :email_address, :username)
                RETURNING receptionist_id INTO :receptionist_id;
                COMMIT;
            END;
            """

        with connection.cursor() as cur:
            data['receptionist_id'] = cur.var(cx_Oracle.NUMBER)
            cur.execute(sql_query, data )
            data['receptionist_id'] = int(data['receptionist_id'].getvalue())
        
        connection.close()

        return {'data': data }, HTTPStatus.OK


class ReceptionistResource( Resource ):

    def get(self, receptionist_id):
        
        pharmacist = None
        if connection is None: return { 'message' : 'No Connection' }, HTTPStatus.SERVICE_UNAVAILABLE
        
        data =[]
        
        with connection.cursor() as cur:
            cur.execute('select * from receptionist where receptionist_id = :id', { 'id':receptionist_id } )
            record = cur.fetchone()

            if record is None:
                connection.close()
                return {'message':"Not Found"}, HTTPStatus.NOT_FOUND
            else:
                receptionist = Receptionist(*record)
                    
        connection.close()
        return {'data': receptionist.data }, HTTPStatus.OK
        
    
    def put(self, receptionist_id):
        pass


    
    def delete(self, receptionist_id):
        
        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        with connection.cursor() as cur:
            if cur.execute('DELETE FROM receptionist WHERE receptionist_id = :id',{'id':receptionist_id}):
                return {}, HTTPStatus.NO_CONTENT

            else:
                return {'message': 'Operation error' }, HTTPStatus.BAD_REQUEST
                    
        connection.close()

