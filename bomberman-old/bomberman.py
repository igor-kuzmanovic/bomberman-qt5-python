from numpy import zeros, array
from random import random
from sys import argv, exit
from time import sleep
from threading import Timer
from math import floor
from itertools import chain
from PyQt5.QtCore import Qt, QThread, QTimer, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QDesktopWidget
from PyQt5.QtGui import QPixmap, QColor, QMovie
import config as cfg
from board import Board
from game import Game
from key_notifier import KeyNotifier


class Bomberman(QWidget):

    def __init__(self):

        super().__init__()

        self.initialize_window()

        self.board = Board(self)
        self.show()

        self.key_notifier = KeyNotifier()

        self.game = Game(self, self.board, self.key_notifier)
        self.game.start()

    def initialize_window(self):

        screen_size = QDesktopWidget().screenGeometry()
        screen_width = screen_size.width()
        screen_height = screen_size.height()

        self.setWindowTitle('Bomberman')
        self.setGeometry((screen_width - cfg.WINDOW_WIDTH) / 2,
                         (screen_height - cfg.WINDOW_HEIGHT) / 2,
                         cfg.WINDOW_WIDTH,
                         cfg.WINDOW_HEIGHT)

    def keyPressEvent(self, event):

        self.key_notifier.add_key(event.key())

    def keyReleaseEvent(self, event):

        self.key_notifier.rem_key(event.key())

    def closeEvent(self, event):

        self.key_notifier.die()


if __name__ == '__main__':

    app = QApplication(argv)
    ex = Bomberman()
    exit(app.exec_())
