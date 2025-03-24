import pygame
import random
from config import *
from simulation import FallingObject, check_collision
from ui import draw_window, init_bridge

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Rigid Frame Breakdown")
font = pygame.font.SysFont("Arial", 20)
clock = pygame.time.Clock()

bridge_members = init_bridge()
falling_objects = []
running = True
simulation_started = False

while running:
    dt = clock.tick(FPS) / 1000  # Convert to seconds
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Press SPACE to add object
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mass = random.choice(OBJECT_MASSES)
                x_pos = random.randint(50, WINDOW_WIDTH - 50)
                falling_objects.append(FallingObject(x_pos, mass))
                if len(falling_objects) >= 3:
                    simulation_started = True

    if simulation_started:
        for obj in falling_objects:
            obj.update(dt)
            check_collision(obj, bridge_members)

    draw_window(screen, falling_objects, bridge_members, font)

pygame.quit()