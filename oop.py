bold_start = '\033[1m'
bold_end = '\033[0m'
italic_start = '\033[3m'
italic_end = '\033[0m'
red_start = '\033[91m'
red_end = '\033[0m'


###############################################################################################
###############################################################################################
                #                    OOP is all about OBJECTS
                # - An object is an instance of a class with its own unique data.
                # - "Unified data type" means everything in Python is an object.

                # "Root of the hierarchy" → `object` is the top-most parent class.
                #  All other classes are inherited from it (directly or indirectly).

###############################################################################################
###############################################################################################



# If I want to tweak the behavior of a class, use `__new__`.
# But normally, we just put data in `__init__`.


###############################################################################################
#                                   A SIMPLE DEMO OF OOP CLASS
###############################################################################################

class Hackers:
    hackers_count = 0  # Example of a class attribute

    def __init__(self, name: str, age: int, is_present: bool):  # Example of a constructor
        self.__name = name        # Private attribute
        self._age = age           # Protected attribute
        self.is_present = is_present  # Public attribute

    def greet(self) -> None: # Example of an instance method
        print(f"Hi {self.__name}")

    @classmethod
    def count_updater(cls):  # Example of a class method
        cls.hackers_count += 1
        print(f"Total hackers: {cls.hackers_count}")

    def run_all(self):  # Another Example of  instance method
        self.greet()
        self.count_updater()


h1 = Hackers("A", 20, True).run_all()
h2 = Hackers("B", 22, True).run_all()
h3 = Hackers("C", 25, True).run_all()
h4 = Hackers("D", 30, True).run_all()




###############################################################################################
#                               ATTRIBUTEs AND METHODs
###############################################################################################

            # --- Attributes vs Normal Variables ---
# Attributes belong to objects/classes (accessed with obj.attr).
# Normal variables are standalone, not tied to objects (e.g., x = 5).

            # --- Methods vs Normal Functions ---
# Methods are functions defined inside classes (called with obj.method()).
# Functions are standalone and not bound to objects (called like func()).


                    # --- 3 Python Method Types ----
        # Instance methods – default, use self, access instance.
        # Class methods – use @classmethod, take cls, access class.
        # Static methods – use @staticmethod, no self/cls, utility functions.


# 1: Instance method:
def method(self):  # `self` is auto-passed
    self.x  # access with dot

# 2: Class method:
@classmethod
def method(cls):
    cls.y  # access class attr

# 3: Static method:
@staticmethod
def method():
    pass  # no self/cls

# Dot (.) is used inside method body, not in the param list.




                    # ---- 3 Python Attribute Types ---
        # Instance attributes – defined in __init__, unique to object.
        # Class attributes – defined in class, shared by all instances.
        # Dynamic attributes – added at runtime to objects




###############################################################################################
#                                       DECORATORS
###############################################################################################

# Decorator = Wrapper function
# A decorator is just a function that wraps another function to modify its behavior without changing its code.

#HERE  ➡   https://github.com/MuhammedSuhaib/21_oop_tasks.py/blob/main/task_16.py
#HERE  ➡   https://github.com/MuhammedSuhaib/21_oop_tasks.py/blob/main/task_17.py

# @property: makes a method act like an attribute. Same as getter
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

p = Person("Ali")
print(p.name)  # acts like attr, calls method
# No `()` needed when accessing. Good for read-only or controlled access.


# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price can't be negative")
        else:
            self._price = value

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Usage:
p = Product(100)
print(p.price)  # 100

p.price = 150
print(p.price)  # 150

del p.price  # Deleting price...
print('|'*100)
print('|'*100)
print(p.price)  #❌AttributeError: 'Product' object has no attribute '_price'. Did you mean: 'price'?
###############################################################################################





class accessModifiers:
    def __init__(self):
###############################################################################################
#                                   SOME ATTRIBUTES
############################################################################################### 
        self.public_variable = "I am public variable"
        self._protected_variable = "I am protected variable"
        self.__private_variable = "I am private variable"

###############################################################################################
#                                   SOME METHODS
############################################################################################### 
    def __call__(self):
            print("I'm callable!")

    def public_method(self):
        print("I am public method")

    def _protected_method(self):
        print("I am protected method")

    def __private_method(self):
        print("I am private method")

###############################################################################################
#*                                   GETTER AND SETTER
############################################################################################### 

    def get_private_variable(self):
        return self.__private_variable
    def get_private_method(self):
        return self.__private_method()
    def set_private_attribute(self,new_variable):
        if type(new_variable) == str: #only works when it is string 
            self.__private_variable = new_variable
            return new_variable


