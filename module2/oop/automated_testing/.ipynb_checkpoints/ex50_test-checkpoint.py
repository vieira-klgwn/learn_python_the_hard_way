from ex50 import Person

def test_combat():
    boxer = Person("Boxer", 100, 10)
    zombie = Person("Zed", 1000,1000)

    # these asserts are bad, fix them
    assert boxer.hp == 100, f"Expected boxer to have hp 100 but got {boxer.hp}"
    assert zombie.hp == 1000, f"Expected zombie to have hp 1000 but got {zombie.hp}"

    boxer.hit(zombie)
    assert zombie.alive(), "Zombie should be alive."

    zombie.hit(boxer)
    assert not boxer.alive(), "Boxer should be dead."