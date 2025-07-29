
# 🧠 How to Make a Game Program Using OOP (Inspired by Learn Python the Hard Way)

If you learn from how I made this game, you'll gain a clear understanding of how to build any kind of program using Object-Oriented Programming (OOP), not just games.

---

## 🗺️ Step-by-Step Roadmap to Build a Program

### 1. Start with Task Listing

List all the key tasks needed for your program.

**Example from the game:**
- Build the game logic  
- Add player interaction (UX)  
- Handle victory/defeat logic  

---

### 2. Break One Task Down

Take one task and break it down into manageable components.

**Example:**

**Task**: Making the Game  
**Breakdown:**
- A `Map` class to guide the player between rooms.  
- An `Engine` class to run the game flow.  
- A parent `Scene` class for inheritance.  
- Child scenes like `CentralCorridor`, `LaserWeaponArmory`, etc.  
- Events like `Death`, and `Finished`.  

---

### 3. Sketch Class Blueprints First

Write empty classes with `pass` and meaningful names.

```python
class Map:
    pass

class Engine:
    pass

class Scene:
    pass

class CentralCorridor(Scene):
    pass
```

This helps you structure before implementing.

---

### 4. Use Comments to Imagine Flow

Before writing any logic, imagine how your program will behave and write it as comments.

**Example from the `Map` class:**

```python
# Get the starting scene from __init__ and return it
# In next_scene, take a scene name and return the corresponding scene object
# Store all scene instances in a dictionary
```

By doing this, you mentally walk through your program before coding.

---

### 5. Design the Core Components First

Pick the core logic that powers your program and make sure it works first.

**For a game:**
- `Map` connects scenes.
- `Engine` controls game flow.

```python
class Map:
    scenes = {
        'central_corridor': CentralCorridor(),
        'death': Death(),
        'finished': Finished()
        # Add other scenes...
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return self.scenes.get(scene_name, self.scenes['death'])

    def opening_scene(self):
        return self.scenes[self.start_scene]
```

```python
class Engine:
    def __init__(self, scene_map):
        self.map = scene_map

    def play(self):
        current_scene = self.map.opening_scene()
        last_scene = self.map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.map.next_scene(next_scene_name)

        current_scene.enter()
```

Test it with scenes that just print messages:

```python
class CentralCorridor(Scene):
    def enter(self):
        print("This is the Central Corridor.")
        return 'death'
```

---

### 6. Implement Real Scene Logic

Once the core loop works, go back and implement the actual scene logic using `input()` and your planned dialogue.

**Example:**

```python
class CentralCorridor(Scene):
    def enter(self):
        print("A Gothon blocks your way.")
        action = input("Choose 'shoot', 'dodge' or 'joke': ")

        if action == 'shoot':
            print("You die.")
            return 'death'
        elif action == 'joke':
            print("You pass!")
            return 'laser_weapon_armory'
        else:
            print("Try again.")
            return 'central_corridor'
```

---

### 7. Iterate and Improve

Now you can:
- Add new features  
- Improve UX  
- Add randomness (like guessing codes)  
- Handle invalid inputs safely  

---

### 8. Final Thoughts & Tips

✅ Always test core logic first before filling in the fluff  
✅ Use comments to design how data flows  
✅ Make each class do one job  
✅ Structure your project with reusable objects  
✅ Think like an engineer and like a player at the same time  

---

## 📚 TL;DR - Game Dev Flow

1. List tasks ➤  
2. Pick a core task ➤  
3. Sketch class structure ➤  
4. Plan logic with comments ➤  
5. Implement core engine/map ➤  
6. Add scene logic ➤  
7. Test each part ➤  
8. Polish & add features  

---

## ✨ Credits

This project was built by applying OOP lessons from *Learn Python the Hard Way*. It taught me how to structure programs, not just games — and how to **think in terms of classes, flow, and responsibility**.