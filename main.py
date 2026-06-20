import sys

import pygame
from constants import *
from logger import log_state
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
from shot import Shot


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock: pygame.timeClock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", SCORE_HEADER_FONT_SIZE)
    header_surface = font.render(f"Player 1", True, "white") # Could change to "Player 1" and "Player 2" if I add multiplayer

    #create sprite groups and assign them to the Player class - muist do before any Player objects are created
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    dt = 0.0   

    last_score = 0 #to keep track of score to know when to render it. Only render when score changes to save on performance. Not really necessary but it's a good practice to only do work when necessary.
    score_surface = font.render(f"Score: {player.score}", True, "white") # to render with score of 0 for the first time since we only render when the score changes and it starts at 0.
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
                return
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.player.score += 10
                    log_event(f"score_increased: {shot.player.score}")
                    asteroid.split()
                    shot.kill()
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        if player.score != last_score:
            last_score = player.score
            score_surface = font.render(f"Score: {player.score}", True, "white")
        screen.blit(header_surface, (10, 10))
        screen.blit(score_surface, (10, 10 + SCORE_HEADER_FONT_SIZE + 5)) #so the score displays below the player. The +5 is just for extra padding
        pygame.display.flip()
        
        #limit framerate to 60 fps and get delta time
        dt = game_clock.tick(60) /1000
       

if __name__ == "__main__":
    main()
