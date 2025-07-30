class Person:
    def __init__(self, name, hp, damage):
        # assert isinstance(name, (str)) and name.strip(), "name should be a string and non empty"
        # assert isinstance(hp, (int, float)) and hp >= 0, "hit points should be a NUMBER greater than or equal zero "
        # assert isinstance(damage,(int, float)) and damage > 0, "damage should be a NUMBER greater than zero" # You can also assert in the init function or any where. The pytest will just do assertions in order of from the first asserting it will meet to the last one by one. Therefore, if you run this code , you will get an error of an assert in this init function and will not get the one defined in the invariant function. 
        self.name = name
        self.hp = hp
        self.damage = damage
        


    def hit(self, who):
        self.hp -= who.damage
    def alive(self):
        return self.hp > 0

    def dinvariant(self): # Remember to give each and every method you write in a class an argument of 'self',even if that function do not need any argument
        assert not self.damage == 0, "Damage should never be zero"
        assert isinstance(self.hp,(int,float)), "hit points should be a number"
        if self.hp > 0:
            assert self.alive(), "When hit points are greater than zero , the player is always alive"
        assert not self.alive() == self.hp > 0, "When hit points are greater than zero , the player is always alive"
        
        