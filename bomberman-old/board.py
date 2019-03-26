from random import randint
from numpy import array
from PyQt5.QtWidgets import QWidget
from config import *
from block import Block
from player import Player
from enemy import Enemy


class Board(QWidget):

    def __init__(self, parent):

        super().__init__(parent)

        self.initialize_window()

        self.template = array([['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                               ['W', 'P', 'R', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'R', 'R', 'W'],
                               ['W', 'R', 'W', 'B', 'W', 'B', 'W', '/', 'W', '/', 'W', 'B', 'W', 'B', 'W', 'R', 'W'],
                               ['W', 'B', 'B', 'B', 'B', 'B', '/', '/', 'B', '/', '/', 'B', 'B', 'B', 'B', 'B', 'W'],
                               ['W', 'B', 'W', 'B', 'W', '/', 'W', '/', 'W', '/', 'W', '/', 'W', 'B', 'W', 'B', 'W'],
                               ['W', 'B', 'B', 'B', '/', '/', '/', '/', 'E', '/', '/', '/', '/', 'B', 'B', 'B', 'W'],
                               ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'E', 'W', 'E', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                               ['W', 'B', 'B', 'B', '/', '/', '/', '/', 'E', '/', '/', '/', '/', 'B', 'B', 'B', 'W'],
                               ['W', 'B', 'W', 'B', 'W', '/', 'W', '/', 'W', '/', 'W', '/', 'W', 'B', 'W', 'B', 'W'],
                               ['W', 'B', 'B', 'B', 'B', 'B', '/', '/', 'B', '/', '/', 'B', 'B', 'B', 'B', 'B', 'W'],
                               ['W', 'R', 'W', 'B', 'W', 'B', 'W', '/', 'W', '/', 'W', 'B', 'W', 'B', 'W', 'R', 'W'],
                               ['W', 'R', 'R', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'R', 'P', 'W'],
                               ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]).transpose()

        self.walls = []
        self.bricks = []
        self.players = []
        self.enemies = []
        self.bombs = []

        self.initialize_board()

    def initialize_window(self):

        self.setGeometry(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)

    def initialize_board(self):

        for i, x in enumerate(self.template, 0):
            for j, y in enumerate(x, 0):
                x_pos = i * SPRITE_SIZE
                y_pos = j * SPRITE_SIZE

                if y != TEMPLATE_WALL:
                    Block(self, x_pos, y_pos, GRASS)

                if y == TEMPLATE_WALL:
                    self.walls.append(Block(self, x_pos, y_pos, WALL))

                elif y == TEMPLATE_BRICK:
                    if BRICK_SPAWN > 0:
                        self.bricks.append(Block(self, x_pos, y_pos, BRICK))

                elif y == TEMPLATE_EMPTY:
                    if randint(0, 99) >= BRICK_SPAWN:
                        self.bricks.append(Block(self, x_pos, y_pos, BRICK))

                elif y == TEMPLATE_ENEMY:
                    if ENEMY_SPAWN > 0:
                        self.enemies.append(Enemy(self, x_pos, y_pos))

                elif y == TEMPLATE_PLAYER:
                    self.players.append(Player(self, x_pos, y_pos, len(self.players)))

        for player in self.players:
            player.raise_()

        for enemy in self.enemies:
            enemy.raise_()

