#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
#  morpion.py
#  
#  Copyright 2013 Gaétan Bahl <blacky@netbook>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
#au morpion les ronds commencent, on part du principe que l'ordinateur joue les ronds, quitte à  changer f en moins f =)



e = "_" 
o = 'o'
x = 'x'



def est_rempli(tableau): #renvoie true ou false
  est_remplie = True
  for i in tableau:
    for j in i:
      if j != "x" and  j != "o":
		est_remplie = False
  return est_remplie

def state(tableau): # fonction qui prend un tableau et qui vérifie l'état de la partie (en cours, win, lose, draw)
  a,b,c = tableau[0],tableau[1],tableau[2]
  state = ""
  victoire = False
  
  for i in range(3):#check les colonnes
    if a[i] == b[i] and a[i] == c[i] and (a[i] == "o" or a[i] == "x"):
      state = str(a[i]) + " win"
      victoire = True
     #check les lignes
    if (tableau[i][0] == tableau[i][1]) and (tableau[i][1] == tableau[i][2])  and (tableau[i][0] == "o"  or tableau[i][0] == "x"):
      state = str(tableau[i][0]) + " win"     
      victoire = True
     
      
  
  if tableau[0][0] == tableau[1][1] and tableau[0][0] == tableau[2][2] and  (tableau[0][0] == "o" or  tableau[0][0] == "x"):
    state = str(a[0]) + " win"
    victoire = True
  if tableau[0][2] == tableau[1][1] and tableau[1][1] == tableau[2][0] and  (tableau[0][2] == "o" or tableau[0][2] == "x"):
    state = str(a[2]) + " win"
    victoire = True
  
  if victoire == False:
    if est_rempli(tableau) and state == "":
      state = "draw"
    elif not est_rempli(tableau) and state == "":
      state = "in progress"
    
  
  return state

def tour(tableau): #renvoie x ou o
	compteurx = 0
	compteuro = 0 
	tour = ''
	for i in tableau:
		for j in i:
			if j == "x":
				compteurx += 1
			elif j == "o":
				compteuro +=1
			else:
				pass
	if compteuro == compteurx:
		tour = 'o'
	elif compteuro > compteurx:
		tour = 'x'
	else:
		tour = "fuck you"
	return tour
	
def cases_vides(tableau): #ON RENVOIE UNE LISTE TUPLES
	liste_cases = []
	for i in range(3):
		for j in range(3):
			if tableau[i][j] != "x" and tableau[i][j] != "o":
				liste_cases.append((i,j))
	return liste_cases

def tableaux_possibles(grille): #RENVOYER UNE LISTE DES GRILLES POSSIBLES
	poney = [i[:] for i in grille]
	cases = cases_vides(grille)
	joueur = tour(grille)
	tableau_transforme = grille
	tableau_de_tableaux = []
	for i in cases:
		grille = [j[:] for j in poney]
		x,y = i
		grille[x][y] = joueur
		tableau_de_tableaux.append(grille)
		
	return tableau_de_tableaux
	
def representation(grille): #renvoie une string representant la grille
	texte = ""
	for i in grille:
		for j in i:
			if j == "o" or j == "x":
				texte += j
			else:
				texte += "_"
		texte += "\n"
	return texte
	
def representation_liste(liste_de_grilles):  #pareil avec plusieurs grilles dans une liste
	texte = ""
	for i in liste_de_grilles:
		texte = texte + representation(i) + "\n"
	return texte
		
def normaliser(grille): #remplace le bordel dans une grille par des "_"
	for i in range(3):
		for j in range(3):
			if grille[i][j] != "o" and grille[i][j] != "x":
				grille[i][j] = "_"
	return grille

def arbre_a_partir_de(grille):
	grille_normalisee = normaliser(grille)
	cases = cases_vides(grille_normalisee)
	joueur = tour(grille_normalisee)
	status = state(grille_normalisee)
	print status
	if status == "in progress":
		print joueur + " play"
		for i in cases:
			x,y = i
			grilleupdate = grille_normalisee
			print grille_normalisee
			grilleupdate[x][y] = joueur
			print representation(grilleupdate)
			grille[x][y] = arbre_a_partir_de(grilleupdate)
		print "__________________________"
		return grille
	else:
		return status

def arbre_dico(grille): #faire des dictionaires 
	etat = state(grille)
	dico = {"grille":grille}
	dico["subtree"] = []
	if  etat == "in progress":
		for i in tableaux_possibles(grille):
			 dico["subtree"].append(arbre_dico(i))
	else:
		dico["subtree"] = etat
	return dico

def nombre_objets_ligne(lettre,grille,ligne):
	nombre = 0
	for i in grille[ligne]:
		if i == lettre:
			nombre += 1
	return nombre
	
	

def prendre_liste_grilles(arbre):
	liste_grilles = []
	liste_grilles.append(arbre["grille"])
	if isinstance(arbre["subtree"],str):
		return liste_grilles
	else:
		for i in arbre["subtree"]:
			for j in parcourir(i):
				liste_grilles.append(j)
		return liste_grilles

def main():
	
	#print est_rempli([[o,o,o],[e,o,x],[x,x,e]])
	#print representation_liste(tableaux_possibles([[o,o,o],[e,o,x],[x,x,e]]))
	#liste = arbre_a_partir_de([[o,e,e],[x,o,x],[o,e,x]])
	#print state([[o,o,o],[x,x,o],[x,o,x]])
	#print arbre_dico([[o,o,e],[e,x,o],[x,e,e]])
	#print tour([[o,o,e],[e,x,o],[x,e,e]])
	poney = arbre_dico([[e,e,e],[e,e,e],[e,e,e]])
	for i in prendre_liste_grilles(poney):
		print representation(i)
if __name__ == "__main__":
	main() 
