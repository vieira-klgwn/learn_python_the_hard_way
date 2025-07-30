from ex50 import Person

def test_combat():
        
    boxer = Person("Boxer", 10, 100)
    zombie = Person("Zed", 1000,100)

        
    # # these asserts are bad, fix them
    # assert boxer.hp == 100, f"Expected boxer to have hp 100 but got {boxer.hp}"
    # assert zombie.hp == 1000, f"Expected zombie to have hp 1000 but got {zombie.hp}"# This is not a good style of programming, because if we change hp to hit_points in the main class, it will 
    # #crash. 



    
        # using the invariant to make sure that the state of object is valid according to the rules that we defined in the main class 

    boxer.__invariant__()
    zombie.__invariant__()


    boxer.hit(zombie)
    assert zombie.alive(), "Zombie should be alive."

    zombie.hit(boxer)
    assert not boxer.alive(), "Boxer should be dead."






    