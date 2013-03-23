#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
#  stats.py
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


from morpion import *




def quiwinplus(arbre): #(77904, 131184, 46080) au total 255168 parties possibles sur 363880 grilles complètes possibles
  compteurwinx, compteurwino,compteurdraw = 0,0,0
	if isinstance(arbre["subtree"],str):
		if arbre["subtree"] == "o win":
			compteurwino += 1
		elif arbre["subtree"] == "x win":
			compteurwinx += 1
		elif arbre["subtree"] == "draw":
			compteurdraw += 1
	else:
		for i in arbre["subtree"]:
			ixe, oh, dro = quiwinplus(i)
			compteurwinx += ixe
			compteurwino += oh
			compteurdraw += dro
	
	return compteurwinx,compteurwino,compteurdraw


def main():
	x, o , e = 'x', 'o', '_'
	grille = [[e,e,e],[e,e,e],[e,e,e]]
	arbre = arbre_dico(grille)
	print quiwinplus(arbre)

if __name__ == "__main__":
	main()
