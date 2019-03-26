from PyQt5.QtCore import Qt
from config import *
from moveable import Moveable


class Player(Moveable):

    def __init__(self, parent, x, y, player_id):

        self.player_id = player_id
        self.name = self.get_name_from_id()

        super().__init__(parent, x, y, self.name, PLAYER_SPEED)

        self.is_alive = True
        self.lives = PLAYER_LIVES
        self.respawn_time = 0
        self.key_up, self.key_down, self.key_left, self.key_right = self.get_keys_from_id()

    def get_name_from_id(self):

        if self.player_id == PLAYER_1:
            return PLAYER_1_NAME

        elif self.player_id == PLAYER_2:
            return PLAYER_2_NAME

        elif self.player_id == PLAYER_3:
            return PLAYER_3_NAME

        elif self.player_id == PLAYER_4:
            return PLAYER_4_NAME

    def get_keys_from_id(self):

        if self.player_id == PLAYER_1:
            return Qt.Key_W, Qt.Key_S, Qt.Key_A, Qt.Key_D

        elif self.player_id == PLAYER_2:
            return Qt.Key_Up, Qt.Key_Down, Qt.Key_Left, Qt.Key_Right

    def kill(self):

        if self.is_alive is True:
            self.is_alive = False
            self.hide()
            self.lives -= 1
            self.reset_position()
            self.respawn_time = PLAYER_RESPAWN_TIME

    def respawn(self):

        if self.respawn_time < PLAYER_RESPAWN_TIME / 2 and self.respawn_time % 2 == 0:
            self.show()
        else:
            self.hide()

        if self.lives and self.is_alive is False and self.respawn_time <= 0:
            self.is_alive = True
            self.show()

    def decrement_respawn_time(self):

        self.respawn_time -= PLAYER_RESPAWN_TIME_STEP

    def try_move(self, key):

        if key == self.key_up:
            self.try_move_up()

        elif key == self.key_down:
            self.try_move_down()

        elif key == self.key_left:
            self.try_move_left()

        elif key == self.key_right:
            self.try_move_right()

    def set_idle_movie(self):

        if self.direction == UP:
            self.set_movie_from_action_direction("idle", "up")

        elif self.direction == DOWN:
            self.set_movie_from_action_direction("idle", "down")

        elif self.direction == LEFT:
            self.set_movie_from_action_direction("idle", "left")

        elif self.direction == RIGHT:
            self.set_movie_from_action_direction("idle", "right")
