from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QMovie
import config as cfg


class Resource:
    resources = {}

    @classmethod
    def get_pixmap(cls, resource):

        if resource not in cls.resources:
            cls.resources[resource] = QPixmap('./resources/' + resource + '.png')
            cls.resources[resource].setDevicePixelRatio(cfg.DEFAULT_SPRITE_SIZE / cfg.BLOCK_RESOURCE_SIZE)

        return cls.resources[resource]

    @classmethod
    def get_movie(cls, resource):

        if 'IDLE_UP_PINK' not in cls.resources:
            cls.resources[resource] = QMovie('./resources/' + resource + '.gif')
            cls.resources[resource].setScaledSize(QSize(cfg.MOVEABLE_RESOURCE_WIDTH, cfg.MOVEABLE_RESOURCE_HEIGHT))
            cls.resources[resource].start()

        return cls.resources[resource]
