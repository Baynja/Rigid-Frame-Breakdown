import pygame
print(pygame.__version__)
pygame.init()

#screen
height = 720
width = 1024
screen = pygame.display.set_mode((width, height))

red_value, green_value, blue_value = 0,255,255
pygame.display.set_caption("game")

#display image
def create_obj(img, imgpos):
    screen.blit(img, imgpos)

#display text
def create_text(text, font, colour, coordinates):
    text_img = font.render(text, False, colour)
    screen.blit(text_img, coordinates)

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

    pygame.display.update()