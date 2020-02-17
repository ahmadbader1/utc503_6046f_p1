import dbConnection as db

class note:
    codeCour: str 
    etudiantId: int
    note: float
    def ajouterNote(self,codeCour,etudiantId,note):
        try:
            conn = db.get_connection()
            cursor = conn.cursor()
            checkEtudiant = "SELECT * FROM etudiants WHERE id = %s"
            dataEtudiant = (etudiantId)
            cursor.execute(checkEtudiant,dataEtudiant)
            if len(cursor.fetchall()) > 0:
                checkCour = "SELECT * FROM cours WHERE code = %s"
                dataCour = (codeCour)
                cursor.execute(checkCour,dataCour)
                if len(cursor.fetchall()) > 0:
                    query = "INSERT INTO note(codeCour,etudiantId,note) VALUES(%s,%s,%s)"
                    data = (codeCour, etudiantId, note)
                    cursor.execute(query, data)
                    if cursor.lastrowid:
                        print('last insert id', cursor.lastrowid)
                    else:
                        print('last insert id not found')
                    conn.commit()
                else:
                    print('Cour does not exists')
            else:
                print('Etudiant does not exists')
            
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
n = note()
n.ajouterNote('utc_503','2',15)
#n.suprimeNote(2)
#n.editNote(2,'GDN100','Management','B')



    