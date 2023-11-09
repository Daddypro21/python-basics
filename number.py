import os 
from functions import *
from package.specialFunctions import *
# import math as mathematique
# from math import *
# var = 2
# var +=1
# print(var)
# majeur = True
# x = y = 3
# print( type(x)) # class int


# if majeur is not True :
#     print (" C'est bien juste")
# elif x < y :
#     print(" x est inferieur à y")
# else:
#     print( " x est égal à y")

# 

# maChaine = " Bonjour les amis"

# # for element in sequence

# for lettre in maChaine :
    
#     if lettre in " iuoaey":
#         print( lettre)
        
#     else:
#         print( " * ")
        

# def multiplication( nb1 , nb2):
#     while nb1 < 13 :
#         print( nb1 ," * ", nb2 ," = ", nb1 * nb2 )
#         nb1+=1
# nb2 = input( "inscrit ton nombre : ")
# nb2 = int(nb2)
# multiplication(0,nb2)    

#fonction lamba 


# f = lambda x , y: x * y
# result = f(5,20)
# print(result) 

# r = mathematique.sqrt(8)
# print(r)

# print(soustraction(2,3))
# print( multi(2,2)) 



# try:
#     annee = int(annee)
#     assert annee > 0 

# except ValueError:
#     print(" Vous n'avez pas saisis un nombre")
# except AssertionError :
#     print( " Le nombre doit être superieur à 0")
# else :
#     print(annee)
# try:    
#     if annee != int :
#         raise ValueError(" l'année doit être de type nombre ")
#     #lever une exception 
# except ValueError:
#     print( " Doit être de type nombre ")
    
 
#annee = input( " Saisissez une année superieur à 0: ")   

# list = ["mangue","banane","figue","ananas"]
# del list[0]
# print(list )

# info = input(" Entrez vos informations : ").split("-")
# print(info)  

dict = { "Paul":10 , "Sam":9 , "John":12 , "Alexa":14} 

for nom , note in dict.items():
    print( f" {nom} a eu {note}")
    
print(dict['Paul'])


os.system("pause") 

