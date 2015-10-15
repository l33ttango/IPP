# program template for Spaceship
# http://www.codeskulptor.org/#user40_xtHIESFQnY_0.py

import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 0
time = 0
rock_group = set([])
missile_group = set([])
started = False



class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")
soundtrack.set_volume(0.8)

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

def group_collide(sprite_group, other_object):
    for object in set(sprite_group):
        if object.collide(other_object):
            sprite_group.remove(object)            
            return True	
    return False        

def group_group_collide(group1, group2):        
    global rock_group, missile_group
    for sprite in set(group2):
        if group_collide(group1, sprite):
            group2.remove(sprite)
            return True

def process_sprite_group(canvas, sprite_group):
    
    for each_sprite in set(sprite_group): 
        each_sprite.draw(canvas)
        each_sprite.update()
        if each_sprite.lifespan != None and each_sprite.age > each_sprite.lifespan:
            sprite_group.remove(each_sprite)
    
def game_start():
    global score, lives, time, rock_group, missile_group
    if started:
        score = 0
        lives = 3      
        rock_group = set([])
        missile_group = set([])
        soundtrack.play()
    

# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0], vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()        
        
    def draw(self,canvas):
        if self.thrust:
            canvas.draw_image(self.image, (self.image_center[0] + 90, self.image_center[1]), self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        forward_vector = angle_to_vector(self.angle)
        if self.thrust:
            self.vel[0] += 0.2 * forward_vector[0]
            self.vel[1] += 0.2  * forward_vector[1]
        self.angle += self.angle_vel
        self.vel[0] *= 0.98
        self.vel[1] *= 0.98
        self.pos[0] += self.vel[0] 
        self.pos[1] += self.vel[1]
        self.pos[0] = self.pos[0] % WIDTH
        self.pos[1] = self.pos[1] % HEIGHT
        
    def shoot(self):
        # press space bar, shoot missile
        forward_vector = angle_to_vector(self.angle)
        missile_pos = (self.pos[0] + self.radius * forward_vector[0], self.pos[1] + self.radius * forward_vector[1]) 
        missile_vel = (self.vel[0] + 10 * forward_vector[0], self.vel[1] + 10 * forward_vector[1])
        a_missile = Sprite(missile_pos, missile_vel, 0, 0, missile_image, missile_info, missile_sound) 
        missile_group.add(a_missile)
        
    def thrust_on(self, turn_on):        
        if turn_on:
            self.thrust = True
            ship_thrust_sound.play()

        else:
            self.thrust = False
            ship_thrust_sound.rewind()		
            
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang_vel 
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
        
    def update(self):
        
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.angle += self.angle_vel
        self.pos[0] = self.pos[0] % WIDTH
        self.pos[1] = self.pos[1] % HEIGHT
        self.age += 1
        
    def collide(self, other_object):                
        if dist(self.pos, other_object.pos) <= self.radius + other_object.radius:
            return True
        else:
            return False
        
def draw(canvas):
    global time, lives, score, started, rock_group, missile_group
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw score and lives
    canvas.draw_text("lives = " + str(lives), [20, 30], 30, "White")
    canvas.draw_text("score = " + str(score), [650, 30], 30, "White")

    # Signify Game over, reset
    if lives == 0:
        started = False
        canvas.draw_image(splash_image, splash_info.get_center(), splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH / 2, HEIGHT / 2])
        rock_group = set([])
        missile_group = set([])
        soundtrack.rewind()
        

    if group_group_collide(rock_group, missile_group):
       score += 1 

    if group_collide(rock_group, my_ship):
        lives -= 1
        explosion_sound.rewind()
        explosion_sound.play()

    # draw ship and sprites, update ship and sprites
    if started:
        process_sprite_group(canvas, rock_group)
        process_sprite_group(canvas, missile_group)
        my_ship.update()
        my_ship.draw(canvas)    
            
# Handler uses timer to spawn rocks once per sec     
# I played with quite a few different ways to affect the speed of the asteroids. 
# I chose the square root function over a step function because I like the continuous increase in speed.
def rock_spawner():
    if len(rock_group) < 12:
        
        a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, 0, asteroid_image, asteroid_info)
        a_rock.pos[0] = random.randrange(0, WIDTH)
        a_rock.pos[1] = random.randrange(0, HEIGHT)
        a_rock.vel[0] = math.sqrt(score + 1.0) * random.randrange(-20.0, 20.0) / 20.0
        a_rock.vel[1] = math.sqrt(score + 1.0) * random.randrange(-20.0, 20.0) / 20.0
        a_rock.angle_vel = random.randrange(-30.0, 30.0) / 1000.0
        
        if dist([a_rock.pos[0], a_rock.pos[1]], my_ship.pos) > 80:
            rock_group.add(a_rock)
               
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)


# Add key handlers for up, left and right
# left and right control angle of ship, up controls forward thrust	
def keydown(key):
    if key == simplegui.KEY_MAP["up"]:
        my_ship.thrust_on(True)
    elif key == simplegui.KEY_MAP["right"]:
        my_ship.angle_vel = 0.1
    elif key == simplegui.KEY_MAP["left"]:
        my_ship.angle_vel = -0.1
    elif key == simplegui.KEY_MAP["space"]:
        my_ship.shoot()
        
def keyup(key):
    if key == simplegui.KEY_MAP["up"]:
        my_ship.thrust_on(False)
         
    elif key == simplegui.KEY_MAP["right"] or key == simplegui.KEY_MAP["left"]:
        my_ship.angle_vel = 0

def mouse_handler(pos):
    global started
    if not started and WIDTH /4 < pos[0] < 3 * WIDTH / 4:
        if HEIGHT / 4 < pos[1] < 3 * HEIGHT / 4:
            started = True
            game_start()
        
# register handlers
frame.set_draw_handler(draw)

timer = simplegui.create_timer(1000.0, rock_spawner)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(mouse_handler)

# get things rolling
timer.start()
frame.start()
