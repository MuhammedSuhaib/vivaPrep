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


#                                   A SIMPLE DEMO OF OOP
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
#                                   GETTER AND SETTER
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
#                                    ATTRIBUTE CALLS
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
#                                    METHODS CALLS
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
