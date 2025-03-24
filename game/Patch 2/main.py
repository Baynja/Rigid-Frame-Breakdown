# main.py
import pygame
import random
from config import *
from simulation import FallingObject
from physics import BridgeMember
from logger import write_log, save_log_file, log, predict_failures
from ui import Button, draw_window

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Rigid Frame Breakdown")
font = pygame.font.SysFont("Arial", 18)
clock = pygame.time.Clock()

# Setup bridge
def init_bridge():
    members = []
    spacing = 100
    y_pos = 500
    for i in range(8):
        members.append(BridgeMember((i * spacing + 50, y_pos), 80, 30))
    return members

bridge_members = init_bridge()
falling_objects = []
simulation_started = False

# Button actions
def start_sim():
    global simulation_started
    if len(falling_objects) >= 3:
        simulation_started = True
        write_log("Simulation started")

def stop_sim():
    global simulation_started
    simulation_started = False
    write_log("Simulation stopped")

def undo_last():
    if falling_objects:
        falling_objects.pop()
        write_log("Last object removed")

def reset_all():
    global bridge_members, falling_objects, simulation_started
    bridge_members = init_bridge()
    falling_objects.clear()
    simulation_started = False
    write_log("System reset")

# Buttons
buttons = [
    Button(820, 20, 150, 30, "Start", start_sim),
    Button(820, 60, 150, 30, "Stop", stop_sim),
    Button(820, 100, 150, 30, "Undo", undo_last),
    Button(820, 140, 150, 30, "Reset", reset_all),
]

running = True
while running:
    dt = clock.tick(FPS) / 1000  # delta time
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_log_file()
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for b in buttons:
                b.check_click(pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mass = random.choice(OBJECT_MASSES)
                x_pos = random.randint(50, 750)
                obj = FallingObject(x_pos, mass)
                falling_objects.append(obj)
                write_log(f"Object added: {mass} kg")

    # Hover effect
    mouse_pos = pygame.mouse.get_pos()
    for b in buttons:
        b.hovered = b.rect.collidepoint(mouse_pos)

    # Update physics
    if simulation_started:
        for obj in falling_objects:
            obj.update(dt)
            for member in bridge_members:
                x, y = member.pos
                if x < obj.x < x + member.width and obj.y >= y and not obj.applied:
                    force = obj.get_force()
                    member.apply_force(force)
                    obj.applied = True
                    write_log(f"Force {round(force)}N applied at member {bridge_members.index(member)}")

    draw_window(screen, falling_objects, bridge_members, font, log)
    for b in buttons:
        b.draw(screen, font)
    pygame.display.update()

pygame.quit()