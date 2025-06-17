# class Hackers:
#     hackers_count = 0
#     def __init__(self, name: str, age: int, is_present: bool):
#         self.__name = name        # private
#         self._age = age           # protected
#         self.is_present = is_present  # public
#     def greet(self) -> None:
#         print(f"Hi {self.__name}")
#     @classmethod 
#     def count_updater(cls):
#         cls.hackers_count += 1
#         print(f"Total hackers: {cls.hackers_count}")
    
#     def run_all(self):
#         self.greet()
#         self.count_updater()
# # h1 = Hackers("A", 20, True).run_all()
# # h2 = Hackers("B", 22, True).run_all()
# # h3 = Hackers("C", 25, True).run_all()
# # h4 = Hackers("D", 30, True).run_all()

class Person:
    # Class attribute
    species = "Homo sapiens"

    # Constructor
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    # Instance method
    def display(self):
        print(f"{self.name} is {self.age} years old and is a {self.species}.")

    # Class method
    @classmethod
    def update_species(cls, new_species):
        cls.species = new_species
        print(f"Species updated to {cls.species}.")

    # Static method
    @staticmethod
    def is_adult(age):
        return age >= 18

# Create an instance of the Person class
person1 = Person("Alice", 25)

# Call instance method
person1.display()  # Output: Alice is 25 years old and is a Homo sapiens.

# Call class method to update species
Person.update_species("Homo sapiens sapiens")  # Output: Species updated to Homo sapiens sapiens.
person1.display()  # Output: Alice is 25 years old and is a Homo sapiens sapiens.

# Call static method to check if the person is an adult
print(f"Is Alice an adult? {Person.is_adult(person1.age)}")  # Output: Is Alice an adult? True



# ✅ An object is an instance of a class and has its own unique data.

# --- Attributes vs Normal Variables ---
# Attributes belong to objects/classes (accessed with obj.attr).
# Normal variables are standalone, not tied to objects (e.g., x = 5).

# --- Methods vs Functions ---
# Methods are functions defined inside classes (called with obj.method()).
# Functions are standalone and not bound to objects (called like func()).
