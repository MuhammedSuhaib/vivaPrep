from animals.birds import Parrot, Sparrow

def test_parrot():
    p= Parrot()
    assert p.speak() == "Squawk!"
def test_sparrow():
    s = Sparrow()
    assert s.speak() == "Chirp!"