
import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot
class Player(CircleShape):
    containers: tuple[pygame.sprite.Group, ...]
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation: int = 0
        self.cooldown_timer: float = 0.0
        self.score: int = 0
        self.lives: int = PLAYER_LIVES

        # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen: pygame.SurfaceType) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: float) -> None:
        self.cooldown_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # enter here to rotate left
            Player.rotate(self, -dt)
        if keys[pygame.K_d]:
            # enter here to rotate right
            Player.rotate(self, dt)
        if keys[pygame.K_w]:
            # enter here to go forward
            Player.move(self, dt)
        if keys[pygame.K_s]:
            # enter here to go backward
            Player.move(self, -dt)
        if keys[pygame.K_SPACE]:
            # enter here to shoot
            Player.shoot(self)


        
    
    def move(self, dt: float) -> None:
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self) -> None:
        if self.cooldown_timer > 0:
            return
        self.cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        current_shot = Shot(self.position.x, self.position.y, self)
        current_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED