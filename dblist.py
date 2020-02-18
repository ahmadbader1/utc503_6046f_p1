import dbConnection as db


class dblist:
    
    def listCours(self):
        conn = db.get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM cours"
        cursor.execute(query)
        rows = cursor.fetchall()
        if not rows:
            print("Pas de cour")
        else:
            print("Code - Name - Niveau")
            for row in rows:
                print("%s - %s - %s" %(row[1],row[2],row[3]))
    def listEtudiants(self):
        conn = db.get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM etudiants"
        cursor.execute(query)
        rows = cursor.fetchall()
        if not rows:
            print("Pas de cour")
        else:
            print("Num - Prenom - Name - Niveau")
            for row in rows:
                print("%s - %s - %s - %s" %(row[0],row[1],row[2],row[3]))
    def listNotes(self,codeCour,numEtudiant):
        conn = db.get_connection()
        if codeCour !='' and numEtudiant !='' :
            query = "SELECT e.id,e.nom,c.code,c.niveau,note.note FROM note join cours c on note.codeCour = c.code join etudiants e on note.etudiantId = e.id where note.codeCour = %s and note.etudiantId = %s"
            dataCondition = (codeCour,numEtudiant)
        elif  codeCour !='' :
            query = "SELECT e.id,e.nom,c.code,c.niveau,note.note FROM note join cours c on note.codeCour = c.code join etudiants e on note.etudiantId = e.id where note.codeCour = %s"
            dataCondition = (codeCour)
        elif  numEtudiant !='' :
            query = "SELECT e.id,e.nom,c.code,c.niveau,note.note FROM note join cours c on note.codeCour = c.code join etudiants e on note.etudiantId = e.id where note.etudiantId = %s"
            dataCondition = (numEtudiant)
        cursor = conn.cursor()
        cursor.execute(query,dataCondition)
        rows = cursor.fetchall()
        if not rows:
            print("Pas de note")
        else:
            print("E.Num - E.Name  - Cour  - Niveau - Note")
            for row in rows:
                print(" %s    -  %s - %s -   %s  -  %s" %(row[0],row[1],row[2],row[3],row[4]))

    # def function_name(self,result):
    #     table=BeautifulTable()
    #     table.column_headers["DJ Name"]
    #     for row in result:
    #         table.append_row(row)
    #     print(table)
   
c = dblist()
#c.listCours()
#c.listEtudiants()
c.listNotes('',5)
#c.ajouterCour('utc_505','SI','B')
#c.suprimeCour(2)
#c.editCour(2,'GDN100','Management','B')



    