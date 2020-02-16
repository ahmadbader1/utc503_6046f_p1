import pymysql

class dbConnection:

    def __init__ (self):
        self.con=pymysql.connect(host='localhost',port=33067,user='root',password='',db='miniproject')
        self.cmd=self.con.cursor()
        
obj=dbConnection()