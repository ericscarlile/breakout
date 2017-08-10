class Scene:
    def __init__(self, game):
        self.__game = game
        self.__texts = []

    def render(self):
        pass

    def get_game(self):
        return self.__game

    def handle_events(self, events):
        pass

    def clear_text(self):
        self.__texts = []

    def add_text(self, string, x = 0, y = 0, color = [255, 255, 255], background = [0, 0, 0], size = 17):
        pass

