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
        pass
    # play a specific scene
    def play(self):
        pass

class Death(Scene):
    #Enter the death scene
    def enter(self):
        pass

class CentralCorridor(Scene):
    # Enter the .....
    def enter(self):
        pass

class LaserWeaponArmory(Scene):
    # Enter the .....
    def enter(self):
        pass

class TheBridge(Scene):
    # Enter the .....
    def enter(self):
        pass

class EscapePod(Scene):
    # Enter the .....
    def enter(self):
        pass

class Map(object):
    def __init__(self, start_scene):
        pass
    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
        
        
        
        
        