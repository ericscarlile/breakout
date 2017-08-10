import pygame

from game import *
from game.scenes import *
from game.shared.game_constants import GameConstants


class Breakout:
    def __init__(self):
        self.__lives = 5
        self.__score = 0

        self.__level = Level(self)
        self.__level.load(0)

        self.__pad = Pad((0, 0), 0)
        self.__balls = [
            Ball((0, 0), pygame.image.load(GameConstants.SPRITE_BALL), self)
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
        self.__current_scene = scene

    def get_level(self):
        return self.__level

    def get_score(self):
        return self.__score

    def increase_score(self, score):
        self.__score += score

    def get_lives(self):
        return self.__lives

    def get_balls(self):
        return self.__balls

    def get_pad(self):
        return self.__pad

    def play_sound(self, sound_clip):
        sound = self.__sounds[sound_clip]

        sound.stop()
        sound.play()

    def reduce_lives(self):
        self.__lives -= 1

    def increase_lives(self):
        self.__lives += 1

    def reset(self):
        pass


Breakout().start()
