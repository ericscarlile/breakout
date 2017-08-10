class GameObject:
    def __init__(self, position, size, sprite):
        self.__position = position
        self.__size = size
        self.__sprite = sprite

    def set_position(self, position):
        self.__position = position

    def get_position(self):
        return self.__position

    def get_size(self):
        return self.__size

    def get_sprite(self):
        return self.__sprite

    def intersects(self, other):
        pass
