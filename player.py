import config as cfg
from moveable import Moveable


class Player(Moveable):

    def __init__(self, parent, x, y, player_id):

        self.player_id = player_id
        self.name = self.get_name_from_id()

        super().__init__(parent, x, y, self.name, cfg.PLAYER_SPEED)

    def get_name_from_id(self):

        if self.player_id == 0:
            return "pink"

        elif self.player_id == 1:
            return "blue"

        elif self.player_id == 2:
            return "green"

        elif self.player_id == 3:
            return "yellow"
