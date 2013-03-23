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

from minmax import *
from morpion import *
import sys

e = "_" 
o = 'o'
x = 'x'
player = x
grille_vide = [[e,e,e],[e,e,e],[e,e,e]]

def verifier_jouable(grille,coup):
  for i in coup:
		if range(3).count(int(i)) == 0:
			return False
	
	if grille[int(coup[0])][int(coup[1])] == e:
		return True
	else:
		return False

def thegame(args):
	print "Vous allez jouer au morpion contre l'IA de GaÃ©tan Bahl et Quentin Adam, \nbasÃ©e sur l'algorithme Min-Max. \n"
	print "Lorsque ce sera Ã  votre tour de jouer, vous entrerez les coordonnÃ©es de votre coup sÃ©parÃ©es par un espace"
	print "GLHF"
	grille = grille_vide
	
	while state2(grille) != "end":
		print representation(grille)
		print "\n l'IA joue..."
		grille = IAplay(grille, args[1])
		if state2(grille) == "end":
			break
		print representation(grille)
		coup = False
		while coup == False:
			banana = raw_input("\n Que jouez vous ? (ligne colonne) \n")
			coord = banana.split()
			coup = verifier_jouable(grille,coord)
			if coup == False:
				print "\n coup invalide, retry \n"
		grille[int(coord[0])][int(coord[1])] = player
			
	print "\n" + etat_jeu(state(grille)) + "\n"
	print representation(grille)

def etat_jeu(state):
	if state == "o win":
		return "PERDU"
	elif state == "x win":
		return "GAGNÉ"
	elif state == "draw":
		return "ÉGALITÉ"


if __name__ == "__main__":
	thegame(sys.argv) 
