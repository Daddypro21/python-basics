class Person():
      
    def __init__(self):
      print(" Person Created")
      
    def gender(self, g ="male"):
        self.g = g 
        return " this is the gender of this person : '{}' ".format(self.g)
    def name(self):
        return " A person has a name"
    
# x = Person( )
# print(x.gender())


#INHERITANCE

class Dav( Person):
    
    def __init__(self): 
        
        # Person.__init__(self)
        print (" Dev's birth")
        
    def name(self, dav_name = "default name") :
        self.dav_name = dav_name
        return " This is his name : ' {} ' ".format(self.dav_name)
    

# y = Dav()

# print(y)
# print(y.name( "Mady"))



#SPECIAL METHOD

class AmSpecial():
    
    def __init__(self , title = " I'm special", pages = [200,100,350 ], author =" Special Class"):
        
        self.title = title
        self.pages = pages 
        self.author = author
        
        print( " I'm very special as Class ")
        
    #normal method
    def are_you_special_as_method(self):
        return " Oh!no, i'm not a special method, i'm just normal"
    
    def simplify_things(self):
        
        i = 0
        while i < len(self.pages):
            i+=1    
            nb = self.pages[i]
            return nb 
    
    #special method
    def __str__(self) -> str:
        return " I'm special as method, i'm __str__ method ."

    def __len__(self):
        return self.simplify_things()
    
    def __del__(self):
        print(" asta la vista baby, i'm destroyed ....ha ha ah !")
    
special = AmSpecial()

print(len(special))

del special