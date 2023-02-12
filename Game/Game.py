import pygame
import os

from .GameObject import GameObject, load_assets
from .Rocket import Rocket


class Game(GameObject):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.screen = pygame.display.set_mode(size=(screen_width, screen_height), flags=0, depth=0, display=0, vsync=0)

        self.game_running = True
        self.refresh_rate = 60

        self.background = load_assets('background.png')
        self.rocket = Rocket(y=100, screen=self.screen)

    def event(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running = False

        self.rocket.event()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.rocket.draw()
        pygame.display.update()

    def update(self, dt):
        self.rocket.update(dt)

    def run(self):
        # for running the game

        clock = pygame.time.Clock()
        dt = 0
        while self.game_running:

            self.event()
            self.update(dt)
            self.draw()

            dt = clock.tick(self.refresh_rate) / 1000

        pygame.quit()
