from flask import request 
from flask_restful import Resource
from http import HTTPStatus
from datetime import datetime

from utils.dbconn import connection

from models.user_account_details import User_account_details




class UserAccountRegResource( Resource ):

    def post(self):

        if connection is None:  return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE

        data = request.get_json()
        patient = User_account_details(
            data['username'],
            data['digest_password'],
            datetime.today().strftime('%Y/%m/%d'),
            None
            )

        sql_query = """
            BEGIN
                INSERT INTO user_account_details (username, digest_password, account_created, account_last_login) 
                VALUES 
                ( :username, :digest_password, TO_DATE(:account_created), :account_last_login)
                RETURNING username INTO :username;
                COMMIT;
            END;
            """
        response_data = {'username': None}
        with connection.cursor() as cur:
            response_data['username'] = cur.var(cx_Oracle.VARCHAR2)
            cur.execute(sql_query, data )
            response_data['username'] = str(response_data['username'].getvalue())
            
        connection.close()
        
        return {'data': response_data }, HTTPStatus.OK


class UserVerResource( Resource ):

    def post(self):
        user = None
        if connection is None:  return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE

        data = request.get_json()
        patient = User_account_details(
            data['username'],
            data['digest_password'],
            None,
            None
            )

        sql_query = """
            BEGIN
                SELECT *  FROM user_account_details WHERE
                username = :username AND digest_password = :digest_password;
            END;
        """
        response_data = {'username': None}
        with connection.cursor() as cur:
            cur.execute(sql_query, data )
            record  = cur.fetchone()

            if record is None:
                connection.close()
                return { 'message': "Unauthorized" }, HTTPStatus.UNAUTHORIZED
            else:
                user = User_account_details(*record)
                user.digest_password = None
        connection.close()
        
        return {'data': user.data }, HTTPStatus.OK


    def put(self, username):
        """
            This put request used if user wanted to change password and username if required
        """
        pass

    def delete(self, username):
        if connection is None: return {'message':'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        
        
        with connection.cursor() as cur:
            if cur.execute('DELETE FROM username WHERE username = :uname',{'username':patient_id}):
                return {}, HTTPStatus.NO_CONTENT

            else:
                return {'message': 'Operation error' }, HTTPStatus.BAD_REQUEST
                    
        connection.close()