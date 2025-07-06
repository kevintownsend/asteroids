import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    fps_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)

    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for o in updatable:
            o.update(dt)
        for asteroid in asteroids:
            if(player.collision(asteroid)):
                print("Game over!")
                return
            for shot in shots:
                if(shot.collision(asteroid)):
                    shot.kill()
                    asteroid.split()
        for o in drawable:
            o.draw(screen)
        pygame.display.flip()
        dt = fps_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
