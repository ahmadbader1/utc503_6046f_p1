import dbConnection as db

class cours:
    code: str 
    nom: str
    niveau: str
    def ajouterCour(self,code,nom,niveau):
        query = "INSERT INTO cours(code,nom,niveau) VALUES(%s,%s,%s)"
        data = (code, nom, niveau)
        try:
            conn = db.get_connection()
            cursor = conn.cursor()
            cursor.execute(query, data)
            if cursor.lastrowid:
                print('last insert id', cursor.lastrowid)
            else:
                print('last insert id not found')
            conn.commit()
        except error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()
    def suprimeCour(self,id):
        query = "DELETE FROM cours WHERE id= %s"
        data = (id)
        try:
            conn = db.get_connection()
            cursor = conn.cursor()
            cursor.execute(query, data)
            conn.commit()
            print("Total rows deleted: %d" % cursor.rowcount)
        except error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()

    def editCour(self,id,code,nom,niveau):
        query = " UPDATE cours SET code = %s,nom = %s,niveau = %s WHERE id = %s "
        data = (code, nom, niveau,id)
        try:
            conn = db.get_connection()
            cursor = conn.cursor()
            cursor.execute(query, data)
            conn.commit()
            print('Cour: %d' % id + ' Updated')
        except error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()
c = cours()
#c.ajouterCour('utc_505','SI','B')
#c.suprimeCour(2)
#c.editCour(2,'GDN100','Management','B')



    