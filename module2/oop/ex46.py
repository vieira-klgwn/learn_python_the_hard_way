## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

# Dog is-a Animal object
class Dog(Animal):
    def __init__(self, name):
        ## Dog  has  a name attribute
        self.name = name

# Cat is-a Animal  object
class Cat(Animal):
    def __init__(self, name):
        ## Cat has a name attribute
        self.name = name


class Person(object):
    def __init__(self, name):
        # Person has a name attribute
        self.name = name
        ## Person has a pet or some kind
        self.pet = None

## Employee is a Person object
class Employee(Person):
    def __init__(self, name, salary):
        ## ?? hmm what is the strange magic?
        super(Employee, self).__init__(name)
        ## Employee has a salary
        self.salary = salary

## Fish is a object

class Fish(object):
    pass

## Salmon is a Fish object
class Salmon(Fish):
    pass

## Halibut is a fish object
class Halibut(Fish):
    pass
    

## rover is a Dog
rover = Dog("Rover")

## satan is a Cat
satan = Cat("Satan")


## Mary is a person
mary = Person("Mary")

## mary has a pet
mary.pet = satan

## frank is an imployee(who has salary)
frank = Employee("Frank", 120000)

## frank has a pet 
frank.pet = rover

## flipper is a fish
flipper = Fish()

## crouse is a Salmon
crouse = Salmon()

## harry is a halibut
harry = Halibut()




































    
    

    
        
        
        
        
    
