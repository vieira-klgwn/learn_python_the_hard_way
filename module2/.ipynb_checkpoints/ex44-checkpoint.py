import random
def Person_new(name, age, eyes, job):
    person = {
        'name': name,
        'age': age,
        'eyes':eyes,
        'hit_points': 0,
        'damage':'sm',
        'dialogue':'I am ...',
        'job':job
    }

    if job == 'boxer':
        person['hit_points'] = 300
        person['damage'] = 'xl'
        person['dialogue'] ="I am a boxer, so you can't win me "
    elif job == 'baby':
        person['hit_points'] = 100
        person['damage'] = 'sm'
        person['dialogue'] = 'Oooh no, I am a baby, I stand no chance of winning a boxer'
    else:
        person['hit_points'] = 0
        person['damage'] ='x_sm'
        person['dialogue']='I am nothing BTW, I can \'t win any_thing ',
     
   

    def talk():
        print(f"I am {person['name']} and {person['dialogue']}")
        
    # Add a new function hit()  which makes one person hit another person
    def hit():
        # Give people hit points in their dict( already done in the dict) and have hit() randomly add each person's hit points
        person['hit_points'] += random.randint(1,5)
        

    person['hit'] = hit
    person['talk'] = talk
    return person


# Create new players. They are going to 1# talk and after 2# hit a wall


vieira = Person_new('Vieira', 18, 'Brown', 'boxer')
hacker = Person_new('Hacker', 30, 'Brown', 'baby')

# Add players to the list of players
players = [vieira, hacker]

still_want_to_play = True

while still_want_to_play:
    print("W E L C O M E   T O   T H E   G A M E   O F   H I T S")
        # Let them talk
    print('Let them talk')
    print('*'*30)
    for player in players:
        player['talk']()
    print('\n') 

    # Let's first see the poinsts they have at first
    print("Let's first see the poinsts they have at first")
    print('*'*30)
    print('\n')
    for player in players:
        print(f"For {player['name']}, he has {player['hit_points']}")
    print('\n')


    # Let them hit the wall
    print("Let them hit the wall...")
    print('*'*30)
    print("wait as the players are hitting the wall")
    print('\n')
    for player in players:
        player['hit']()
    print("They \'ve all hit the wall successfully")
    print('\n')
    print("You can now we see who have the GREATEST POINTS! ")

    # Now let's see again what points they have
    print("Now let's see again what points they have")
    print('*'*30)
    print('\n')
    for player in players:
        print(f"For {player['name']}, he has {player['hit_points']}")
    print("GAME OVER! I think you saw who won the game") 
    choice = input('Do you still want to play?(Y/N) ')
    if choice == 'Y':
        still_want_to_play = True
    elif choice == 'N':
        print("Bye, Oki donkie! ")
        still_want_to_play = False
    else:
        print("We really don't know what you are talking about. use capital Y or capital N to confirm if you still wanna game. Try Again")
        still_want_To_play = False
        



    



    
        