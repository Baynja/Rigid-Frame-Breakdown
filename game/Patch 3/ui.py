# ui.py
import pygame
from config import COLORS, WINDOW_WIDTH

class Button:
    def __init__(self, x, y, w, h, text, action):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.action = action
        self.hovered = False

    def draw(self, screen, font):
        color = COLORS["button_hover"] if self.hovered else COLORS["button"]
        pygame.draw.rect(screen, color, self.rect)
        text_surf = font.render(self.text, True, COLORS["white"])
        screen.blit(text_surf, text_surf.get_rect(center=self.rect.center))

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            self.action()

def draw_window(screen, objects, bridge_members, font, log_lines):
    screen.fill(COLORS["bg"])
    
    for member in bridge_members:
        x, y = member.pos
        color = COLORS[member.get_status_color()]
        pygame.draw.rect(screen, color, (x, y, member.width, member.height))

    for obj in objects:
        pygame.draw.circle(screen, COLORS["white"], (int(obj.x), int(obj.y)), obj.size)
        text_surf = font.render(str(obj.mass), True, COLORS["black"])
        screen.blit(text_surf, text_surf.get_rect(center = (obj.x, obj.y)))

    y_offset = 10
    for line in log_lines[-6:]:  # show last 6 lines
        screen.blit(font.render(line, True, COLORS["white"]), (10, y_offset))
        y_offset += 20