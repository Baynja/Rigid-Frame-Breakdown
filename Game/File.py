import pygame
import pymunk
import pymunk.pygame_util

print(pygame.__version__)
pygame.init()

space = pymunk.Space()
clock = pygame.time.Clock()
FPS = 60

#screen
height = 720
width = 1024
screen = pygame.display.set_mode((width, height))

red_value, green_value, blue_value = 0,255,255
pygame.display.set_caption("Simulation")

space = pymunk.Space()
space.gravity = 0, -981  # Horizontal and vertical forces

def Add_Circle(radius, pos, density):
    body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
    body.position = pos[0], pos[1]
    shape = pymunk.Circle(body, radius)
    shape.elasticity = 1
    shape.density = density
    space.add(body, shape)
    return body, shape

def Add_Bridge_Segment(posA, posB, segment_thickness):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    shape = pymunk.Segment(body, posA, posB, segment_thickness)
    shape.elasticity = 0.5
    space.add(body, shape)
    return body, shape


def convert_coordinates(position):
    return position[0], (height-position[1]) #position[0] is an x value, and pos[1] is the y val


First_Body, First_Shape = Add_Circle(10, (width/2, height/2), 1)
First_Segment, Segment_Shape = Add_Bridge_Segment((0,500), (width, 10), 10)
print(convert_coordinates(Segment_Shape.b))

#rendering window
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
    pygame.draw.circle(screen, (255,255,0), (int(x), int(y)), 10)

    x,y = convert_coordinates(Segment_Shape.a)
    x1,y1 = convert_coordinates(Segment_Shape.b)
    pygame.draw.line(screen, (0,0,0), (int(x), int(y)), (int(x1), int(y1)), 10)

    pygame.display.update()
    clock.tick(FPS)
    space.step(1/FPS)
