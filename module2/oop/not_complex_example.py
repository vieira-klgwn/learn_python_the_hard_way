class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello from Parent, my name is {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Calls Parent's __init__
        self.age = age

    def greet(self):
        super().greet()  # Calls Parent's greet method
        print(f"And I am {self.age} years old.")

child_instance = Child("Alice", 10)
child_instance.greet()