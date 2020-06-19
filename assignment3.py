#Parent Class Wizard
class Wizard:
    def __init__(self, first_name, last_name, house,
                 region):
        self.first_name = first_name
        self.last_name = last_name
        self.house = house
        self.region = region

    def channelMana(self):
        print("As you meditate the earth's energies concentrate into your being")
            


#Child Class Fire Mage
class Fire_Mage(Wizard):
    class_level = 10
    alignment = 'neutral'
    
    def fireball(self):
        print("A giant fireball shoots from your wand")

# This is the same method in the parent class "Wizard".
# This mana channelization is specific to the Fire Mage 

    def channelMana(self):
        print("As you meditate the energies from earth's volcanos and fires concentrate into your being")



#Child Class Ice Mage
class Ice_Mage(Wizard):
    class_level = 20
    alignment = 'good'

    def iceCannon(self):
        print("A giant sheet of ice shoots from your wand")

# This is the same method in the parent class "Wizard".
# This mana channelization is specific to the Ice Mage.

    def channelMana(Self):
        print("As you medidate the energies from the earth's glaciers and snow concentrate into your being")


merlin = Wizard("Myrddin", "Wyllt", "None", "Caledonian Forest")
print(merlin.first_name + " " + merlin.last_name)
print("House: " + merlin.house)
print("Region: " + merlin.region)
merlin.channelMana()

print(" ")

chandra = Fire_Mage("Chandra", "Nalaar", "Gatewatch", "Kaladesh")
print(chandra.first_name + " " + chandra.last_name)
print("House: " + chandra.house)
print("Region: " + chandra.region)
chandra.channelMana()
chandra.fireball()

print(" ")

cohlien = Ice_Mage("Cohlien", "Frostweaver", "Sons of Lothar", "Netherstorm")
print(cohlien.first_name + " " + cohlien.last_name)
print("House: " + cohlien.house)
print("Region: " + cohlien.region)
cohlien.channelMana()
cohlien.iceCannon()



