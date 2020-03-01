class Etudiant:

    def __init__(self, numero, nom, prenom, niveau):
        
        self._numero = numero
        self._nom = nom
        self._prenom = prenom
        if(niveau in ['A', 'B', 'C']):
            self._niveau = niveau
        else:
            print("Le niveau doit eter  A, B  ou C.")
            self._niveau = "A" 

    
    def _getNom(self):
        return self._nom
    
    def _setNom(self, nom):
        self._nom = nom

    def _getNumero(self):
        return self._numero
    
    def _setNumero(self, num):
        self._numero = num

    def _getPrenom(self):
        return self._prenom

    def _setPrenom(self, prenom):
        self._prenom = prenom

    def _getNiveau(self):
        return self._niveau
    def _setNiveau(self, n):
        if(n in ["A", "B", "C"]):
            self._niveau = n
        else:
            print("Le niveau doit eter A, B  ou C.")
            self._niveau = "A"

    numero = property(_getNumero, _setNumero)
    nom = property(_getNom, _setNom)
    prenom = property(_getPrenom, _setPrenom)
    niveau = property(_getNiveau, _setNiveau)