# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 16:59:15 2023

@author: eliot
"""
import numpy as np
from colorama import init, Fore, Back, Style
import time
import math
import copy
INFPOS = float("inf")
INFNEG = -float("inf")
class plateauMorpion:
    #initialise juste un plateau vide 
    def __init__(self):
        self.plateau = np.zeros((3,3))
    #renvoie si le morpion est fini
    def fini(self):
        rep = False
        somme1 = 0
        somme2 = 0
        for i in range(3):
            if abs(sum(self.plateau[i]))==3 or abs(sum(self.plateau[:,i]))==3:
                rep = True
            somme1 += self.plateau[i,i]
            somme2 += self.plateau[i,2-i]
        
        if abs(somme1)==3 or abs(somme2)==3:
            rep = True
        if not rep and np.count_nonzero(self.plateau == 0) == 0:
            
            rep = True
        
        
        return rep
    
    def Action(self,pos):
        liste = []
        for i in range(3):
            for j in range(3):
                if self.plateau[i,j] == 0:
                   
                    liste.append([i+pos[0]*3,j+pos[1]*3])
        return liste
    def egalite(self):
        rep = False
        if not rep and np.count_nonzero(self.plateau == 0) == 0:
            
            rep = True
        return rep
    def vainqueur(self):
        rep = 0
        somme1=0
        somme2=0
        for i in range(3):
            if all(elem == 1 for elem in self.plateau[i]) or all(elem == 1 for elem in self.plateau[:,i]):
                rep = 1
            if all(elem == -1 for elem in self.plateau[i]) or all(elem == -1 for elem in self.plateau[:,i]):
                rep =-1
            somme1 += self.plateau[i,i]
            somme2 += self.plateau[i,2-i]
            
        if somme1==3 or somme2 == 3:
            rep = 1
        if somme1== -3 or somme2 == -3:
            rep = -1
        

        return rep
    def afficherElement(self,x,y):
        rep = " "
        if  self.plateau[x,y]== 1:
            rep = "X"
        elif self.plateau[x,y] == -1:
            rep = "O"
        return rep
    
    
    def heuristique3(self, joueurmax):
        evaluation = 0
        points = np.array([[0.2, 0.17, 0.2], [0.17, 0.22, 0.17], [0.2, 0.17, 0.2]])
        for i in range(3):
            for j in range(3):
                evaluation += self.plateau[i,j]*points[i,j]*joueurmax
                
            a= 2
            #check s'il y a deux x ou O sur une ligne 
                
            if(self.plateau[0,0] + self.plateau[0,1] + self.plateau[0,2] == a*joueurmax or self.plateau[1,0] + self.plateau[1,1] + self.plateau[1,2] == a*joueurmax or self.plateau[0,0] + self.plateau[0,1] + self.plateau[0,2] == a*joueurmax):
                evaluation += 6
                
            if(self.plateau[0,0] + self.plateau[0,1] + self.plateau[0,2] == -a*joueurmax or self.plateau[1,0] + self.plateau[1,1] + self.plateau[1,2] == -a*joueurmax or self.plateau[0,0] + self.plateau[0,1] + self.plateau[0,2] == -a*joueurmax):
                evaluation -= 6
                    
            #check s'il y a deux x ou O sur une colonne
                
            if(self.plateau[0,0] + self.plateau[1,0] + self.plateau[2,0] == a*joueurmax or self.plateau[0,1] + self.plateau[1,1] + self.plateau[2,1] == a*joueurmax or self.plateau[0,2] + self.plateau[1,2] + self.plateau[2,2] == a*joueurmax):
                evaluation += 6
                
            if(self.plateau[0,0] + self.plateau[1,0] + self.plateau[2,0] == -a*joueurmax or self.plateau[0,1] + self.plateau[1,1] + self.plateau[2,1] == -a*joueurmax or self.plateau[0,2] + self.plateau[1,2] + self.plateau[2,2] == -a*joueurmax):
                evaluation -= 6
                    
            #check s'il y a deux x ou O sur une diagonale
                
            if(self.plateau[0,0] + self.plateau[1,1] + self.plateau[2,2] == a*joueurmax or self.plateau[0,2] + self.plateau[1,1] + self.plateau[0,2] == a*joueurmax ):
                evaluation += 7
                
            if(self.plateau[0,0] + self.plateau[1,1] + self.plateau[2,2] == -a*joueurmax or self.plateau[0,2] + self.plateau[1,1] + self.plateau[0,2] == -a*joueurmax ):
                evaluation -= 7
                    
                    
            #check si une ligne ou une colonne a été bloquée
                
            a = -1
                
            if((self.plateau[0,0] + self.plateau[0,1] == 2*a*joueurmax and self.plateau[0,2]==-a*joueurmax) or (self.plateau[0,2] + self.plateau[0,1] == 2*a*joueurmax and self.plateau[0,0]==-a*joueurmax) or (self.plateau[0,0] + self.plateau[0,2] == 2*a*joueurmax and self.plateau[0,1]==-a*joueurmax) or (self.plateau[1,0] + self.plateau[1,1] == 2*a*joueurmax and self.plateau[1,2]==-a*joueurmax) or (self.plateau[1,2] + self.plateau[1,1] == 2*a*joueurmax and self.plateau[1,0]==-a*joueurmax) or (self.plateau[1,0] + self.plateau[1,2] == 2*a*joueurmax and self.plateau[1,1]==-a*joueurmax) or (self.plateau[2,0] + self.plateau[2,1] == 2*a*joueurmax and self.plateau[2,2]==-a*joueurmax) or (self.plateau[2,2] + self.plateau[2,1] == 2*a*joueurmax and self.plateau[2,0]==-a*joueurmax) or (self.plateau[2,0] + self.plateau[2,2] == 2*a*joueurmax and self.plateau[2,1]==-a*joueurmax) or (self.plateau[0,0] + self.plateau[1,0] == 2*a*joueurmax and self.plateau[2,0]==-a*joueurmax) or (self.plateau[2,0] + self.plateau[1,0] == 2*a*joueurmax and self.plateau[0,0]==-a*joueurmax) or (self.plateau[0,0] + self.plateau[2,0] == 2*a*joueurmax and self.plateau[1,0]==-a*joueurmax) or (self.plateau[0,1] + self.plateau[1,1] == 2*a*joueurmax and self.plateau[2,1]==-a*joueurmax) or (self.plateau[2,1] + self.plateau[1,1] == 2*a*joueurmax and self.plateau[0,1]==-a*joueurmax) or (self.plateau[0,1] + self.plateau[2,1] == 2*a*joueurmax and self.plateau[1,1]==-a*joueurmax) or (self.plateau[0,2] + self.plateau[1,2] == 2*a*joueurmax and self.plateau[2,2]==-a*joueurmax) or (self.plateau[2,2] + self.plateau[1,2] == 2*a*joueurmax and self.plateau[0,2]==-a*joueurmax) or (self.plateau[0,2] + self.plateau[2,2] == 2*a*joueurmax and self.plateau[1,2]==-a*joueurmax) or (self.plateau[2,2] + self.plateau[1,1] == 2*a*joueurmax and self.plateau[0,0]==-a*joueurmax) or (self.plateau[0,0] + self.plateau[1,1] == 2*a*joueurmax and self.plateau[2,2]==-a*joueurmax) or (self.plateau[2,2] + self.plateau[0,0] == 2*a*joueurmax and self.plateau[1,1]==-a*joueurmax) or (self.plateau[2,0] + self.plateau[1,1] == 2*a*joueurmax and self.plateau[0,2]==-a*joueurmax) or (self.plateau[0,2] + self.plateau[1,1] == 2*a*joueurmax and self.plateau[2,0]==-a*joueurmax) or (self.plateau[2,0] + self.plateau[0,2] == 2*a*joueurmax and self.plateau[1,1]==-a*joueurmax)):
                evaluation += 9
            
            a = 1
                
            if((self.plateau[0,0] + self.plateau[0,1] == 2*a*joueurmax and self.plateau[0,2]==-a*joueurmax) or (self.plateau[0,2] + self.plateau[0,1] == 2*a*joueurmax and self.plateau[0,0]==-a*joueurmax) or (self.plateau[0,0] + self.plateau[0,2] == 2*a*joueurmax and self.plateau[0,1]==-a*joueurmax) or (self.plateau[1,0] + self.plateau[1,1] == 2*a*joueurmax and self.plateau[1,2]==-a*joueurmax) or (self.plateau[1,2] + self.plateau[1,1] == 2*a*joueurmax and self.plateau[1,0]==-a*joueurmax) or (self.plateau[1,0] + self.plateau[1,2] == 2*a*joueurmax and self.plateau[1,1]==-a*joueurmax) or (self.plateau[2,0] + self.plateau[2,1] == 2*a*joueurmax and self.plateau[2,2]==-a*joueurmax) or (self.plateau[2,2] + self.plateau[2,1] == 2*a*joueurmax and self.plateau[2,0]==-a*joueurmax) or (self.plateau[2,0] + self.plateau[2,2] == 2*a*joueurmax and self.plateau[2,1]==-a*joueurmax) or (self.plateau[0,0] + self.plateau[1,0] == 2*a*joueurmax and self.plateau[2,0]==-a*joueurmax) or (self.plateau[2,0] + self.plateau[1,0] == 2*a*joueurmax and self.plateau[0,0]==-a*joueurmax) or (self.plateau[0,0] + self.plateau[2,0] == 2*a*joueurmax and self.plateau[1,0]==-a*joueurmax) or (self.plateau[0,1] + self.plateau[1,1] == 2*a*joueurmax and self.plateau[2,1]==-a*joueurmax) or (self.plateau[2,1] + self.plateau[1,1] == 2*a*joueurmax and self.plateau[0,1]==-a*joueurmax) or (self.plateau[0,1] + self.plateau[2,1] == 2*a*joueurmax and self.plateau[1,1]==-a*joueurmax) or (self.plateau[0,2] + self.plateau[1,2] == 2*a*joueurmax and self.plateau[2,2]==-a*joueurmax) or (self.plateau[2,2] + self.plateau[1,2] == 2*a*joueurmax and self.plateau[0,2]==-a*joueurmax) or (self.plateau[0,2] + self.plateau[2,2] == 2*a*joueurmax and self.plateau[1,2]==-a*joueurmax) or (self.plateau[2,2] + self.plateau[1,1] == 2*a*joueurmax and self.plateau[0,0]==-a*joueurmax) or (self.plateau[0,0] + self.plateau[1,1] == 2*a*joueurmax and self.plateau[2,2]==-a*joueurmax) or (self.plateau[2,2] + self.plateau[0,0] == 2*a*joueurmax and self.plateau[1,1]==-a*joueurmax) or (self.plateau[2,0] + self.plateau[1,1] == 2*a*joueurmax and self.plateau[0,2]==-a*joueurmax) or (self.plateau[0,2] + self.plateau[1,1] == 2*a*joueurmax and self.plateau[2,0]==-a*joueurmax) or (self.plateau[2,0] + self.plateau[0,2] == 2*a*joueurmax and self.plateau[1,1]==-a*joueurmax)):
                evaluation -= 9
                
            if self.fini():
                evaluation += self.vainqueur()*joueurmax*12
            return evaluation
                
                
                
                    
                    
        
        
    
    
        

class sousPlateau(plateauMorpion):
    def __init__(self,position : list):
        plateauMorpion.__init__(self)
        self.focus = True
        self.jouable = True
        self.positionIndexLigne : int = position[0]
        self.positionIndexColonne : int = position[1]
        

class grandPlateau(plateauMorpion):
    def __init__(self):
        plateauMorpion.__init__(self)
        self.sousPlateaux = np.array([[sousPlateau([0,0]),sousPlateau([0,1]),sousPlateau([0,2])],[sousPlateau([1,0]),sousPlateau([1,1]),sousPlateau([1,2])],[sousPlateau([3,0]),sousPlateau([3,1]),sousPlateau([3,2])]])
    
    def afficherPlateau(self,a):
        s = np.zeros((9,9))
        for i in range(3):
            for j in range(3):
                s[i*3:(i+1)*3,j*3:(j+1)*3]= self.sousPlateaux[i,j].plateau
        afficherTableau(s,a)
        print("")
        afficherTableau1(self.plateau)
        
        
    def MarquerSousPlateau(self, sousPlateau, joueur):
        ligne = self.sousPlateaux.positionIndexLigne
        colonne = self.sousPlateaux.positionIndexLigne
        self.plateau[ligne,colonne] =  joueur
    
    def MajFocus(self, action):
        #Plateaufocus = self.sousPlateaux[action[0],action[1]]
        
        if self.sousPlateaux[action[0],action[1]].jouable:
            for i in range(3):
                for j in range(3):
                    self.sousPlateaux[i,j].focus = False
            self.sousPlateaux[action[0],action[1]].focus = True
            
        else:
            for i in range(3):
                for j in range(3):
                    self.sousPlateaux[i,j].focus = self.sousPlateaux[i,j].jouable
    def GetPlateau(self):
        s = np.zeros((9,9))
        for i in range(3):
            for j in range(3):
                s[i*3:(i+1)*3,j*3:(j+1)*3]= self.sousPlateaux[i,j].plateau
        return s
    
    def Result(self,a,joueur):
        
        action3 = [a[0]//3,a[1]//3]
        self.sousPlateaux[action3[0],action3[1]].plateau[a[0]%3,a[1]%3] = joueur
        if self.sousPlateaux[action3[0],action3[1]].fini():
            #print("check")
            self.plateau[action3[0],action3[1]]= self.sousPlateaux[action3[0],action3[1]].vainqueur()
           # print(self.sousPlateaux[action3[0],action3[1]])
            self.sousPlateaux[action3[0],action3[1]].jouable = False
        self.MajFocus([a[0]%3,a[1]%3]) 
    
    def Result1(self,a,joueur):
        jeu = copy.deepcopy(self)
        action3 = [a[0]//3,a[1]//3]
        jeu.sousPlateaux[action3[0],action3[1]].plateau[a[0]%3,a[1]%3] = joueur
        if jeu.sousPlateaux[action3[0],action3[1]].fini():
           
            jeu.plateau[action3[0],action3[1]]= jeu.sousPlateaux[action3[0],action3[1]].vainqueur()
           
            jeu.sousPlateaux[action3[0],action3[1]].jouable = False
        jeu.MajFocus([a[0]%3,a[1]%3]) 
        return jeu
        
    def Actions(self):
        liste = []
        for i in range(3):
            for j in range(3):
                if self.sousPlateaux[i,j].focus == True:
                    liste += self.sousPlateaux[i,j].Action([i,j])
        return liste
        
        
    
    def get_move(self):
        while True:
            try:
                row = int(input("Entrez la ligne: "))-1
                col = int(input("Entrez la colonne: "))-1
                if 0 <= row <= 8 and 0 <= col <= 8 and self.sousPlateaux[row//3,col//3].plateau[row%3,col%3]==0 and self.sousPlateaux[row//3,col//3].focus:
                    return [row, col]
                else:
                    print("Action invalide, veuillez réessayer.")
            except ValueError:
                print("Entrée invalide, veuillez réessayer.")
    def get_move1(self):
        while True:
            try:
                morpion = int(input("Entrez morpion: "))-1
                case = int(input("Entrez la case: "))-1
                row = morpion//3 +case//3
                col = case%3 + morpion%3
                if 0 <= row <= 8 and 0 <= col <= 8 and self.sousPlateaux[row//3,col//3].plateau[row%3,col%3]==0 and self.sousPlateaux[row//3,col//3].focus:
                    return [row, col]
                else:
                    print("Action invalide, veuillez réessayer.")
            except ValueError:
                print("Entrée invalide, veuillez réessayer.")
                
    def printFocus(self):
        for i in range(3):
            for j in range(3):
                print(self.sousPlateaux[i,j].focus)
                
                
    def printJouable(self):
        for i in range(3):
            for j in range(3):
                print(self.sousPlateaux[i,j].jouable)
    #il faut fournir quel joueur incarne l'ia
    def utility(self,joueuria):
        s= self.plateau
        rep = 0
        somme1=0
        somme2=0
        for i in range(3):
            if all(elem == -joueuria for elem in s[i]) or all(elem == -joueuria for elem in s[:,i]):
                rep = -1000000
            if all(elem == joueuria for elem in s[i]) or all(elem == joueuria for elem in s[:,i]):
                rep = 1000000
            somme1 += s[i,i]
            somme2 += s[i,2-i]
            
        if somme1==3*(-joueuria) or somme2 == 3*(-joueuria):
            rep = -1000000
        if somme1== 3*joueuria or somme2 == 3*joueuria:
            rep = 1000000
        if rep == None and np.count_nonzero(s == 0) == 0:
            rep = 0

        return rep
    
    def heuristique9(self,joueur):
        evaluation1 = 0
        points1 = np.array([[1.4, 1, 1.4],[ 1, 1.75, 1],[ 1.4, 1, 1.4]])
        
        for i in range(3):
            for j in range(3):
                evaluation1 += self.sousPlateaux[i,j].heuristique3(joueur)*1.5*points1[i,j]
                if self.sousPlateaux[i,j].focus:
                    evaluation1 += self.sousPlateaux[i,j].heuristique3(joueur)*points1[i,j]
                    
        evaluation1 += self.heuristique3(joueur)*150
        evaluation1 += self.utility(joueur)
        return evaluation1
    
    
        
                
        
        
    
        

def afficherTableau(s,a):
    couleur = Fore.GREEN
    print("    1   2   3   4   5   6   7   8   9")
    print(couleur + "   ------------------------------------"+Fore.RESET)
    for i in range(9):
        print (str(i+1) + couleur + " | "+ Fore.RESET,end="")
        for j in range(9):
            print(afficherCase(s[i,j]) if [i,j] != a else Fore.RED + afficherCase(s[i,j]) + Fore.RESET, end = "") 
            print(" | " if (j+1)%3 != 0 else couleur + " | " + Fore.RESET,end = "")
            
        print("")
        print("   ------------------------------------" if (i+1)%3 != 0 else couleur + "   ------------------------------------" +Fore.RESET)
        
def afficherTableau1(s):
    
    print("    1   2   3")
    print("  -------------")
    for i in range(3):
        print (str(i+1) + " | ",end="")
        for j in range(3):
            print(afficherCase(s[i,j]),end = "")
            print(" | ",end ="")
        print("")
        print("  -------------")

        
        
def afficherCase(case):
    rep = " "
    if case == 1:
        rep = "X"
    elif case == -1:
        rep = "O"
    return rep
 
def get_move(s):
    while True:
        try:
            
            row = int(input("Entrez la ligne: "))
            col = int(input("Entrez la colonne: "))
            if 0 <= row <= 8 and 0 <= col <= 8 and s[row, col] == 0:
                return [row, col]
            else:
                print("Action invalide, veuillez réessayer.")
        except ValueError:
            print("Entrée invalide, veuillez réessayer.")

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        print("La fonction {} a pris {} secondes pour s'exécuter".format(func.__name__, end_time - start_time))
        
        return result
    return wrapper

@timer
def Min_Max_Decision(jeu,profondeurMax,joueur):
    t1= time.time()
    profondeur = 0
    actions=jeu.Actions()
    listeutilities=[Min_Value(jeu.Result1(a,joueur), INFNEG,INFPOS,joueur,profondeur,profondeurMax,t1) for a in actions]
    rep = np.argsort(listeutilities)
    return actions[rep[-1]],time.time()-t1

def Max_Value(jeu,alpha,beta,joueur,profondeur1,profondeurmax,t1):
    profondeur = profondeur1
    profondeur += 1
    v=INFNEG
    
    if jeu.fini():
        return jeu.utility(joueur)
    
    elif profondeur==profondeurmax or time.time()-t1>9.8:
        return jeu.heuristique9(joueur)
    
    
    else:
        for a in jeu.Actions():
            v  = max(v,Min_Value(jeu.Result1(a,joueur),alpha,beta,joueur,profondeur,profondeurmax,t1))
            if v >= beta:
                return v
            alpha = max(alpha,v)

        return v
def Min_Value(jeu,alpha,beta,joueur,profondeur1,profondeurmax,t1): 
  
    profondeur = profondeur1
    profondeur += 1
    v =  INFPOS
   
    if jeu.fini():
        return jeu.utility(joueur)
    
    elif profondeur==profondeurmax or time.time()-t1>9.8:
        return jeu.heuristique9(joueur)
    
    else:
        for a in jeu.Actions():
            v=min(v,Max_Value(jeu.Result1(a,-joueur),alpha,beta,joueur,profondeur,profondeurmax,t1))
            if v <= alpha:
                return v
            beta = min(beta,v)
        return v















#commence: si le joueur commence
#joueur 1 pour x, -1 pour O
#ia: true s'il y a une ia, false pour pvp
def Partie(commence : bool, joueur : int, ia : bool, profondeur: int):
    jeu = grandPlateau()
    action=[0,0]
    if commence:
        jeu.afficherPlateau(action)
        action = jeu.get_move()
        jeu.Result(action, joueur)
    if not ia:
        
        while True:
    
        
            jeu.afficherPlateau(action)
            action = jeu.get_move()
            jeu.Result(action, -joueur)
            if jeu.fini():
                jeu.afficherPlateau(action)
                if jeu.vainqueur()==1:
                    print("X gagne")
                elif jeu.vainqueur()==-1:
                    print("O gagne")
                elif jeu.vainqueur()==0:
                    print("égalité")
                else: 
                    print("erreur")
                break
            print(jeu.Actions())
            
                    
            jeu.afficherPlateau(action)
            action = jeu.get_move()
            jeu.Result(action, joueur)
            if jeu.fini():
                jeu.afficherPlateau(action)
                if jeu.vainqueur()==1:
                    print("X gagne")
                elif jeu.vainqueur()==-1:
                    print("O gagne")
                elif jeu.vainqueur()==0:
                    print("égalité")
                else: 
                    print("erreur")
                break
            print(jeu.Actions())
    else:
        if not commence:            
            jeu.Result([4,4], -joueur)
            jeu.afficherPlateau(action)
            action = jeu.get_move()
            jeu.Result(action, joueur)
            
                
                
        liste_temps = [0]
        while True:
            
            
            action,temps  = Min_Max_Decision(jeu, profondeur, -joueur)
            liste_temps.append(temps)
            jeu.Result(action, -joueur)
            if jeu.fini():
                jeu.afficherPlateau(action)
                if jeu.vainqueur()==1:
                    print("X gagne")
                elif jeu.vainqueur()==-1:
                    print("O gagne")
                elif jeu.vainqueur()==0:
                    print("égalité")
                else: 
                    print("erreur")
                print(np.mean(liste_temps))
                break
            jeu.afficherPlateau(action)
            action = jeu.get_move()
            jeu.Result(action, joueur)
            if jeu.fini():
                jeu.afficherPlateau(action)
                if jeu.vainqueur()==1:
                    print("X gagne")
                elif jeu.vainqueur()==-1:
                    print("O gagne")
                elif jeu.vainqueur()==0:
                    print("égalité")
                else: 
                    print("erreur")
                print(np.mean(liste_temps))
                break
        
        
        
            
        
        

        
        
    
        