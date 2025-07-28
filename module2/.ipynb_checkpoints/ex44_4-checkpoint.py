def Person_new(name, age, eyes):
    person = {
        'name':name,
        'age':age,
        'eyes':eyes,
    }

    def talk(words):
        print(f"I am {person['name']} and {words}")

    person['talk'] = talk # adding a new feature to a dict (which is now a function)
    return person


becky = Person_new('Becky', 39, green)
becky['talk']('I am talking here!')
    
    
