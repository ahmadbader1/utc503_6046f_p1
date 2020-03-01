from Etudiant import *
from Cours import *
from Note import *
from functools import reduce

a1 = Etudiant("1234", "Ahmad", "Mouhammad", "B")
a2 = Etudiant("6789", "Imad", "Mouhammad", "B")
a3 = Etudiant("3672", "Majed", "Karim", "C")

c1 = Cours("utc503", "Paradigmes", "B")
c2 = Cours("utc505", "SI", "B")
c3 = Cours("utc504", "Reseaux", "C")

n1 = Note("1234", "utc503", 14)
n2 = Note("1234", "utc503", 19)
n3 = Note("6789", "test", 15)

etudiants = [a1, a2]
cours = [c1,c2]
notes = [n1,n2,n3]

def returnNote(n, code):
    if n.codeCours == code:
        return n.note

def moyenneCours(cours):
    listeNotes = list(filter(lambda x: x.codeCours == cours, notes))
    listeValeurs = list(map(lambda x: x.note, listeNotes))
    return  reduce(lambda x,y: x+y, listeValeurs)/len(listeValeurs)

def moyenneEtudiant(etu):
    listeNotes = list(filter(lambda x: x.numEtudiant == etu, notes))
    listeValeurs = list(map(lambda x: x.note, listeNotes))
    return  reduce(lambda x,y: x+y, listeValeurs)/len(listeValeurs)

def consulterClasse(idCours):
    listeNotes =  list(filter(lambda x: x.codeCours == idCours, notes))
    return list(map(lambda x: x.note, listeNotes))

def consulterEtudiant(idEtu):
    listeNotes = list(filter(lambda x: x.numEtudiant == idEtu, notes))
    return list(map(lambda x: x.note, listeNotes))

print(consulterEtudiant("1234"))