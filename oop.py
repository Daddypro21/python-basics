class Person():
    
    true_name = " Adama"
  
    def __init__(self, name,nick_name):
      self.name = name
      self.nick_name = nick_name
      
    def __str__(self) -> str:
    #  print( " Cette classe est une representation d'une personne")
        return " Bonjour je suis la classe Person , voici les param : {} ,{} et {}".format(self.name,self.nick_name, Person.true_name)

    def set_name(self, new_n):
        self.name = new_n

    def get_name(self):
        return self.name
    
x = Person( "Dav","Loa")
x.set_name(" Barack")
print(x.get_name())
print( x)