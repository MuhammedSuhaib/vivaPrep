bold_start = '\033[1m'
bold_end = '\033[0m'
italic_start = '\033[3m'
italic_end = '\033[0m'
red_start = '\033[91m'
red_end = '\033[0m'

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
        if type(new_variable)!= str: return(f'{red_start}NAN{red_end}') 
        else :
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