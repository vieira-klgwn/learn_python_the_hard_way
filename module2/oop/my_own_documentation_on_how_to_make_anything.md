## These are the lessons that I learnt from learn python the hard way on how to make any program

<h1>How to make a Game program using OOP</h1>
<p>If you learn from how I made this game, you can get a clear point on how to make any program, even not a game</p>
<ul>
    <li>First list all the tasks that are needed to make the program(e.g Making the game, Beautifying the game with good UX)</li>
    <li>Take one task (e.g making the game)</li>
    <li>Try to think all the classes that will be needed and list them(e.g Map--to guide the player in rooms he is going to use for the game, Engine to run the map and traverse the gamer through out all the scenes of the game, Scene parent class, Scenes like CentralCorridor, EscapePod, Bridge....and events like Death, Finish etc, )</li>
    <li>Make the classes using oop, and do not implement them. use the pass keyword only on them 
    <p>
    (e.g class CentralCorridor:  def enter(): pass)    
    </p>
    </li>
    <li>In each class add in the actions that that class will do. For example, in map, it will need to show the opening scene and show the next_scene too. You do this class Map: def opening_scene: pass  def ending_scene: pass  def __init__: pass </li>
    <li>Using comments, say explicitly how you are going to make the game alive. Like imagine how data will be flowing in the game and write it in sentences (e.g )
    <p>e.g class Map: # get the name of the starting scene from the init ,and return that scene. def opening_scene: pass  #get the name of the scene they want to follow . if that name is valid and is in collection of scenes,return the scene as an object  def next_scene: pass  #get the starting scene as an argument def __init__: pass</p>
    </li>
    <li>Now after designing the whole program, making sure you understand how the whole app will be flowing through those comments, you can implement those comments.
        <p>ATTENTION:Make sure you checked carefully that if you write the whole program as the way you commented, the app should run.Check and check carefully and imagine yourself carefully how the app will be running</p>
        <h1>How to implement the comments<h1>
            <ul><li>Take the core componenst of the program and implement them. For example, the core components of the game were the Map and Engine. For a springboot app, it may be, the services.
            <p>This is an example of implementing map  : class Map(object):
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
            raise ValueError(f'Start scene does not exist {start_scene}')
        self.current_scene = start_scene
        
    def next_scene(self, scene_name):
        if scene_name in self.scenes:
            self.current_scene = scene_name
            return self.scenes[scene_name]
        return self.scenes['death']
        
        

    def open_scene(self):
        return self.scenes[self.current_scene]
   
</p>
Implement the Engine and test if actually An map class can give the engine a scene one by one , and if the engine runs the provided scenes one by the one , until to the last one. Check if the program exits. To make it more obvious, Make the scene print something like "Central corridor scene" , etc... and also return the 'central_corridor' string to be used in the map. To summarize it, all scenes can be looking like class CentralCorridor: def enter(self): print('Central corridor scene') return 'central_corridor'. and Map looking like those codes above, and Engine looking like this : class Engine(object):
    def __init__(self, scene_map):
        self.map = scene_map
    # play a specific scene
    def play(self):
        current_scene = self.map.opening_scene()
        last_scene = self.map.next_scene('finished')
        
        
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.map.next_scene(next_scene_name)              
                
            
        current_scene.enter() Now if Map is giving to the Engine correct scenes in order using the Scene classes like Central_corridor, proceed</li> 
        
        </ul>
    <li>Now after the core components work, Implement the Scene classes to do their jobs by implementing the comments you wrote in them.</li>
    <li>
        
    </li>
    <li>Implement other tasks too using the guide I showed you above</li>
</ul>
