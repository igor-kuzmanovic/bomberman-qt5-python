from numpy import zeros, array
from random import random, randint
from sys import argv, exit
from time import sleep
from threading import Timer
from math import floor
from PyQt5.QtCore import Qt, QThread, QTimer, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QDesktopWidget
from PyQt5.QtGui import QPixmap, QColor, QMovie
import config as cfg
from board import Board


class Game(QWidget):

    def __init__(self, parent, board):

        super().__init__(parent)

        self.board = board

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_game)

    def start(self):

        self.timer.start(1000 / cfg.GAME_SPEED)

    def stop(self):

        self.timer.stop()

    def update_game(self):

        for player_id, player in enumerate(self.board.players, 0):
            if player.is_alive is True:
                for enemy_id, enemy in enumerate(self.board.enemies, 0):
                    if enemy.is_alive is True:
                        if player.check_temp_collision(enemy) is True:
                            self.board.players[player_id].change_direction()

                random_move = player.direction

                if random_move == 0:
                    self.board.players[player_id].try_move_up()

                elif random_move == 1:
                    self.board.players[player_id].try_move_down()

                elif random_move == 2:
                    self.board.players[player_id].try_move_left()

                elif random_move == 3:
                    self.board.players[player_id].try_move_right()

                for wall in self.board.walls:
                    if player.check_temp_collision(wall):
                        self.board.players[player_id].revert_position()
                        self.board.players[player_id].change_direction()
                        break
                else:
                    for block in self.board.blocks:
                        if player.check_temp_collision(block):
                            self.board.players[player_id].revert_position()
                            self.board.players[player_id].change_direction()
                            break

                self.board.players[player_id].update_position()
            else:
                self.board.players[player_id].respawn_timer -= 1
                self.board.players[player_id].respawn()

        for enemy_id, enemy in enumerate(self.board.enemies, 0):
            if enemy.is_alive is True:
                random_move = enemy.direction

                if random_move == 0:
                    self.board.enemies[enemy_id].try_move_up()

                elif random_move == 1:
                    self.board.enemies[enemy_id].try_move_down()

                elif random_move == 2:
                    self.board.enemies[enemy_id].try_move_left()

                elif random_move == 3:
                    self.board.enemies[enemy_id].try_move_right()

                for wall in self.board.walls:
                    if enemy.check_temp_collision(wall):
                        self.board.enemies[enemy_id].revert_position()
                        self.board.enemies[enemy_id].change_direction()
                        break
                else:
                    for block in self.board.blocks:
                        if enemy.check_temp_collision(block):
                            self.board.enemies[enemy_id].revert_position()
                            self.board.enemies[enemy_id].change_direction()
                            break

                self.board.enemies[enemy_id].update_position()

                for player_id, player in enumerate(self.board.players, 0):
                    if player.is_alive is True:
                        if enemy.check_collision(player) is True:
                            self.board.players[player_id].kill()

            else:
                self.board.enemies[enemy_id].respawn_timer -= 1
                self.board.enemies[enemy_id].respawn()
