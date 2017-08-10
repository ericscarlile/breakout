from game.shared import GameObject
from game.shared import GameConstants


class Brick(GameObject):
    def __init__(self, position, sprite, game):
        self. __game = game
        self.__hit_points = 100
        self.__lives = 1
        super(Brick, self).__init__(position, GameConstants.BRICK_SIZE, sprite)

    def get_game(self):
        return self.__game

    def is_destroyed(self):
        return self.__lives <= 0

    def get_hit_points(self):
        return self.__hit_points

    def hit(self):
        self.__lives -= 1

    def get_hit_sound(self):
        pass
