import pygame
import pymunk
import pymunk.pygame_util

print(pygame.__version__)
pygame.init()

#screen
height = 720
width = 1280
screen = pygame.display.set_mode((width, height))

red_value, green_value, blue_value = 255,255,255
pygame.display.set_caption("Simulation")


space = pymunk.Space()
clock = pygame.time.Clock()
FPS = 240
space.gravity = 0, -981  # Horizontal and vertical forces

#------------------------------------------functions

def convert_coordinates(position):
    return position[0], (height-position[1]) #position[0] is an x value, and pos[1] is the y val

def Add_Circle(radius, pos, density):
    body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
    body.position = pos[0], pos[1]
    shape = pymunk.Circle(body, radius)
    shape.elasticity = 1
    shape.density = density
    space.add(body, shape)
    return body, shape

class Bridge_Segment():
    def __init__(self, posA, posB):
        print("defining")
        print(posA, posB)
        self.body = pymunk.Body()
        self.body.body_type = pymunk.Body.STATIC
        self.shape = pymunk.Segment(self.body, posA, posB, 10)
        self.shape.elasticity = 0.5
        space.add(self.body, self.shape)
    def draw(self):
        print("drawing")
        print(self.shape.a, self.shape.b)
        x,y = convert_coordinates(self.shape.a)
        x1,y1 = convert_coordinates(self.shape.b)
        pygame.draw.line(screen, (0,255,0), (int(x), int(y)), (int(x1), int(y1)), 20)

def Add_Bridge_Segment(posA, posB, segment_thickness):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    shape = pymunk.Segment(body, posA, posB, segment_thickness)
    shape.elasticity = 0.5
    space.add(body, shape)
    return body, shape

#-----------------------------------------Adding Objects

First_Body, First_Shape = Add_Circle(10, (width/2, height), 1) #small object for now
Barrier_body, Barrier_Shape = Add_Bridge_Segment((0,10), (width, 10), 5) #creates a barrier for the floor so objects dont fall past the screen

Bridge = [Bridge_Segment((10+i*256, height/3), ((i+1)*256, height/3)) for i in range(5)]

#----------------------------------------rendering window
running_state = True
while running_state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #terminate window when quit
            running_state = False
        else:
            # continue running
            pass
    
    #fills screen with colour
    screen.fill((red_value, green_value, blue_value))

    x,y = convert_coordinates(First_Body.position)
    pygame.draw.circle(screen, (255,0,0), (int(x), int(y)), 10)

    x,y = convert_coordinates(Barrier_Shape.a)
    x1,y1 = convert_coordinates(Barrier_Shape.b)
    pygame.draw.line(screen, (0,0,255), (int(x), int(y)), (int(x1), int(y1)), 10)

    [Bridge_Segment.draw() for Bridge_Segment in Bridge]

    pygame.display.update()
    clock.tick(FPS)
    space.step(1/FPS)
