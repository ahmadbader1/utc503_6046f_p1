import pymysql

def get_connection():
    _connection = pymysql.connect(host='localhost',port=33067,user='root',password='',db='miniproject')
    if _connection: 
       return _connection
    else:
        return "No database connection"