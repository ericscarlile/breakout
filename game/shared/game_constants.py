import os


class GameConstants:
    SCREEN_SIZE = [800, 600]
    BRICK_SIZE = [100, 30]
    BALL_SIZE = [16, 16]
    PAD_SIZE = [139, 13]

    SPRITE_BALL = os.path.join("Assets", "ball.png")
    SPRITE_BRICK = os.path.join("Assets", "standard_brick.png")
    SPRITE_SPEED_BRICK = os.path.join("Assets", "speed_brick.png")
    SPRITE_LIFE_BRICK = os.path.join("Assets", "life_brick.png")