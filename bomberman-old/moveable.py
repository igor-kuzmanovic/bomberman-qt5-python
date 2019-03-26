from config import *
from sprite import Sprite


class Moveable(Sprite):

    def __init__(self, parent, x, y, name, speed):

        super().__init__(parent, x, y, DYNAMIC_WIDTH, DYNAMIC_HEIGHT)

        self.name = name
        self.set_movie_from_action_direction("idle", "down")
        self.speed = speed
        self.initial_x = x
        self.initial_y = y
        self.potential_x = x
        self.potential_y = y

    def set_movie_from_action_direction(self, action, direction):

        movie_name = action + "_" + direction + "_" + self.name
        self.set_movie(movie_name)

    def try_move_up(self):

        self.set_movie_from_action_direction("walk", "up")

        if self.get_up_y() - self.speed > 0:
            self.potential_y = self.y() - self.speed

    def try_move_down(self):

        self.set_movie_from_action_direction("walk", "down")

        if self.get_down_y() + self.speed < WINDOW_HEIGHT:
            self.potential_y = self.y() + self.speed

    def try_move_left(self):

        self.set_movie_from_action_direction("walk", "left")

        if self.get_left_x() - self.speed > 0:
            self.potential_x = self.x() - self.speed

    def try_move_right(self):

        self.set_movie_from_action_direction("walk", "right")

        if self.get_right_x() + self.speed < WINDOW_WIDTH:
            self.potential_x = self.x() + self.speed

    def update_vertical_position(self):

        self.move(self.x(), self.potential_y)

    def update_horizontal_position(self):

        self.move(self.potential_x, self.y())

    def update_position(self):

        self.update_vertical_position()
        self.update_horizontal_position()

    def revert_vertical_position(self):

        self.potential_y = self.y()

    def revert_horizontal_position(self):

        self.potential_x = self.x()

    def revert_position(self):

        self.revert_vertical_position()
        self.revert_horizontal_position()

    def reset_vertical_position(self):

        self.potential_y = self.initial_y

    def reset_horizontal_position(self):

        self.potential_x = self.inital_x

    def reset_position(self):

        self.reset_vertical_position()
        self.reset_horizontal_position()

    def get_potential_up_y(self):

        return self.potential_y

    def get_potential_down_y(self):

        return self.potential_y + self.height - 1

    def get_potential_left_x(self):

        return self.potential_x

    def get_potential_right_x(self):

        return self.potential_x + self.width - 1

    def check_potential_horizontal_collision(self, target):

        return self.get_potential_left_x() < target.get_right_x() and self.get_potential_right_x() > target.get_left_x()

    def check_potential_vertical_collision(self, target):

        return self.get_potential_up_y() < target.get_down_y() and self.get_potential_down_y() > target.get_up_y()

    def check_potential_collision(self, target):

        return self.check_potential_horizontal_collision(target) and self.check_potential_vertical_collision(target)
