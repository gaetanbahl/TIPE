##pickle avec l'arbre


from morpion import *
import pickle

file = open("arbre_dico_final", 'w')

pickle.dump(arbre_dico([[e,e,e],[e,e,e],[e,e,e]]),file)

file.close()
