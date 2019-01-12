from random import randint
import config as cfg
from sprite import Sprite


class Moveable(Sprite):

    def __init__(self, parent, x, y, name, speed):

        super().__init__(parent, x, y, cfg.MOVEABLE_WIDTH, cfg.MOVEABLE_HEIGHT)

        self.name = name
        self.set_movie_from_action_direction("idle", "down")
        self.speed = speed
        self.initial_x = x
        self.initial_y = y
        self.temp_x = x
        self.temp_y = y
        self.is_alive = True
        self.respawn_timer = 0
        self.direction = randint(0, 3)

    def set_movie_from_action_direction(self, action, direction):

        movie_name = action + "_" + direction + "_" + self.name
        self.set_movie(movie_name)

    def kill(self):

        if self.is_alive is True:
            self.is_alive = False
            self.hide()
            self.temp_x = self.initial_x
            self.temp_y = self.initial_y
            self.move(self.initial_x, self.initial_y)
            self.respawn_timer = cfg.GAME_SPEED * cfg.RESPAWN_TIME

    def respawn(self):

        if self.is_alive is False and self.respawn_timer <= 0:
            self.is_alive = True
            self.show()

    def try_move_up(self):

        self.set_movie_from_action_direction("walk", "up")

        if self.get_up_y() - self.speed > 0:
            self.temp_y = self.y() - self.speed

    def try_move_down(self):

        self.set_movie_from_action_direction("walk", "down")

        if self.get_down_y() + self.speed < cfg.WINDOW_HEIGHT:
            self.temp_y = self.y() + self.speed

    def try_move_left(self):

        self.set_movie_from_action_direction("walk", "left")

        if self.get_left_x() - self.speed > 0:
            self.temp_x = self.x() - self.speed

    def try_move_right(self):

        self.set_movie_from_action_direction("walk", "right")

        if self.get_right_x() + self.speed < cfg.WINDOW_WIDTH:
            self.temp_x = self.x() + self.speed

    def update_position(self):

        self.move(self.temp_x, self.temp_y)

    def revert_position(self):

        self.temp_x = self.x()
        self.temp_y = self.y()

    def change_direction(self):

        old_direction = self.direction
        while old_direction == self.direction:
            self.direction = randint(0, 3)

    def get_temp_up_y(self):

        return self.temp_y

    def get_temp_down_y(self):

        return self.temp_y + self.height - 1

    def get_temp_left_x(self):

        return self.temp_x

    def get_temp_right_x(self):

        return self.temp_x + self.width - 1

    def check_temp_collision(self, target):

        if self.get_temp_left_x() < target.get_right_x() \
                and self.get_temp_right_x() > target.get_left_x() \
                and self.get_temp_up_y() < target.get_down_y() \
                and self.get_temp_down_y() > target.get_up_y():
            return True

        return False
