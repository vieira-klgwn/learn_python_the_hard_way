import ex47_dialogue as dialogue
import random
from sys import exit

# testing if  I can access the dialogue
# print(dialogue.DIALOGUE['CentralCorridor_enter'])
# It works haha , here we go
# 

# GAME DESCRIPTION CAN BE FOUND: https://github.com/vieira-klgwn/learn_python_the_hard_way/blob/main/module2/oop/ex47_dialogue.py

class Scene(object):

    # Enter a specific scene
    def enter(self):
        pass


class Engine(object):
    def __init__(self, scene_map):
        self.map = scene_map
    # play a specific scene
    def play(self):
        current_scene = self.map.opening_scene()
        last_scene = self.map.next_scene('finished')
        
        
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.map.next_scene(next_scene_name)              
                
            
        current_scene.enter() 
            

class Death(Scene):
    #Enter the death scene
    quicks = [
            'You\'re worse than my dog\'s puppus ',
            'You\' re such a luser...',
            'Your mom would be proud of you, and now ,look at you',
            'Shame on you, jerk. We though you\'re our hero',
            'I have a puppy that\' better at this '
    ]
    def enter(self):
        
        print(self.quicks[random.randint(0,len(self.quicks)-1)])
        exit(1)
        return 'central_corridor'

class CentralCorridor(Scene):
    # Enter the .....
    def enter(self):
        print(dialogue.DIALOGUE['CentralCorridor_enter'])
        choice = input("Choose btn 'shoot','joke' and 'dodge'> ")
        if choice == 'shoot':
            print(dialogue.DIALOGUE['CentralCorridor_shoot'])
            return 'death'
        elif choice == 'dodge':
            print(dialogue.DIALOGUE['CentralCorridor_dodge'])
            return 'death'
        elif choice == 'joke':
            print(dialogue.DIALOGUE['CentralCorridor_joke'])
            return 'laser_weapon_armory'
        else:
            print("Invalid input, RETRY.....")
            return 'central_corridor'

class LaserWeaponArmory(Scene):
    # Enter the .....
    def enter(self):
        print(dialogue.DIALOGUE['LaserWeaponArmory_enter'])
        guess = input("Input the correct key> ")
        attempts = 10
        code = f'{random.randint(1,9)}{random.randint(1,9)}{random.randint(1,9)}'
        while guess != code and attempts > 0:
            print(f"BZZZZZ, TRY AGAIN, You remain with {attempts} attempts")
            guess = input('> ')
            attempts -= 1
            
        if guess == code:
            print(dialogue.DIALOGUE['LaserWeaponArmory_guess'])
            return 'the_bridge'
        else:
            print(dialogue.DIALOGUE['LaserWeaponArmory_fail'])
            return 'death'

class TheBridge(Scene):
    # Enter the .....
    def enter(self):
        print(dialogue.DIALOGUE['TheBridge_enter'])
        choice = input("Choose btn 'place bomb'and 'throw bomb'> ")
        if choice == 'place bomb':
            print(dialogue.DIALOGUE['TheBridge_place_bomb'])
            return 'escape_pod'
        elif choice == 'throw bomb':
            print(dialogue.DIALOGUE['TheBridge_throw_bomb'])
            return 'death'
        else:
            print("Invalid input, TRY AGAIN.......")
            return 'the_bridge'

class EscapePod(Scene):
    # Enter the .....
    def enter(self):
        print(dialogue.DIALOGUE['EscapePod_enter'])
        
        guess = input("Enter the correct pod number between 1 and 5 > ")
        code = random.randint(1,5)
        if int(guess) == code:
            print(dialogue.DIALOGUE['EscapePod_escape'].format(guess=guess))
            return 'finished'
        else:
            print(dialogue.DIALOGUE['EscapePod_death'].format(guess=guess))
            return 'death'
        
        
class Finished(Scene):
    def enter(self):
        print("You Won. Game finished")
        exit(1)
        
        

