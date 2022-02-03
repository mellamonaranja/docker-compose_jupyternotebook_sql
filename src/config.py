import os

SQL_HOST=os.getenv('SQL_HOST')
if SQL_HOST==None:
    SQL_HOST='http://localhost'

SQL_PORT=os.getenv('SQL_PORT')
if SQL_PORT==None:
    SQL_PORT=3306
else:
    SQL_PORT=int(SQL_PORT)
    
SQL_USER=os.getenv('SQL_USER')
if SQL_USER==None:
    SQL_USER='root'
    
SQL_PASSWORD=os.environ.get('SQL_PASSWORD')
if SQL_PASSWORD==None:
    SQL_PASSWORD='123'
    
SQL_DATABASE=os.environ.get('SQL_DATABASE')
if SQL_DATABASE==None:
    SQL_DATABASE='db'

SQL_CONFIG={
    'host': SQL_HOST,
    'port': SQL_PORT,
    'user': SQL_USER,
    'password': SQL_PASSWORD,
    'database': SQL_DATABASE
}
print(SQL_CONFIG)