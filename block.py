import config as cfg
from sprite import Sprite


class Block(Sprite):

    def __init__(self, parent, x, y, block_type):

        super().__init__(parent, x, y, cfg.BLOCK_WIDTH, cfg.BLOCK_HEIGHT)

        self.block_type = block_type
        self.block_name = self.get_name_from_type()
        self.set_pixmap(self.block_name)

    def get_name_from_type(self):

        if self.block_type == cfg.GRASS:
            return "grass"

        elif self.block_type == cfg.WALL:
            return "brick"

        elif self.block_type == cfg.BRICK:
            return "wood"
