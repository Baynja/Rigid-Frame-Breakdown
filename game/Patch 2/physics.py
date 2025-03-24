import random
from config import RESISTIVE_FORCE_RANGE

class BridgeMember:
    def __init__(self, pos, width, height):
        self.pos = pos
        self.width = width
        self.height = height
        self.resist_force = random.randint(*RESISTIVE_FORCE_RANGE)
        self.current_force = 0

    def apply_force(self, force):
        self.current_force += force
        return self.is_broken()

    def is_broken(self):
        percent = self.current_force / self.resist_force
        return percent >= 1

    def get_status_color(self):
        percent = self.current_force / self.resist_force
        if percent > 0.8:
            return "green"
        elif percent > 0.3:
            return "yellow"
        else:
            return "red"