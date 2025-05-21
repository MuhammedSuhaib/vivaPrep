from animals.mammals import Cat, Dog

def test_cat():
    c = Cat()
    assert c.speak() == "Meow!"

def test_dog():
    d = Dog()
    assert d.speak() == "Woof!"