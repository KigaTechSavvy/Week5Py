# Question 1

# Base class
class Superhero:
    def __init__(self, name, alias, power_level):
        self.name = name                  # Real name
        self.alias = alias                # Hero name
        self.power_level = power_level    # Power rating out of 100

    def display_info(self):
        print(f"{self.alias} ({self.name}) - Power Level: {self.power_level}")

    def use_power(self):
        print(f"{self.alias} uses their generic superpower!")

    def attack_ability(self):
        print(f"{self.name} performs a flying kick")

    def __str__(self):
        return f"Superhero: {self.name}" # Defines how the object is represented as a string when you use print() or str().


# Subclass 1 - FlyingHero (inherits from Superhero)
class FlyingHero(Superhero):
    def __init__(self, name, alias, power_level, flight_speed):
        super().__init__(name, alias, power_level)  # Call parent constructor
        self.flight_speed = flight_speed             # Additional attribute

    # Polymorphism: override use_power method
    def use_power(self):
        print(f"{self.alias} soars through the sky at {self.flight_speed} km/h!")

    

# Subclass 2 - StrengthHero (inherits from Superhero)
class StrengthHero(Superhero):
    def __init__(self, name, alias, power_level, max_lift):
        super().__init__(name, alias, power_level)
        self.max_lift = max_lift                     # Additional attribute

    def use_power(self):
        print(f"{self.alias} lifts {self.max_lift} tons with ease!")

    def attack_ability(self):
        print(f"{self.name} performs a devastating dive bomb attack!") # Polymorphism; Same method name, different behaviors


# Creating different players (hero objects)
hero1 = FlyingHero("Clark Kent", "Superman", 98, 2000)
hero2 = StrengthHero("Bruce Banner", "Hulk", 95, 100)
hero3 = Superhero("Peter Parker", "Spider-Man", 90)

# Display info and use powers (demonstrates polymorphism)

hero2.attack_ability()
hero1.attack_ability()

hero1.display_info()
hero1.use_power()

hero2.display_info()
hero2.use_power()

hero3.display_info()
hero3.use_power()

#Question 2

# Base class
class Vehicle:
    def move(self):
        print("The vehicle moves in its own way.")

# Subclass 1 - Car
class Car(Vehicle):
    def move(self):
        print("🚗 The car is driving on the road.")

# Subclass 2 - Plane
class Plane(Vehicle):
    def move(self):
        print("✈️ The plane is flying in the sky.")

# Subclass 3 - Boat
class Boat(Vehicle):
    def move(self):
        print("🚤 The boat is sailing across the water.")

# Create a list of different vehicle objects
vehicles = [Car(), Plane(), Boat()]

# Use polymorphism to call the move() method on each
for vehicle in vehicles:
    vehicle.move()
