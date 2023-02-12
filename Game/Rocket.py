from .GameObject import GameObject, load_assets
import pygame
import math


class Rocket(GameObject):
    def __init__(self, y, screen):
        super().__init__()
        self.y = y  # The y location
        self.v = 0  # The velocity
        self.a = -1  # The acceleration

        self.screen = screen  # The screen to blit on

        self.image = load_assets('rocket.png', True, (240, 240))

    def event(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.v = -50
            self.a = -50

    def update(self, dt):

        angle = 0
        if self.v * self.a > 0:
            self.image = pygame.transform.rotate(self.image, angle)
        self.a -= (self.a - 9.8) / 3
        self.v += self.a * dt
        self.y += self.v * dt

        # self.image = pygame.transform.scale(self.image, (math.e ** (self.y / 100), math.e ** (self.y / 100)))

    def draw(self):
        # draw this on a screen
        self.image.get_rect().center = self.screen.get_rect().center
        self.screen.blit(self.image, self.image.get_rect())
