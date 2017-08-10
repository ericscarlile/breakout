import os
import fileinput
import pygame

from game.bricks import *
from game.shared import GameConstants


class Level:
    def __init__(self, game):
        self.__game = game
        self.__bricks = []
        self.__amount_of_bricks_left = 0
        self.__current_level = 0

    def get_bricks(self):
        return self.__bricks

    def get_amount_of_bricks_left(self):
        return self.__amout_of_bricks_left

    def brick_hit(self):
        self.__amout_of_bricks_left -= 1

    def load_next_level(self):
        pass

    def load(self, level):
        self.__current_level = level
        self.__bricks = []

        x, y = 0, 0

        for line in fileinput.input(os.path.join("assets", "Levels", "level{}.dat".format(str(level)))):
            for current_brick in line:
                if current_brick == "1":
                    brick = Brick([x, y], pygame.image.load(GameConstants.SPRITE_BRICK), self.__game)
                    self.__bricks.append(brick)
                    self.__amount_of_bricks_left += 1
                elif current_brick == "2":
                    brick = SpeedBrick([x, y], pygame.image.load(GameConstants.SPRITE_SPEED_BRICK), self.__game)
                    self.__bricks.append(brick)
                    self.__amount_of_bricks_left += 1
                elif current_brick == "3":
                    brick = LifeBrick([x, y], pygame.image.load(GameConstants.SPRITE_LIFE_BRICK), self.__game)
                    self.__bricks.append(brick)
                    self.__amount_of_bricks_left += 1

                x += GameConstants.BRICK_SIZE[0]

            x = 0
            y += GameConstants.BRICK_SIZE[1]