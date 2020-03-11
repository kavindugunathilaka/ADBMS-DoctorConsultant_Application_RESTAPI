from flask import request 
from flask_restful import Resource
from http import HTTPStatus

from utils.dbconn import connection

from models.consultant_datetime import Consultant_datetime 




class ConsultantDateTimeListResource( Resource ):

    def get(self):
        
        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        data =[]
        
        with connection.cursor() as cur:
            cur.execute('select * from consultant_datetime')
            records = cur.fetchall()

            if len(records) == 0:   return {'message':"Not Found"}, HTTPStatus.NOT_FOUND
            
            for row in records:
                consultantDateTime = Consultant_datetime(*list(row))
                data.append(consultantDateTime.data)

        connection.close()
        
        return {'data': data }, HTTPStatus.OK

    def post(self):

        if connection is None:  return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE

        data = request.get_json()
        # consultDateTime = Consultant_datetime(
        #     data['consult_id'],
        #     data['consult_date'],
        #     data['consult_date'],
        #     data['status'],
        #     data['receptionist_id']
        #     )

        sql_query = """
            BEGIN
                INSERT INTO consultant_datetime (consult_id, consult_date, consult_time, status, receptionist_id) 
                VALUES 
                ( TO_DATE(:consult_date, 'yyyy/mm/dd'), TO_DATE(:consult_time,'hh:mm'), :status, :receptionist_id)
                RETURNING consult_id INTO :consult_id;
                COMMIT;
            END;
            """

        with connection.cursor() as cur:
            data['consult_id'] = cur.var(cx_Oracle.NUMBER)
            cur.execute(sql_query, data )
            data['consult_id'] = int(data['consult_id'].getvalue())
        
        connection.close()

        return {'data': data }, HTTPStatus.OK


class ConsultantDateTimeResource( Resource ):

    def get(self, consult_id):
        
        Consultant_datetime = None
        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        data =[]
        
        with connection.cursor() as cur:
            cur.execute('select * from consultant_datetime where consult_id = :id',{'id':consult_id})
            record = cur.fetchone()

            if record is None:
                connection.close()
                return {'message':"Not Found"}, HTTPStatus.NOT_FOUND
            else:
                consultantDateTime = Consultant_datetime(*record)
                    
        connection.close()
        return {'data': consultantDateTime.data }, HTTPStatus.OK
        

    def put(self, consult_id):
        pass


    def delete(self, consult_id):
        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        
        with connection.cursor() as cur:
            if cur.execute('DELETE FROM consultant_datetime WHERE consult_id = :id',{'id':consult_id}):
                return {}, HTTPStatus.NO_CONTENT

            else:
                return {'message': 'Operation error' }, HTTPStatus.BAD_REQUEST
                    
        connection.close()

class ConsultStatusResource( Resource ):

    def get(self, status):
        
        
        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        data =[]
        
        with connection.cursor() as cur:
            cur.execute('select * from consultant_datetime where status = :status',{'status':status})
            record = cur.fetchone()

            if record is None:
                connection.close()
                return {'message':"Not Found"}, HTTPStatus.NOT_FOUND
            else:
                consultDateTime = Consultant_datetime(*record)
                    
        connection.close()
        return {'data': data }, HTTPStatus.OK
        

