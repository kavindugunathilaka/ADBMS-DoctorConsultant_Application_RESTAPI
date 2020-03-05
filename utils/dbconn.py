
import cx_Oracle

class DbConnection():

    __host_name = 'localhost'
    __port_number = 1521
    __service_name = 'doc_consult_db'

    __user = 'admin_user'
    __pcode = 'Admin$12345'

    CON = None
    
    def __init__(self):
        try:
            constring = self.__host_name+':'+str(self.__port_number)+'/'+self.__service_name
            self.CON = cx_Oracle.connect(self.__user, self.__pcode, constring, encoding='UTF-8')
            # self.CON
        except Exception as ex:
            self.CON = None
    
    # def getConnection():
    #     return self.connection
        
    # def closeConnection():
    #     self.connection.close()

connection = DbConnection().CON