from config import *
from sprite import Sprite


class Block(Sprite):

    def __init__(self, parent, x, y, block_type):

        super().__init__(parent, x, y, STATIC_WIDTH, STATIC_HEIGHT)

        self.block_type = block_type
        self.block_name = self.get_name_from_type()
        self.set_pixmap(self.block_name)

    def get_name_from_type(self):

        if self.block_type == GRASS:
            return "grass"

        elif self.block_type == WALL:
            return "brick"

        elif self.block_type == BRICK:
            return "wood"
