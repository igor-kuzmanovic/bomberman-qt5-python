from random import random
from sys import argv, exit
from time import sleep
from threading import Timer
from math import floor
from numpy import array, zeros, count_nonzero
from PyQt5.QtCore import Qt, QThread, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QDesktopWidget
from PyQt5.QtGui import QPixmap, QColor, QMovie
import config as cfg
from block import Block
from player import Player
from enemy import Enemy
from bomb import Bomb


class Board(QWidget):

    def __init__(self, parent):

        super().__init__(parent)

        self.initialize_window()

        self.template = array([['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                               ['W', 'P', 'R', '/', '/', '/', '/', '/', '/', '/', '/', '/', '/', '/', 'R', 'P', 'W'],
                               ['W', 'R', 'W', '/', 'W', '/', 'W', '/', 'W', '/', 'W', '/', 'W', '/', 'W', 'R', 'W'],
                               ['W', '/', '/', '/', '/', '/', '/', '/', '/', '/', '/', '/', '/', '/', '/', '/', 'W'],
                               ['W', '/', 'W', '/', 'W', '/', 'W', '/', 'W', '/', 'W', '/', 'W', '/', 'W', '/', 'W'],
                               ['W', '/', '/', '/', '/', '/', '/', '/', '/', '/', '/', '/', '/', '/', '/', '/', 'W'],
                               ['W', '/', 'W', '/', 'W', '/', 'W', '/', 'W', '/', 'W', '/', 'W', '/', 'W', '/', 'W'],
                               ['W', '/', '/', '/', '/', '/', '/', '/', '/', '/', '/', '/', '/', '/', '/', '/', 'W'],
                               ['W', '/', 'W', '/', 'W', '/', 'W', '/', 'W', '/', 'W', '/', 'W', '/', 'W', '/', 'W'],
                               ['W', '/', '/', '/', '/', '/', '/', '/', '/', '/', '/', '/', '/', '/', '/', '/', 'W'],
                               ['W', 'R', 'W', '/', 'W', '/', 'W', '/', 'W', '/', 'W', '/', 'W', '/', 'W', 'R', 'W'],
                               ['W', 'P', 'R', '/', '/', '/', '/', '/', '/', '/', '/', '/', '/', '/', 'R', 'P', 'W'],
                               ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]).transpose()

        self.walls = []
        self.blocks = []
        self.players = []
        self.enemies = []
        self.bombs = []

        self.initialize_board()

    def initialize_window(self):

        self.setGeometry(0, 0, cfg.WINDOW_WIDTH, cfg.WINDOW_HEIGHT)

    def initialize_board(self):

        for i, x in enumerate(self.template, 0):
            for j, y in enumerate(x, 0):
                x_pos = i * cfg.SPRITE_SIZE
                y_pos = j * cfg.SPRITE_SIZE

                if y != cfg.TEMPLATE_WALL:
                    Block(self, x_pos, y_pos, cfg.GRASS)

                if y == cfg.TEMPLATE_WALL:
                    self.walls.append(Block(self, x_pos, y_pos, cfg.WALL))

                elif y == cfg.TEMPLATE_BLOCK:
                    self.blocks.append(Block(self, x_pos, y_pos, cfg.BRICK))

                elif y == cfg.TEMPLATE_EMPTY:
                    if random() < cfg.BRICK_SPAWN_CHANCE:
                        self.blocks.append(Block(self, x_pos, y_pos, cfg.BRICK))
                        self.template[i, j] = cfg.TEMPLATE_BLOCK

                elif y == cfg.TEMPLATE_PLAYER:
                        self.players.append(Player(self, x_pos, y_pos, len(self.players)))

        for player_id, player in enumerate(self.players, 0):
            self.players[player_id].raise_()

        while len(self.enemies) != cfg.ENEMY_COUNT:
            for i, x in enumerate(self.template, 0):
                for j, y in enumerate(x, 0):
                    x_pos = i * cfg.SPRITE_SIZE
                    y_pos = j * cfg.SPRITE_SIZE

                    if y == cfg.TEMPLATE_EMPTY:
                        if len(self.enemies) != cfg.ENEMY_COUNT:
                            if random() < cfg.ENEMY_SPAWN_CHANCE:
                                self.enemies.append(Enemy(self, x_pos, y_pos))

        for enemy_id, enemy in enumerate(self.enemies, 0):
            self.enemies[enemy_id].raise_()

