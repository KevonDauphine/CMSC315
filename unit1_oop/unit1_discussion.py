"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class Weapon:
    weapon_type = "Melee"
    def __init__(self, name: str, cost: int, damage:int, rarity: str):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.rarity = rarity

    def display_stats(self):
        return f"Weapon: {self.name}, Cost of weapon: {self.cost}, Damage {self.damage}, Rarity {self.rarity}"

# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class RangedWeapon(Weapon):

    weapon_type = "Ranged"
    gun_type = "Standard"

    def __init__(self, name: str, cost: int, damage: int, rarity: str, ammo_type: str, mag_size: int, fire_rate: float):
        super().__init__(name, cost, damage, rarity)
        self.ammo = ammo_type
        self.mag_size = mag_size
        self.fire_rate = fire_rate
        self.attachments = []

    def display_stats(self):

        return (super().display_stats() + ", "
                f"Ammo type: {self.ammo}, Mag capacity: {self.mag_size}, Fire Rate {self.fire_rate}")

    def weapon_attachments(self, attachment_name: str):
        self.attachments.append(attachment_name)

    def display_attachments(self):
        return f" {self.name} Attachments: {self.attachments}"




# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    #print("TODO: Implement namespace demonstration")

    weapon1 = Weapon("Sword", 30, 9, "Common")
    weapon2 = RangedWeapon("Gun", 50, 2, "common", "Pistol", 6, 7.5)
    weapon3 = RangedWeapon("RPG", 700, 100, "rare", "Rocket", 5, 2.5)

    print("Ranged weapon type through class ", RangedWeapon.weapon_type)
    print("Ranged weapon type through object ", weapon2.weapon_type)

    weapon3.aoe_radius = 25

    print("weapon2 namespace: ", weapon2.__dict__)
    print("weapon3 namespace: ", weapon3.__dict__)

    print("class namespace: ", Weapon.__dict__ )


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    # print("TODO: Implement shallow copy and deep copy demonstration")

    laser = RangedWeapon("Laser", 900, 500, "Epic", "Battery", 32, 15)

    copy_laser = copy(laser) # Creates a copy with references to the original, changes to this copy effect the original, a shallow copy
    deep_laser = deepcopy(laser) # Creates an independent copy of the original so that, unlike shallow copy, can be changed w/o effecting the original

    laser.damage = 550
    copy_laser.weapon_attachments("Heat sink")
    deep_laser.weapon_attachments("Scope")
    print(f"Original object: {laser.__dict__} \n Shallow copy: {copy_laser.__dict__} \n Deep copy: {deep_laser.__dict__} ")




# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\nTODO: Create and test your parent object")
    sword_weapon = Weapon("sword", 15, 10, "common")
    print(sword_weapon.display_stats())

    print("\nTODO: Create and test your child object")
    boom_rweapon = RangedWeapon("RPG", 700, 100, "rare", "Rocket", 5, 2.5)
    boom_rweapon.weapon_attachments("Guided lazer")
    print(boom_rweapon.display_stats())
    print(boom_rweapon.display_attachments())


    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()