import pygame
import os


def load_assets(image, alpha=False, scale=(1024, 1024)):
    main_dir = os.path.abspath(os.path.dirname(__file__))
    assets_dir = os.path.join(main_dir, 'assets')
    background_path = os.path.join(assets_dir, image)

    x = None  # Image
    if alpha:
        x = pygame.image.load(background_path).convert_alpha()
    else:
        x = pygame.image.load(background_path).convert()

    return pygame.transform.scale(x, scale)


class GameObject(object):
    def __init__(self):
        pass

    def event(self):
        print("Not overloaded")

    def update(self, dt):
        print("Not overloaded")

    def draw(self):
        print("Not overloaded")
