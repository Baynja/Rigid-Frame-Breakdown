# simulation.py
from config import GRAVITY

class FallingObject:
    def __init__(self, x, mass):
        self.mass = mass
        self.x = x
        self.y = 0
        self.vel_y = 0
        self.size = 20
        self.applied = False

    def update(self, dt):
        self.vel_y += GRAVITY * dt
        self.y += self.vel_y * dt

    def get_force(self):
        return self.mass * GRAVITY