#imports
#from mod import *

#Inner Classes
class Equipment:
    def __init__(self, dmg, name, lvl):
        if lvl >= 1.1: 
            self.dmg = dmg * lvl / 2
        else:
            self.dmg = dmg
    def __repr__(self):
        return f"Equipment|name:{self.name} dmg:{self.dmg}, lvl:{self.lvl}"
        
class Player:
    def __init__(self, hp, lvl, equipment): 
        self.hp = hp
        self.lvl = lvl
        self.eq = equipment
    def AddEquipment(self, equipment):
        self.eq.append(equipment)
    def RemoveEquipment(self, equipment):
        self.eq.remove(equipment)
    
        

#Inner Functions
def preExecution():
    print("THIS IS PREEXECUTION")
#Main Function
def Main():
    preExecution()
    print("Hello World")



#Execution
if __name__ == "__main__":
    Main()
