import pygame

from game import *
from game.scenes import *
from game.shared import GameConstants


class Breakout:
    def __init__(self):
        self.__lives = 5
        self.__score = 0

        self.__level = Level(self)
        self.__level.load(0)

        self.__pad = Pad((0, 0), 0)
        self.__balls = [
            Ball((0, 0), 0, self)
        ]

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Breakout!")

        self.__clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(GameConstants.SCREEN_SIZE, pygame.DOUBLEBUF)
        pygame.mouse.set_visible(0)

        self.__scenes = (
            PlayingGameScene(self),
            GameOverScene(self),
            HighscoreScene(self),
            MenuScene(self)
        )

        self.__current_scene = 0

        self.__sounds = ()

    def start(self):
        while True:
            self.__clock.tick(60)
            self.screen.fill((0, 0, 0))

            current_scene = self.__scenes[self.__current_scene]
            current_scene.handle_events(pygame.event.get())
            current_scene.render()

            pygame.display.update()

    def change_scene(self, scene):
        pass

    def get_level(self):
        pass

    def get_score(self):
        pass

    def increase_score(self, score):
        pass

    def get_lives(self):
        pass

    def get_balls(self):
        pass

    def get_pad(self):
        pass

    def play_sound(self, sound_clip):
        pass

    def reduce_lives(self):
        pass

    def increase_lives(self):
        pass

    def reset(self):
        pass


Breakout().start()
