Activity_1
class Superhero:
    def __init__(self, name, power, strength):
        self.name = name
        self.power = power
        self.__strength = strength 

    def display_info(self):
        print(f"{self.name} has the power of {self.power}.")

    def get_strength(self): 
        return self.__strength

    def set_strength(self, new_strength):
        if new_strength > 0:
            self.__strength = new_strength
        else: 
            print("Strength must be positive.")

hero1 = Superhero("Superman ", "Flight", 35)
hero1.display_info()
print("strength:", hero1.get_strength())

hero2 = Superhero("Batman", "Intelligence", 25)
hero2.display_info()

Activity_2
class vehicle:
    def move(self):
        print("The vehicle is moving.")

class car(vehicle):
    def move(self):
        print("driving")

class plane(vehicle):
    def move(flying):
        print("flying")
    
class boat(vehicle):
    def move(self):
        print("sailing")

vehilce =[car(), plane(), boat()]

for v in vehicles:
    v.move
