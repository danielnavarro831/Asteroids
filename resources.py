import pyglet

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2


# Tell pyglet where to find the resources
pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

# Load the resources
player_image = pyglet.resource.image("player.png")
center_image(player_image)

bullet_image = pyglet.resource.image("bullet.png")
center_image(bullet_image)

asteroid_image = pyglet.resource.image("asteroid.png")
center_image(asteroid_image)

engine_image = pyglet.resource.image("engine_flame.png")
engine_image.anchor_x = engine_image.width * 1.5 
engine_image.anchor_y = engine_image.height / 2

bullet_sound = pyglet.media.load('C:\\Users\\Daniel\\workspace\\Asteroids\\resources\\bullet.wav')

def fireSFX():
    bullet_sound.play()