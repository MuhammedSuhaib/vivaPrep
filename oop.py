

            # ---- Python Attribute Types ---
# Instance attributes – defined in __init__, unique to object.
# Class attributes – defined in class, shared by all instances.
# Dynamic attributes – added at runtime to objects




# `@property` makes a method act like an attribute. Same as getter

# ### Example:

# ```py
# class Person:
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name

# p = Person("Ali")
# print(p.name)  # acts like attr, calls method
# ```

# No `()` needed when accessing. Good for read-only or controlled access.


        #A decorator is a function that wraps another function to modify its behavior.

### `@property`, `@<prop>.setter`, `@<prop>.deleter` example:

# ```py
# class A:
#     def __init__(self):
#         self._x = 1

#     @property
#     def x(self):
#         return self._x

#     @x.setter
#     def x(self, val):
#         self._x = val

#     @x.deleter
#     def x(self):
#         del self._x
# ```

# Use:

# ```py
# a = A()
# a.x = 5       # setter
# print(a.x)    # getter
# del a.x       # deleter
# ```
