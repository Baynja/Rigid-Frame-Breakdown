# simulation.py
from config import GRAVITY

class FallingObject:
    def __init__(self, x, mass):
        self.initial_velocity = 0
        self.mass = mass
        self.x = x
        self.y = 0
        self.vel_y = 0
        self.size = 20+0.1*mass
        self.applied = False

    def update(self, dt):
        self.vel_y += self.initial_velocity + GRAVITY * dt
        self.y += self.vel_y * dt

    def get_force(self):
        return self.mass * GRAVITY