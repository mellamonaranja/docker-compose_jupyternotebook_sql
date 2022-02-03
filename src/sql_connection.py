import mysql.connector
from config import SQL_CONFIG


class SQLconnector:
    def __init__(self):
        print('creating')
        self.mydb=None
        
    def connect(self):
        
        mydb=mysql.connector.connect(host=SQL_CONFIG['host'],port=SQL_CONFIG['port'],
                                     user=SQL_CONFIG['user'],password=SQL_CONFIG['password'],database=SQL_CONFIG['database'])
        print(mydb)
        

        self.mydb=mydb

    def isConnected(self):
        if self.mydb is not None:
            return True
        else:
            return False
        
    def getConnection(self):
        if not self.isConnected():
            self.connect()
        return self.mydb.cursor(buffered=True)