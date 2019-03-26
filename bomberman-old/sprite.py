from PyQt5.QtWidgets import QLabel
from resource import Resource


class Sprite(QLabel):

    def __init__(self, parent, x, y, width, height):

        super().__init__(parent)

        self.width = width
        self.height = height
        self.setGeometry(x, y, self.width, self.height)

    def set_pixmap(self, name):

        if self.pixmap() is None or name not in self.get_pixmap_filename():
            pixmap = Resource.get_pixmap(name)
            self.setPixmap(pixmap)

    def get_pixmap_filename(self):

        if self.pixmap():
            return self.pixmap().fileName()
        else:
            return ''

    def set_movie(self, name):

        if name not in self.get_movie_filename():
            movie = Resource.get_movie(name)
            self.setMovie(movie)

    def get_movie_filename(self):

        if self.movie():
            return self.movie().fileName()
        else:
            return ''

    def get_up_y(self):

        return self.y()

    def get_down_y(self):

        return self.y() + self.height - 1

    def get_left_x(self):

        return self.x()

    def get_right_x(self):

        return self.x() + self.width - 1

    def check_horizontal_collision(self, target):

        return self.get_left_x() < target.get_right_x() and self.get_right_x() > target.get_left_x()

    def check_vertical_collision(self, target):

        return self.get_up_y() < target.get_down_y() and self.get_down_y() > target.get_up_y()

    def check_collision(self, target):

        return self.check_horizontal_collision(target) and self.check_vertical_collision(target)
