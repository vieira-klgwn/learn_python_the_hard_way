import ex26
from pprint import pprint

# Showing how to import
print ("name ", ex26.name)
print("height", ex26.height)

# Showing how you can change variable in a module using their __dict__ property
print("I am currently {} inches tall".format(ex26.height))

ex26.__dict__['height'] = 1000
print(f"I am now {ex26.height} inches tal")

ex26.height = 12
print(f"Ooops, now I'm {ex26.__dict__['height']} inches tall")

#showing some examples of dundles (double underscore variables)

print(pprint.__doc__) # this will give you the descriptiion of the pprint function . 

# This works the same way as the help function 

help(pprint)