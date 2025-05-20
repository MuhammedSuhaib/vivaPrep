bold_start = '\033[1m'
bold_end = '\033[0m'
italic_start = '\033[3m'
italic_end = '\033[0m'
red_start = '\033[91m'
red_end = '\033[0m'

class accessModifiers:
    def __init__(self):
        self.public_variable = "I am public variable"
        self._protected_variable = "I am protected variable"
        self.__private_variable = "I am private variable"
        # self.public_method()
        # self._protected_method()
        # self.__private_method()
        # self.__private_method_with_args("Hello", "World")
        # self.__private_method_with_args("Hello", "World", "!")
        # self.__private_method_with_args("Hello", "World", "!", "Python")

    def get_private_variable(self):
        return self.__private_variable
    def set_private_attribute(self,new_variable):
        if type(new_variable)!= str: return(f'{red_start}NAN{red_end}') 
        else :
            self.new_variable = self.__private_variable 
            return new_variable

lets_access = accessModifiers()
print(lets_access.public_variable)
print('PROTECTED DON`T SHY TO SHOW OFF >>',lets_access._protected_variable)
print('ACCESS BY NAME MANGLED >>',lets_access._accessModifiers__private_variable)
print('ACCESS BY GETTER >>',lets_access.get_private_variable())

#print(lets_access.__private_variable) # AttributeError: 'accessModifiers' object has no attribute '__private_variable'. 
lets_access.__private_variable = 'i `ve updated the private attribute'
print( lets_access.__private_variable)
print('>>',lets_access.__private_variable is lets_access.get_private_variable()) #false 
# this means that i ve only updated the instance`s attribute but class still ve same

print('ACCESS BY SETTER >>',lets_access.set_private_attribute('updated using setter'))
print('ACCESS BY SETTER >>',lets_access.set_private_attribute(3))
print('ACCESS BY GETTER >>',lets_access.get_private_variable())
