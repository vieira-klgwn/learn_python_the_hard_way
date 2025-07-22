# I was told to make a function that does this 

# In this Study Drill you’re going to create a new
# function that creates any car. Your creator function should meet these requirements:
# 1.It should take parameters to set things like the color, speed, or anything else your cars can do.
# 2.It should create a dict that has the correct settings and already contains all the functions
# you’ve created.
# 3.It should return this dict so people can assign the results to anything they want and use later.
# 4.It should be written so that someone can create any number of different cars and each one
# they make is independent.
# 5.
# Your code should test #4 by changing settings in a few different cars and then confirming they
# didn’t change in other cars.

def its_sound():
    print('VROOM')

def create_car (type_,color, speed):
    new_car = {
        'type': type_,
        'color': color,
        'speed': speed,
        'its_sound': its_sound # make sure you understand this
    }
    return new_car

    

mercedez = create_car('benz', 'dark-grey','100MPH')
toyota = create_car('corolla','black', '40MPH')
prado = create_car('prado','black','80MPH')
range_rover = create_car('range_rover_latest','dark-grey','120MPH')


# text if cars are independent

#               Before editing

print(f"You have a {mercedez['color']} {mercedez['speed']} {mercedez['type']} car ")

print(f"You have a {toyota['color']} {toyota['speed']} {toyota['type']} car ")

print(f"You have a {prado['color']} {prado['speed']} {prado['type']} car ")

print(f"You have a {range_rover['color']} {range_rover['speed']} {range_rover['type']} car ")

print("Wann try this thing")

range_rover['its_sound']()
print("\n")



#              Editing one of the cars


prado['speed'] = '70MPH'



#              After editing

print(f"You have a {mercedez['color']} {mercedez['speed']} {mercedez['type']} car ")

print(f"You have a {toyota['color']} {toyota['speed']} {toyota['type']} car ")

print(f"You have a {prado['color']} {prado['speed']} {prado['type']} car ")

print(f"You have a {range_rover['color']} {range_rover['speed']} {range_rover['type']} car ")







