import pygame
from physics import BridgeMember
from config import COLORS, WINDOW_WIDTH, WINDOW_HEIGHT, FPS

def draw_window(screen, objects, bridge_members, font):
    screen.fill(COLORS["bg"])

    # Draw bridge members
    for member in bridge_members:
        x, y = member.pos
        color = COLORS[member.get_status_color()]
        pygame.draw.rect(screen, color, (x, y, member.width, member.height))

    # Draw falling objects
    for obj in objects:
        pygame.draw.circle(screen, COLORS["white"], (int(obj.x), int(obj.y)), obj.size)

    # Force display (optional)
    text = font.render(f"Objects: {len(objects)}", True, COLORS["white"])
    screen.blit(text, (20, 20))

    pygame.display.update()

def init_bridge():
    members = []
    spacing = 100
    y_pos = 500
    for i in range(8):
        x = i * spacing + 50
        members.append(BridgeMember((x, y_pos), 80, 30))
    return members