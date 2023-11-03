#ERRORS AND EXCEPTIONS
# try , except and finally , and also else 

# example : print('hello) => you get a SyntaxError 

# try:
#     f = open('simple.pdf','w')
#     f.write(" Hey this is my texte")
# except IOError :
#     print ( " ERROR : COULD NOT FIND FILE OR READ DATA")

# else : 
#     print(" SUCCESS !")
#     f.close()
    
    
try:
    f = open('simple.pdf','r')
    f.write(" Hey this is my texte")
except IOError :
    print ( " ERROR : COULD NOT FIND FILE OR READ DATA")

finally : 
    print(" ALWAYS WORKS NO MATTER WHAT !")
    