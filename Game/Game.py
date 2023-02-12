import pygame


class Game:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.screen = pygame.display.set_mode(size=(screen_width, screen_height), flags=0, depth=0, display=0, vsync=0)

        self.game_running = True

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running = False

    def draw(self):
        self.screen.fill("Black")

    def update(self):
        pass

    def run(self):
        # for running the game

        clock = pygame.time.Clock()
        while self.game_running:

            self.event()
            self.update()
            self.draw()
