#!/usr/bin/python -O
# -*- coding: iso-8859-1 -*-
## ici, fonction qui prend un tableau et qui vÃ©rifie l'Ã©tat de la partie (en cours, win, lose, draw)
#au morpion les ronds commencent, on part du principe que l'ordinateur joue les ronds, quitte Ã  changer f en moins f =)
#c'est un tableau de 3 tableaux de 3 lettres chacun
##TODO:PENSER A CHANGER LES STRINGS EN ENTIERS -> OPTIMISATION

def est_rempli(tableau):
  est_remplie = True
  for i in tableau:
    for j in i:
      if j == "":
  est_remplie = False
  return est_remplie

def state(tableau):
  a,b,c = tableau[0],tableau[1],tableau[2]
  state = ""
  victoire = False
  
  for i in range(3):
    if a[i] == b[i] and a[i] == c[i] and a[i] != "":
      state = str(a[i]) + " win"
      victoire = True
    
    if tableau[i][0] == tableau[i][1] and tableau[i][1] == tableau[i][2]  and tableau[i][0] != "":
      state = str(tableau[i][0]) + " win"     
      victoire = True
     
      
  
  if tableau[0][0] == tableau[1][1] and tableau[0][0] == tableau[2][2] and  tableau[0][0] != "":
    state = str(a[0]) + " win"
    victoire = True
  if tableau[0][2] == tableau[1][1] and tableau[1][1] == tableau[2][0] and  tableau[0][2] != "":
    state = str(a[2]) + " win"
    victoire = True
  
  if victoire == False:
    if est_rempli(tableau):
      state = "draw"
    else:
      state = "in progress"
    
  
  return state
  
x,o = "x","o"  
print state([[o,o,o],[o,o,o],[o,o,o]])
print state([[o,x,o],[x,x,o],[x,o,o]])
print state([[o,o,o],[x,o,x],[x,x,o]])
print state([[o,"",""],["","",""],["","",""]])
