import cx_Oracle

# from utils.db_helper import CursorByName
from models.doctor import Doctor

host_name = 'localhost'
port_number = 1521
service_name = 'doc_consult_db'

user = 'admin_user'
pcode = 'Admin$12345'

connection = None
try:
    
    constring = host_name+':'+str(port_number)+'/'+service_name
    connection = cx_Oracle.connect(user, pcode, constring, encoding='UTF-8')

    
    # data = {}
    with connection.cursor() as cur:
        cur.execute('select * from user_account_details')
        for col, description in enumerate(cur):
            print({description[0]: col})


        # return { description[0]: row[col] for col, description in enumerate(self._cursor.description) }    
        # for row in CursorByName(cur):
        #     print(row)

    #     num = 0
    #     for col in cur.description:
    #         data[col[0]] = retrived_data[num]
    #         num += 1
    # print(data)
    connection.close()

    # data = []
    # with connection.cursor() as cur:
    #     for row in cur.execute('select * from doctor'):
    #         retrived_data = list(row)
    #         doctor = Doctor(*retrived_data)
    #         data.append(doctor.data)

    print(data)

except Exception as ex:
    print("Message : {0}".format(ex))

