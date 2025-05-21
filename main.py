from animals import Dog, Cat, Parrot, Sparrow
from vehicles import Car, Bike

# A module is a single file containing Python code  
# Package is a directory containing multiple modules and an __init__.py file.

# Create instances of animal classes
dog = Dog()
cat = Cat()
parrot = Parrot()
sparrow = Sparrow()

# Call methods from animal classes
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
print(parrot.speak())  # Output: Squawk!
print(sparrow.speak())  # Output: Chirp!

# Create instances of vehicle classes
car = Car("Toyota Corolla")
bike = Bike("Harley Davidson")

# Call methods from vehicle classes
print(car.display())  # Output: Car: Toyota Corolla
print(bike.display())  # Output: Bike: Harley Davidson