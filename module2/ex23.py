fruit = [
    ['Apples',12,'AAA'], ['Oranges', 1, 'B'],
    ['Pears', 2, 'A'], ['Grapes', 14, 'UR']
]

cars = [
    ['Cadillac', ['Black', 'Big', 34500]],
    ['Corvette', ['Red', 'Little', 1000000]],
    ['Ford', ['Blue', 'Medium', 1234]],
    ['BMW', ['White', 'Baby', 7890]]
]

languages = [
    ['Python', ['Slow', ['Terrible', 'Mush']]],
    ['JavaScript', ['Moderate',['Alright', 'Bizarre']]],
    ['C', ['Fast', ['Annoying', 'Dangerous']]],
    ['Forth', ['Fast', ['Fun','Difficult']]],
    ['Perl6',['Moderate', ['Fun', 'Weird']] ]
]

print(f"In Fruits,  12 is{fruit[0][1]} and AAA is {fruit[0][2]} and 14 is {fruit[3][1]} and Apples is {fruit[0][0]} ")

print(f"In Cars , Big is {cars[0][1][1]} and 1234 is {cars[2][1][2]} and 34500 is {cars[0][1][2]} and Blue is {cars[2][1][0]}" )

print(f"In Languages, Slow is {languages[0][1][0]} and Alright is {languages[1][1][1][0]} and Dangerous is {languages[2][1][1][1]} and Weird is {languages[4][1][1][1]} and Moderate is {languages[1][1][0]}")

print(f"If you look well, you'll find that Mush is {languages[0][1][1][1]}")
