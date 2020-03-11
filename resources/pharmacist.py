
from flask import request 
from flask_restful import Resource
from http import HTTPStatus

from utils.dbconn import connection

from models.pharmacist import Pharmacist 




class PharmacistListResource( Resource ):

    def get(self):
        
        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        data =[]
        
        with connection.cursor() as cur:
            cur.execute('select * from pharmacist')
            records = cur.fetchall()

            if len(records) == 0:   return {'message':"Not Found"}, HTTPStatus.NOT_FOUND
            
            for row in records:
                pharmacist = Pharmacist(*list(row))
                pharmacist.append(pharmacist.data)

        connection.close()
        
        return {'data': data }, HTTPStatus.OK

    def post(self):

        if connection is None:  return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE

        data = request.get_json()
        # pharmacist = Pharmacist(
        #     data['first_name'],
        #     data['last_name'],
        #     data['mobile_number'],
        #     data['email_address'],
        #     data['username']
        #     )

        sql_query = """
            BEGIN
                INSERT INTO pharmacist (first_name, last_name, mobile_number, email_address, username) 
                VALUES 
                ( :first_name, :last_name, :mobile_number, :email_address, :username)
                RETURNING pharmacist_id INTO :pharmacist_id;
                COMMIT;
            END;
            """

        with connection.cursor() as cur:
            data['pharmacist_id'] = cur.var(cx_Oracle.NUMBER)
            cur.execute(sql_query, data )
            data['pharmacist_id'] = int(data['pharmacist_id'].getvalue())
        
        connection.close()

        return {'data': data }, HTTPStatus.OK


class PharmacistResource( Resource ):

    def get(self, pharmacist_id):
        
        doctor = None
        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        data =[]
        
        with connection.cursor() as cur:
            cur.execute('select * from pharmacist where pharmacist_id = :id',{'id':pharmacist_id})
            record = cur.fetchone()

            if record is None:
                connection.close()
                return {'message':"Not Found"}, HTTPStatus.NOT_FOUND
            else:
                pharmacist = Pharmacist(*record)
                    
        connection.close()
        return {'data': pharmacist.data }, HTTPStatus.OK
        
    def put(self, doctor_id):
        pass


    def delete(self, doctor_id):

        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        with connection.cursor() as cur:
            if cur.execute('DELETE FROM pharmacist WHERE pharmacist_id = :id',{'id':pharmacist_id}):
                return {}, HTTPStatus.NO_CONTENT

            else:
                return {'message': 'Operation error' }, HTTPStatus.BAD_REQUEST
                    
        connection.close()
