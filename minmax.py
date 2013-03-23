#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
#  minmax.py
#  
#  Copyright 2013 GaÃ©tan Bahl <blacky@netbook>
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
##implementation de min max sur l'arbre
#on part du principe qu'on joue les O

from morpion import *
import pickle

#fichier = open("arbre_dico_final","r")

#arbre = pickle.load(fichier)

poids_lose = -3000
poids_win = 3000
poids_draw = 100

x,o,e = 'x','o','_'


def isstring(machin):
  if isinstance(machin,str):
		return True
	else:
		return False
	

def align2(ligne, joueur):
	compteur = 0
	compteur_vide = 0
	for i in ligne:
		if i == joueur:
			compteur += 1
		elif i == "_":
			compteur_vide += 1
	if compteur == 2 and compteur_vide == 1:
		return 1
	else:
		return 0

def prendre_colonne (grille, numero):
	liste = []
	for i in range(3):
		liste.append(grille[i][numero])
	return liste

def prendre_diagonale (grille,boule):
	liste = []
	if boule == False:
		liste=[grille[0][0],grille[1][1],grille[2][2]]
	else:
		liste=[grille[0][2],grille[1][1],grille[2][0]]
	return liste

def evaluer(lettre_jou,lettre_adv,grille):
	poids = 0
	
	if state(grille) == lettre_jou + " win":
		return 3000
	if state(grille)  == lettre_adv + " win":
		return -3000
	if state(grille) == "draw":
		return poids_draw
	

	for i in grille: #on regarde sur les lignes
		poids += align2(i,lettre_jou)
		poids -= align2(i,lettre_adv)
	
	for i in range(3): #on regarde sur les colonnes
		poids += align2(prendre_colonne(grille,i),lettre_jou)
		poids -= align2(prendre_colonne(grille,i),lettre_adv)
	
	for i in [True,False]:
		poids += align2(prendre_diagonale(grille,i),lettre_jou)
		poids -= align2(prendre_diagonale(grille,i),lettre_adv)
	
	return poids

def state2(grille):
	if state(grille) == "o win" or state(grille) == "x win" or state(grille) == "draw":
		return "end"
	else:
		return "nope"

def Min(grille,profondeur):
	if state2(grille) == "end" or profondeur == 0:
		return evaluer(o,x,grille)
	minimum = 1000000
	possibles = tableaux_possibles(grille)
	
	for i in possibles:
		test = Max(i,profondeur -1)
		
		if test < minimum:
			minimum = test
			
	return minimum
		
def Max(grille,profondeur):
	if state2(grille) == "end" or profondeur == 0:
		return evaluer(o,x,grille)
	maximum = -1000000
	possibles = tableaux_possibles(grille)
	
	for i in possibles:
		test = Min(i,profondeur -1)
		
		if test > maximum:
			maximum = test
			
	return maximum

def IAplay(grille,profondeur):
	maximum = -100000
	
	possibles = tableaux_possibles(grille)
	
	for i in possibles:
		test = Min(i,profondeur-1)
		
		if test > maximum:
			maximum = test
			a_jouer = i	
	return a_jouer

def main():
	print evaluer(o,x,[[o,x,o],[e,e,e],[o,e,x]])
	#print poids(o,x,[[x,o,o],[e,o,x],[x,x,e]])
if __name__ == "__main__":
	main()
	
