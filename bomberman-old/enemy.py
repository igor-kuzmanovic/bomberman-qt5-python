from random import randint
from config import *
from moveable import Moveable


class Enemy(Moveable):

    def __init__(self, parent, x, y):

        super().__init__(parent, x, y, "enemy", ENEMY_SPEED)

        self.direction = -1
        self.change_direction()

    def change_direction(self):

        old_direction = self.direction

        while old_direction == self.direction:
            self.direction = randint(0, 3)

    def try_move_in_direction(self):

        if self.direction == UP:
            self.try_move_up()

        elif self.direction == DOWN:
            self.try_move_down()

        elif self.direction == LEFT:
            self.try_move_left()

        elif self.direction == RIGHT:
            self.try_move_right()
