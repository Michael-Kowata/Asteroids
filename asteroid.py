import pygame
from circleshape import CircleShape
import random 
from constants import ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")

        # randomize the angle of the split
        random_angle = random.uniform(20, 50)

        vector1 = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_astroid = Asteroid(self.position.x, self.position.y, new_radius)
        new_astroid.velocity = vector1 * 1.2
        new_astroid = Asteroid(self.position.x, self.position.y, new_radius)
        new_astroid.velocity = vector2 * 1.2


