from __future__ import annotations
from circleshape import CircleShape
from constants import *
import pygame

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from player import Player # Only seen by the IDE, not at runtiume. This is to avoid circular imports since Player imports Shot and Shot imports Player.

class Shot(CircleShape):
    def __init__(self, x:float, y: float, player: Player):
        super().__init__(x, y, SHOT_RADIUS)
        self.player = player

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt