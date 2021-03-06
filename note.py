from __future__ import division
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
    def suprimeNote(self,id):
        query = "DELETE FROM note WHERE id= %s"
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

    def editNote(self,id,note):
        query = " UPDATE note SET note = %s WHERE id = %s "
        data = (note,id)
        try:
            conn = db.get_connection()
            cursor = conn.cursor()
            cursor.execute(query, data)
            conn.commit()
            print('Note: %d' % id + ' Updated')
        except error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()
    def calculeMoyenneClass(self,codeCour):
        try:
            conn = db.get_connection()
            cursor = conn.cursor()
            query = "SELECT SUM(note) as sum FROM note WHERE codeCour = %s"
            dataNote = (codeCour)
            cursor.execute(query,dataNote)
            cursor2 = conn.cursor()
            query2 = "SELECT * FROM note WHERE codeCour = %s"
            dataNote = (codeCour)
            cursor2.execute(query2,dataNote)
            count = cursor2.rowcount
            conn.commit()
            print("Moyenne: %d" %float(cursor.fetchone()[0]/float(count)) )
        except error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()
    def calculeMoyenneEtudiant(self,codeEtudiant):
        try:
            conn = db.get_connection()
            cursor = conn.cursor()
            query = "SELECT SUM(note) as sum FROM note WHERE etudiantId = %s"
            dataNote = (codeEtudiant)
            cursor.execute(query,dataNote)
            cursor2 = conn.cursor()
            query2 = "SELECT * FROM note WHERE etudiantId = %s"
            dataNote = (codeEtudiant)
            cursor2.execute(query2,dataNote)
            count = cursor2.rowcount
            conn.commit()
            print("Moyenne: %d" %float(cursor.fetchone()[0]/float(count)) )
        except error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()


n = note()
#n.ajouterNote('utc_504','5',19)
#n.suprimeNote(2)
#n.editNote(3,18)
n.calculeMoyenneClass('utc_503')
n.calculeMoyenneEtudiant(5)



    