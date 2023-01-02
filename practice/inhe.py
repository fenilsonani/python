class Person:
    def __init__(self,name,surname) :
        self.name=name;
        self.surname=surname;
    
    def printdetail(self):
        print("Your name : ",self.name," Your Surname : ",self.surname)

class Extended(Person):
    pass

pe=Extended("Fenil","Sonani")

pe.printdetail()