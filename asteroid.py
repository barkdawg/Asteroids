import pygame
import circleshape
from circleshape import CircleShape
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self. radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        new_velocity_vector_1 = self.velocity.rotate(random_angle)
        new_velocity_vector_2 = self.velocity.rotate(-random_angle)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        Asteroid(self.position.x, self.position.y, new_asteroid_radius).velocity = new_velocity_vector_1 * 1.2
        Asteroid(self.position.x, self.position.y, new_asteroid_radius).velocity = new_velocity_vector_2 * 1.2

