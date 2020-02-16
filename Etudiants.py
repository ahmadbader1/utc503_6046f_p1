import dbConnection

class Etudiants:
    a = dbConnection()
    sql = 'select * from `test`;'
    a.execute(sql)
    countrow = a.execute(sql)
    print("Number of rows :",countrow)
    data = a.fetchone()
    print(data)