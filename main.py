#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Game import Game
import pygame


def main():
    pygame.init()

    game = Game.Game(1024, 1024)
    game.run()


if __name__ == '__main__':
    main()
