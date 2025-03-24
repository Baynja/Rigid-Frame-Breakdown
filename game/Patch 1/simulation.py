from physics import BridgeMember
from config import OBJECT_MASSES, GRAVITY

class FallingObject:
    def __init__(self, x, mass):
        self.mass = mass
        self.x = x
        self.y = 0
        self.vel_y = 0
        self.size = 20

    def update(self, dt):
        self.vel_y += GRAVITY * dt
        self.y += self.vel_y * dt

    def get_force(self):
        return self.mass * GRAVITY

def check_collision(obj, bridge_members):
    for member in bridge_members:
        x, y = member.pos
        if x < obj.x < x + member.width and obj.y >= y:
            broken = member.apply_force(obj.get_force())
            return broken
    return False