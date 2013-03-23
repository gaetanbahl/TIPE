import pygame
from morpion import *

from pygame.locals import *
 
#constantes
x, o , e = 'x', 'o', '_'
echelle = 0.34
echelle_titre = 0.6
resx = 800
resy = 480 
compteur_redbox = 0
continuer = 1
grille_current = [[e,e,e],[e,e,e],[e,e,e]]
grille_before = [[e,e,e],[e,e,e],[e,e,e]]
espacement = 13
#initialisation
pygame.init()
LM = pygame.font.match_font('Sans')
font = pygame.font.Font(LM, 36)
font2 = pygame.font.Font(LM, 50)
fenetre = pygame.display.set_mode((resx, resy))
pygame.display.set_caption('Explorateur d\'arbre')
fond = pygame.transform.scale(pygame.image.load("fond.png").convert(),(resx,resy))
surflignes = pygame.transform.scale(pygame.image.load("transparent.png").convert_alpha(),(resx,resy))
surflignesmod = surflignes
grille_vide = pygame.image.load("tic_tac_toe.png").convert_alpha()
croix = pygame.image.load("croix.png").convert_alpha()
titre = font2.render("Arbre du morpion", 1, (10, 10, 10))
pos = titre.get_rect()
pos.centerx = fond.get_rect().centerx
pos.centery = 50


rond = pygame.image.load("rond.png").convert_alpha()
redbox = pygame.transform.smoothscale(pygame.image.load("redbox.png").convert_alpha(),(int(echelle*220),int(echelle*220)))
pygame.display.flip()
fenetre.blit(fond, (0,0)) 

#definition des fonctions

def afficher_grille (grille,x,y):
  ps = 73*echelle
	grille_vide = pygame.image.load("tic_tac_toe.png").convert_alpha()
	
	taillegrille = grille_vide.get_size()
	grilleres = pygame.transform.smoothscale(grille_vide,(int(taillegrille[0]*echelle),int(taillegrille[1]*echelle)))
	fenetre.blit(grilleres,(x,y))
	taille = croix.get_size()
	croixres = pygame.transform.scale(croix,(int(taille[0]*echelle),int(taille[1]*echelle)))
	rondres = pygame.transform.scale(rond,(int(taille[0]*echelle),int(taille[1]*echelle)))
	liste = []
	for i in range(3):
		for j in range(3):
			if grille[j][i] == "x":
				fenetre.blit(croixres,((x+i*ps) -2,(y+j*ps)))
			elif grille[j][i] == "o":
				fenetre.blit(rondres,((x+i*ps) -2,(y+j*ps)))
			
def afficher_liste_grilles(liste,coord,espacement):
	x,y = coord
	largeur = (grille_vide.get_size())[0]*echelle
	compt=0
	for i in liste:
		afficher_grille(i,x+compt*(largeur + espacement),y)
		pygame.draw.aaline(surflignesmod,(0,0,0), (resx/2, 200), ((x+compt*(largeur + espacement)+ echelle*220/2), y -20 ))
		if compt == compteur_redbox:
			fenetre.blit(redbox,(x+compt*(largeur + espacement),y))
		compt += 1
	

#boucle d'affichage
afficher_grille(grille_current,resx/2 - 220*echelle/2,120 )
possibles = tableaux_possibles(grille_current)
afficher_liste_grilles(possibles, (10,380), espacement)
liste_grilles = []

while continuer:
	for event in pygame.event.get():   
		if event.type == QUIT:
			continuer = 0
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE: #sert juste a quitter sans cliquer sur la croix
				continuer = 0
			if event.key == K_DOWN: #on passe a la grille designee par la redbox
				surflignesmod = pygame.transform.scale(pygame.image.load("transparent.png").convert_alpha(),(resx,resy))
				fenetre.blit(fond, (0,0)) 
				grille_before = grille_current
				liste_grilles.append(grille_current)
				grille_current = possibles[compteur_redbox]
				
				afficher_grille(grille_current,resx/2 - 220*echelle/2,120 )
				compteur_redbox = 0
				etat = state(grille_current)
				if etat == "in progress":
					possibles = tableaux_possibles(grille_current)
					afficher_liste_grilles(possibles, (10,380), espacement)
				else:
					texte = font.render(etat, 1, (10, 10, 10))
					textpos = texte.get_rect()
					textpos.centerx = fond.get_rect().centerx
					textpos.centery = 320
					fenetre.blit(texte, textpos)
					
				
				
				
			if event.key == K_RIGHT and compteur_redbox < (len(possibles) -1 ): #on change la redbox de place
				compteur_redbox += 1
				fenetre.blit(fond, (0,0))
				afficher_grille(grille_current,resx/2 - 220*echelle/2,120 )
				afficher_liste_grilles(possibles, (10,380), espacement)
				
			if event.key == K_LEFT and compteur_redbox > 0: #on change la redbox de place
				compteur_redbox -= 1
				fenetre.blit(fond, (0,0))
				afficher_grille(grille_current,resx/2 - 220*echelle/2,120 )
				afficher_liste_grilles(possibles, (10,380), espacement)
			
			if event.key == K_UP and liste_grilles != []: #pour remonter dans l'arbre
				surflignesmod = pygame.transform.scale(pygame.image.load("transparent.png").convert_alpha(),(resx,resy))
				fenetre.blit(fond, (0,0)) 
				grille_current = liste_grilles[-1]
				liste_grilles.pop()
				possibles = tableaux_possibles(grille_current)
				afficher_grille(grille_current,resx/2 - 220*echelle/2,120 )
				compteur_redbox = 0
				afficher_liste_grilles(possibles, (10,380), espacement)
	
	fenetre.blit(titre,pos)
	fenetre.blit(surflignesmod, (0,0))
	pygame.display.flip()
