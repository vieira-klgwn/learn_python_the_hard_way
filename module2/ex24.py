fruit = [
    {'kind':'Apples','count':12, 'rating':'AAA'}, 
    {'kind':'Oranges','count':1,'rating':'B'},
    {'kind':'Pears', 'count': 2, 'rating':'A'}, 
    {'kind':'Grapes','count': 14, 'rating':'UR'}
]

cars = [
    {'type':'Cadillac', 'color':'Black', 'size':'Big', 'miles': 34500},
    {'type':'Corvette', 'color':'Red', 'size':'Little', 'miles': 1000000},
    {'type':'Ford', 'color':'Blue','size' :'Medium','miles': 1234},
    {'type':'BMW', 'color':'White', 'size':'Baby','miles': 7890}
]

languages = [
    {'name':'Python', 'speed':'Slow', 'opinion':['Terrible', 'Mush']},
    {'name':'JavaScript', 'speed':'Moderate','opinion':['Alright', 'Bizarre']},
    {'name':'C++', 'speed':'Fast', 'opinion':['Annoying', 'Dangerous']},
    {'name':'Forth', 'speed':'Fast','opinion': ['Fun','Difficult']},
    {'name':'Perl6','speed':'Moderate','opinion': ['Fun', 'Weird']}
]

print(f"In fruits, 12 is {fruit[0]['count']} and 'AAA' is {fruit[0]['rating']} and 14 is {fruit[3]['count']} and Apples is {fruit[0]['kind']}")

print(f"In cars, Big is {cars[0]['size']} and White is {cars[3]['color']}")

print(f"In languages, Slow is {languages[0]['speed']} and Alright is {languages[1]['opinion'][0]} and Moderate is {languages[4]['speed']}")
