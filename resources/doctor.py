from flask import Flask 
from flask_restful import Resource
from http import HTTPStatus

# import utils.config

from models.doctor import Doctor 

import cx_Oracle



class DoctorListResource( Resource ):

    def get(self):
        host_name = 'localhost'
        port_number = 1521
        service_name = 'doc_consult_db'

        user = 'admin_user'
        pcode = 'Admin$12345'

        connection = None
        try:
    
            constring = host_name+':'+str(port_number)+'/'+service_name
            connection = cx_Oracle.connect(user, pcode, constring, encoding='UTF-8')

        except Exception as ex:
            return {'message' : ex}, HTTPStatus.NOT_FOUND
        # connection = config.connection
        data = []
        with connection.cursor() as cur:
            for row in cur.execute('select * from doctor'):
                retrived_data = list(row)
                doctor = Doctor(*retrived_data)
                data.append(doctor.data)

        connection.close()
        return {'data': data }