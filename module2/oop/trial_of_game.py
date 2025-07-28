import ex47_dialogue as dialogue

# testing if  I can access the dialogue
# print(dialogue.DIALOGUE['CentralCorridor_enter'])
# It works haha , here we go

class Scene(object):

    # Enter a specific scene
    
    def enter(self):
        pass


class Engine(object):
    def __init__(self, scene_map):
        self.map = scene_map
    
    def play(self):
        current_scene = self.map.open_scene()
        while True:
            if current_scene == 'finished' or current_scene == 'death':
                break
            next_scene_name = current_scene.enter()
            current_scene = self.map.next_scene(next_scene_name)
       
           
class Death(Scene):
    #Enter the death scene
    def enter(self):
        print("Ooops , sorry you are dead,")
        print("You're worse than my dog")
        print("You're a useless hero")
        print("Go to where you belong luser. You're such a looser !")
        
# test the death scene
# dead = Death()

# dead.enter()
# it works

class CentralCorridor(Scene):
    # Enter the .....
    def enter(self):
        print(dialogue.DIALOGUE['CentralCorridor_enter'])
        choice = input("> ")
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
            print("You are spoiling the game , I don't know what you mean by that input")
            return 'central_corridor'
    

class LaserWeaponArmory(Scene):
    # Enter the .....
    def enter(self):
        print(dialogue.DIALOGUE['LaserWeaponArmory_enter'])
        guess = input("> ")
        if guess == '123':
            print(dialogue.DIALOGUE['LaserWeaponArmory_guess'])
            return 'the_bridge'
        else:
            print(dialogue.DIALOGUE['LaserWeaponArmory_fail'])
            return 'death'
        

class TheBridge(Scene):
    # Enter the .....
    def enter(self):
        print(dialogue.DIALOGUE['TheBridge_enter'])
        choice = input("> ")
        if choice == 'throw bomb':
            print(dialogue.DIALOGUE['TheBridge_throw_bomb'])
            return 'death'
        elif choice == 'place_bomb':
            print(dialogue.DIALOGUE['TheBridge_place_bomb'])
            return 'escape_pod'
        else:
            print("You are spoiling the game , I don't know what you mean by that input")
            return 'the_bridge'
    

class EscapePod(Scene):
    # Enter the .....
    def enter(self):
        print(dialogue.DIALOGUE['EscapePod_enter'])
        choice = input("> ").strip()
        if choice == '2':
            print(dialogue.DIALOGUE['EscapePod_escape'])
            return 'finished'
        else:
            print(dialogue.DIALOGUE['EscapePod_death'])
            return 'death'

class Map(object):
    scenes = {
        'central_corridor':CentralCorridor(),
        'laser_weapon_armory':LaserWeaponArmory(),
        'the_bridge':TheBridge(),
        'EscapePod':EscapePod(), 
        'death':Death()
    }
    def __init__(self, start_scene):
        if start_scene not in self.scenes:
            raise ValueError(f'Start scene does not exist {start_scene}')
        self.current_scene = start_scene
        
    def next_scene(self, scene_name):
        if scene_name in self.scenes:
            self.current_scene = scene_name
            return self.scenes[scene_name]
        return self.scenes['death']
        
        

    def open_scene(self):
        return self.scenes[self.current_scene]
   



a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
        
        
        
        
        