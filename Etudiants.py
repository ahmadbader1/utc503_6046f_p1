import dbConnection as db

class etudiants:
    #num: int
    prenom: str 
    nom: str
    niveau: str

    # def __init__(self,prenom,nom,niveau):
    #     #self.num = num
    #     self.prenom = prenom
    #     self.nom = nom
    #     self.niveau = niveau
    
    
    def ajouterEtudiant(self,prenom,nom,niveau):
        query = "INSERT INTO etudiants(prenom,nom,niveau) VALUES(%s,%s,%s)"
        data = (prenom, nom, niveau)
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
    def suprimeEtudiant(self,num):
        query = "DELETE FROM etudiants WHERE id= %s"
        query2 = "DELETE FROM note WHERE etudiantID= %s"
        data = (num)
        try:
            conn = db.get_connection()
            cursor = conn.cursor()
            cursor.execute(query, data)
            cursor.execute(query2, data)
            conn.commit()
            print("Total rows deleted: %d" % cursor.rowcount)
        except error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()
            

    def editEtudiant(self,num,prenom,nom,niveau):
        query = " UPDATE etudiants SET prenom = %s,nom = %s,niveau = %s WHERE id = %s "
        data = (prenom, nom, niveau,num)
        try:
            conn = db.get_connection()
            cursor = conn.cursor()
            cursor.execute(query, data)
            conn.commit()
            print('Etudiant: %d' % num + ' Updated')
        except error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()
a = etudiants()
a.ajouterEtudiant('Anas','Ezzo','B')
a.ajouterEtudiant('Imad','Ragheb','C')
a.ajouterEtudiant('Khalil','Sami','A')
#a.suprimeEtudiant(2)
#a.editEtudiant(2,'Bader','Hamoud','c')



    