###############################################################################################
#*                                    ATTRIBUTE CALLS
###############################################################################################

lets_access = accessModifiers()
print(lets_access.public_variable)
print('PROTECTED DON`T SHY TO SHOW OFF >>',lets_access._protected_variable)
print('ACCESS BY NAME MANGLED >>',lets_access._accessModifiers__private_variable)
print('ACCESS BY GETTER >>',lets_access.get_private_variable())

#print(lets_access.__private_variable) #❌❌ AttributeError: 'accessModifiers' object has no attribute '__private_variable'. 
lets_access.__private_variable = 'i `ve updated the private attribute'
print( lets_access.__private_variable)# creates new public var, doesn't affect the private one
print('>>',lets_access.__private_variable is lets_access.get_private_variable()) #false 

print('ACCESS BY SETTER >>',lets_access.set_private_attribute('updated using setter'))
print('ACCESS BY SETTER >>',lets_access.set_private_attribute(3))
print('ACCESS BY GETTER >>',lets_access.get_private_variable())

###############################################################################################
#*                                    METHODS CALLS
###############################################################################################

obj = accessModifiers()
obj.public_method()
obj._protected_method()
obj._accessModifiers__private_method() # access private method using name mangling
obj.get_private_method() # access private method using getter
#obj.__private_method() # ❌❌AttributeError: 'accessModifiers' object has no attribute '__private_method'

for_calls = accessModifiers()
for_calls()
print(callable(for_calls)) # True
print(callable(123)) # False
print(callable(accessModifiers)) # True




###############################################################################################
#*                                    DELETER
###############################################################################################
class TryToDelete:
    def __init__(self):
        self.about_to_delete = 'to be deleted'
#  can't use `@deleter` without defining a `@property`.
# A property must have at least a dummy getter for the deleter to work.
# like  @property  def deleting_def(self): pass 
# then @deleting_def.deleter def deleting_def(self): print('Deleting...') del self.about_to_delete
    @property
    def deleting_def(self):
        """ here i ve to tell wht hpn while deleting"""
        print(self.about_to_delete)
        print('while deleting the variable passed out from this program😔')

    @deleting_def.deleter
    def deleting_def(self):
        del self.about_to_delete
        print('about_to_delete: ', self.about_to_delete)

wht_hpn_while_deleting = TryToDelete()
wht_hpn_while_deleting.deleting_def  # triggers @property
# del wht_hpn_while_deleting.deleting_def  # triggers @deleter ❌




###############################################################################################
#*                                __call__ and callable()
###############################################################################################

#__call__(self, ...):   Makes an object callable like a function.
# callable(obj) :       Returns `True` if `obj` can be called (has `__call__`).
#HERE  ➡   https://github.com/MuhammedSuhaib/21_oop_tasks.py/blob/main/task_19.py

class A:
    def __call__(self):
        print("called")

a = A()
callable(a)        # True
a()                # prints "called"




###############################################################################################
#*                                        Design Patterns
###############################################################################################

            # --- Metaclass Design Patterns ---  
# A blueprint for **creating classes** (just like classes create objects).
# Means if class is the type of an object, then a metaclass is the type of a class.

class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class: {name}")
        return super().__new__(cls, name, bases, dct)

        # Class using the custom metaclass
class MyClass(metaclass=Meta):
    pass




            # --- Singleton Design Patterns ---
# Ensures only **one instance** of a class exists, and provides global access to it.

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # super() here calls the parent class of Singleton, which is object by default.
            # So, super().__new__(cls) means:
            # "Use Python’s built-in way to create a new object of this class."
            
            # Even if you don’t see a parent explicitly, every class in Python inherits from object automatically
            cls._instance = super().__new__(cls)
        return cls._instance

# Create instances of the Singleton class
singleton1 = Singleton()
singleton2 = Singleton()

# Check if both instances are the same
print(singleton1 is singleton2)  # Output: True
print(id(singleton1) == id(singleton2))  # Output: True




            # --- Factory Design Patterns ---

# A **parent class** creates objects, but **child classes** decide *what kind* of objects to create.

# Product interface
class Animal:
    def speak(self):
        pass

# Concrete products
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Factory class
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Invalid animal type")

# Use the factory to create animals
dog = AnimalFactory.create_animal("dog")
cat = AnimalFactory.create_animal("cat")

# Call the speak method
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!