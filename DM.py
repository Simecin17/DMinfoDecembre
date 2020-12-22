//Thomas Boulanger et Siméon Boyer  PSI*1


import math
import numpy as np
import random

// N particules de masse m, rayon R, dans un récipient linéique, carré ou cubique de coté L

//Q1 : p est tableau de numpy de dimension 1 à une case contenant un flottant compris entre 0 et L.
//Q2 : c est un tableau de numpy définit comme argument de la fonction possible.
//Q3 : la première case du tableau c est comparé aux bords du récipient pour voir si il n entre pas
//en contacte avec les parois, si il y a contact, la position n est pas possible, on return False
//Q4 : on compare ensuite la position de la boule c avec toutes les autres boules pour voir si il
//n y a pas de collisions entres elles, si il y en a une, on return False, sinon on return True
//Q5 : la fonction possible vérifie qu il est possible de placer une particule sur la position c 
//Q6 : p = R + (L-2*R)* np.random.rand(1)         avec cette version, il n y a pas de collision
// possible avec les bords
//Q7 : la fonction possible revera toujours Fasle, car il est impossible deplacer une 4 ème 
// particule, la fonction va donc être bloquer dans une boucle while.
//Q8 : C = 1 + N * (2 + (2 + N*2 + 1) + 1) + 1 = 2N² +6N +2 = O(N²)
//Q9 : 
res=[]
while len(res)<N:
    p = R + (L-2*R)* np.random.rand(1)
    if possible(p): res.append(p)
    else : res=[]
return res
//Q10 : 
def placement1Drapide(N,R,L):
    l= L-N*2*R
    
                         
