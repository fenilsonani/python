class fenil:
    my="fenil"
    def __init__(self,name,surname):
        self.name=name;
        self.surname=surname;
    
    def printname(self):
        print(self.name,self.surname)

fe=fenil("Fenil",18)

fe.printname()



# method 2
class fenil:
    def printname(self,name,surname):
        print(name,surname)

fe=fenil()

fe.printname("fenil")