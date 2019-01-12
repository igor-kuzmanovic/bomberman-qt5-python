import config as cfg
from moveable import Moveable


class Enemy(Moveable):

    def __init__(self, parent, x, y):

        self.name = "enemy"

        super().__init__(parent, x, y, self.name, cfg.ENEMY_SPEED)
