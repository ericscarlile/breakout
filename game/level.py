class Level:
    def __init__(self, game):
        self.__game = game
        self.__bricks = []
        self.__amout_of_bricks_left = 0
        self.__current_level = 0

    def get_bricks(self):
        pass

    def get_amount_of_bricks_left(self):
        return self.__amout_of_bricks_left

    def brick_hit(self):
        self.__amout_of_bricks_left -= 1

    def load_next_level(self):
        pass

    def load(self, level):
        pass