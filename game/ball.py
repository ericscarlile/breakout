import pygame
from game.shared import *


class Ball(GameObject):
    def __init__(self, position, sprite, game):
        self.__game = game
        self.__speed = 3
        self.__increment = [2, 2]
        self.__direction = [1, 1]
        self.__in_motion = 0

        super(Ball, self).__init__(position, GameConstants.BALL_SIZE, sprite)

    def set_speed(self, new_speed):
        self.__speed = new_speed

    def reset_speed(self):
        self.set_speed(3)

    def get_speed(self):
        return self.__speed

    def is_in_motion(self):
        return self.__in_motion

    def set_motion(self, is_moving):
        self.__in_motion = is_moving
        self.reset_speed()

    def change_direction(self, game_object):
        position = self.get_position()
        size = self.get_size()
        object_position = game_object.get_position()
        object_size = game_object.get_size()

        if position[1] > object_position[1] \
                and position[1] < object_position[1] + object_size[1] \
                and position[0] > object_position[0] \
                and position[0] < object_position[0] + object_size[1]:
            self.set_position((position[0], object_position[1] + object_size[1]))
            self.__direction[1] *= -1

        elif position[1] + size[1] > object_position[1] \
                and position[1] + size[1] < object_position[1] + object_size[1] \
                and position[0] > object_position[0] \
                and position[0] < object_position[0] + object_size[0]:
            self.set_position((position[0], object_position[1] - object_size[1]))
            self.__direction[1] *= -1

        elif position[0] + size[0] > object_position[0] \
                and position[0] + size[0] < object_position[0] + object_size[0]:
            self.set_position((object_position[0] - size[0], position[1]))
            self.__direction[0] *= -1

        else:
            self.set_position((object_position[0] + object_size[0], position[1]))
            self.__direction[0] *= -1
            self.__direction[1] *= -1

    def update_position(self):
        position = self.get_position()
        size = self.get_size()

        new_position = [position[0] + (self.__increment[0] * self.__speed) * self.__direction[0],
                        position[1] + (self.__increment[1] * self.__speed) * self.__direction[1]]

        if new_position[0] + size[0] >= GameConstants.SCREEN_SIZE[0]:
            self.__direction[0] *= -1
            new_position = [GameConstants.SCREEN_SIZE[0] - size[0], new_position[1]]

        if new_position[0] <= 0:
            self.__direction[0] *= -1
            new_position = [0, new_position[1]]

        if new_position[1] + size[1] >= GameConstants.SCREEN_SIZE[1]:
            self.__direction[1] *= -1
            new_position = [new_position[0], GameConstants.SCREEN_SIZE[1] - size[1]]

        if new_position[1] <= 0:
            self.__direction[1] *= -1
            new_position = [new_position[0], 0]

        self.set_position(new_position)

    def is_ball_dead(self):
        pass