class Map(object):
    scenes = {
        'central_corridor':CentralCorridor(),
        'laser_weapon_armory':LaserWeaponArmory(),
        'the_bridge':TheBridge(),
        'escape_pod':EscapePod(),
        'death':Death(),
        'finished': Finished()
    }
    def __init__(self, start_scene):
        if start_scene not in self.scenes:
            print(f"Invalid start scene {start_scene}")
        self.start_scene = start_scene
            
        
    def next_scene(self, scene_name):
        if scene_name not in self.scenes:
            print(f"Ooops , Scene does not exist: {scene_name}")
        return self.scenes[scene_name]
        

    def opening_scene(self):
        return self.scenes[self.start_scene]


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()


# ME WINNING THE GAME AFTER MORE THAN 5 ATTEMPTS. HHHH , I BET THIS WAS THE HARDEST GAME I'VE EVER PLAYED. BUT IT WAS WORTH IT........

# python3 ex47.py

# The Gothons of Planet Percal #25 have invaded your ship and destroyed your entire crew. 
# You are the last surviving member and your last mission is to get the neutron destruct 
# bomb from the Weapons Armory, put it in the bridge, and blow the ship up after getting 
# into an escape pod.
# You're running down the central corridor to the Weapons Armory when a Gothon jumps out, 
# red scaly skin, dark grimy teeth, and evil clown costume flowing around his hate-filled 
# body. He's blocking the door to the Armory and about to pull a weapon to blast you.

# Choose btn 'shoot','joke' and 'dodge'> joke

# Lucky for you they made you learn Gothon insults in the academy. You tell the one Gothon 
# joke you know: Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq 
# gur ubhfr. The Gothon stops, tries not to laugh, then busts out laughing and can't move. 
# While he's laughing you run up and shoot him square in the head putting him down, then 
# jump through the Weapon Armory door.


# You do a dive roll into the Weapon Armory, crouch and scan the room for more Gothons that 
# might be hiding. It's dead quiet, too quiet. You stand up and run to the far side of the 
# room and find the neutron bomb in its container. There's a keypad lock on the box and you 
# need the code to get the bomb out. If you get the code wrong 10 times then the lock closes 
# forever and you can't get the bomb. The code is 3 digits.

# Input the correct key> 353
# BZZZZZ, TRY AGAIN, You remain with 10 attempts
# > 123

# The container clicks open and the seal breaks, letting gas out. You grab the neutron bomb 
# and run as fast as you can to the bridge where you must place it in the right spot.


# You burst onto the Bridge with the neutron destruct bomb under your arm and surprise 5 
# Gothons who are trying to take control of the ship. Each of them has an even uglier clown 
# costume than the last. They haven't pulled their weapons out yet, as they see the active 
# bomb under your arm and don't want to set it off.

# Choose btn 'place bomb'and 'throw bomb'> place bomb

# You point your blaster at the bomb under your arm and the Gothons put their hands up and 
# start to sweat. You inch backward to the door, open it, and then carefully place the bomb 
# on the floor, pointing your blaster at it. You then jump back through the door, punch the 
# close button and blast the lock so the Gothons can't get out. Now that the bomb is placed 
# you run to the escape pod to get off this tin can.


# You rush through the ship desperately trying to make it to the escape pod before the whole 
# ship explodes. It seems like hardly any Gothons are on the ship, so your run is clear of 
# interference. You get to the chamber with the escape pods, and now need to pick one to take. 
# Some of them could be damaged but you don't have time to look. There's 5 pods, which one do 
# you take?

# Enter the correct pod number between 1 and 5 > 4

# You jump into pod 4 and hit the eject button. The pod easily slides out into space 
# heading to the planet below. As it flies to the planet, you look back and see your ship 
# implode then explode like a bright star, taking out the Gothon ship at the same time. You won!

# You Won. Game finished


        
        
        
        
