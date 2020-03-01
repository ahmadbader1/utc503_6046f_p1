from BD import *


start = BD([], [], [])

start.ajouterEtudiant("1234", "Ahmad", "Mohammad", "B")
start.ajouterEtudiant("5678", "Imad", "Mohammad", "B")
start.ajouterEtudiant("3271", "Majed", "Karim", "C")
start.ajouterCours("utc503", "Paradigmes", "B")
start.ajouterCours("utc505", "SI", "B")
start.ajouterCours("utc504", "Reseaux", "C")

start.ajouterNote("1234", "utc503", 18)
start.ajouterNote("1234", "utc505", 17)
start.ajouterNote("1234", "utc504", 15)
start.ajouterNote("5678", "utc503", 15)
start.ajouterNote("5678", "utc505", 16)
start.ajouterNote("5678", "utc504", 19)

print(start.consulterNotesEtudiant("1234"))

print(start.moyenneClassV2("utc503"))
