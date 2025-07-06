import pygame
import random
import copy

from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        random_angle = random.uniform(20, 50)
        if(self.radius > ASTEROID_MIN_RADIUS):

            asteroid1 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
            asteroid1.velocity = self.velocity.rotate(-random_angle) * 1.2

            asteroid2 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
            asteroid2.velocity = self.velocity.rotate(random_angle) * 1.2

