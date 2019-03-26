from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QMovie, QColor, QRgba64
from config import *


class Resource:
    resources = {}

    @classmethod
    def get_pixmap(cls, resource):

        if resource not in cls.resources:
            cls.resources[resource] = QPixmap('./resources/' + resource + '.png')
            cls.resources[resource].setDevicePixelRatio(PIXMAP_SIZE / STATIC_SIZE)

        return cls.resources[resource]

    @classmethod
    def get_movie(cls, resource):

        if 'IDLE_UP_PINK' not in cls.resources:
            cls.resources[resource] = QMovie('./resources/' + resource + '.gif')
            cls.resources[resource].setScaledSize(QSize(MOVIE_WIDTH, MOVIE_HEIGHT))
            cls.resources[resource].start()

        return cls.resources[resource]
