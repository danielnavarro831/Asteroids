import math
from pyglet.window import key
from pyglet.media import player
from . import physicalobject, resources, bullet
from game.resources import fireSFX
import pyglet

player = pyglet.media.Player()

class Player(physicalobject.PhysicalObject):

    def __init__(self, *args, **kwargs):
        super().__init__(img=resources.player_image, *args, **kwargs)

        self.thrust = 30.0
        self.rotate_speed = 200.0

        self.engine_sprite = pyglet.sprite.Sprite(img=resources.engine_image, *args, **kwargs)
        self.engine_sprite.visible = False

        self.key_handler = key.KeyStateHandler()

        self.bullet_speed = 100.0
        self.reacts_to_bullets = False

    def fire(self):
        angle_radians = -math.radians(self.rotation)
        ship_radius = self.image.width/2
        bullet_x = self.x + math.cos(angle_radians) * ship_radius
        bullet_y = self.y + math.sin(angle_radians) * ship_radius
        new_bullet = bullet.Bullet(bullet_x, bullet_y, batch=self.batch)
        bullet_vx = (
            self.velocity_x +
            math.cos(angle_radians) * self.bullet_speed
        )
        bullet_vy = (
            self.velocity_y +
            math.sin(angle_radians) * self.bullet_speed
        )
        new_bullet.velocity_x = bullet_vx
        new_bullet.velocity_y = bullet_vy
        self.new_objects.append(new_bullet)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            self.fire()
            resources.fireSFX()

    def delete(self):
        self.engine_sprite.delete()
        super(Player, self).delete()

    def update(self, dt):
        super(Player, self).update(dt)

        if self.key_handler[key.LEFT]:
            self.rotation -= self.rotate_speed * dt
        if self.key_handler[key.RIGHT]:
            self.rotation += self.rotate_speed * dt
        if self.key_handler[key.UP]:
            angle_radians = -math.radians(self.rotation)
            force_x = math.cos(angle_radians) * self.thrust * dt
            force_y = math.sin(angle_radians) * self.thrust * dt
            self.velocity_x += force_x
            self.velocity_y += force_y
            self.engine_sprite.rotation = self.rotation
            self.engine_sprite.x = self.x
            self.engine_sprite.y = self.y
            self.engine_sprite.visible = True
        else:
            self.engine_sprite.visible = False
