import pyglet
from game import resources, load, physicalobject, player
game_window = pyglet.window.Window(800, 600, "Asteroids")

#Batch Draw
main_batch = pyglet.graphics.Batch()

#Set Labels
score_label = pyglet.text.Label(text="Score: 0", x=10, y=460, batch=main_batch)

player_ship = player.Player(x=400, y=300, batch=main_batch)

game_window.push_handlers(player_ship.key_handler)
game_window.push_handlers(player_ship.on_key_press)

asteroids = load.asteroids(3, player_ship.position, batch=main_batch)

player_lives = load.player_lives(load.lives, batch=main_batch)

game_objects = [player_ship] + asteroids

def update(dt):
    for i in range(len(game_objects)):
        to_add = []

        for j in range(i+1, len(game_objects)):
            obj_1 = game_objects[i]
            obj_2 = game_objects[j]
        #Collision
        if not obj_1.dead and not obj_2.dead:
            if obj_1.collides_with(obj_2):
                obj_1.handle_collision_with(obj_2)
                obj_2.handle_collision_with(obj_1)
        #Add new objects
        for obj in game_objects:
            obj.update(dt)
            to_add.extend(obj.new_objects)
            obj.new_objects = []
            if isinstance(obj, player.Player) and obj.respawn:
                game_window.push_handlers(obj.key_handler)
                game_window.push_handlers(obj.on_key_press)
                obj.respawn = False
                load.lives -= 1
                print("lives: " + str(load.lives))
        #Removal
        for to_remove in [obj for obj in game_objects if obj.dead]:
            to_remove.delete()
            game_objects.remove(to_remove)
        game_objects.extend(to_add)

#Redraw Game Window
@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()

#Runs
if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()