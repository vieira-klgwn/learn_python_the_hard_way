ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait there are not 10 things in that list. Let's fix that. ")
print('\n')

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    print('\n')
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")
    print('\n')



print("There we go: ", stuff)
print('\n')
print("Let's do some more things with stuff.")
print('\n')


print(stuff[1])
print('\n')

print(stuff[-1]) #whoa! fancy
print('\n')

print(stuff.pop())
print('\n')

print(' '.join(stuff)) # what! cool!
print('\n')

print('#'.join(stuff[3:5])) # super stellar!
print('\n')




    