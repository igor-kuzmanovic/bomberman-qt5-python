from itertools import chain
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget
from config import *


class Game(QWidget):

    def __init__(self, parent, board, key_notifier):

        super().__init__(parent)

        self.board = board

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_game)

        self.key_notifier = key_notifier
        self.key_notifier.key_signal.connect(self.notify_players)

    def start(self):

        self.timer.start(GAME_CYCLE_SLEEP)
        self.key_notifier.start()

    def stop(self):

        self.timer.stop()

    def notify_players(self, key):

        for player in self.board.players:
            if key in player.get_keys_from_id():
                if player.is_alive:
                    player.try_move(key)

    def update_game(self):

        for player in self.board.players:
            if player.is_alive is True:
                for block in chain(self.board.walls, self.board.bricks):
                    if player.check_potential_collision(block):
                        player.revert_position()
                        break

            else:
                player.decrement_respawn_time()
                player.respawn()

            player.update_position()

        for enemy in self.board.enemies:
            enemy.try_move_in_direction()

            for block in chain(self.board.walls, self.board.bricks):
                if enemy.check_potential_collision(block):
                    enemy.revert_position()
                    enemy.change_direction()
                    break

            for player in self.board.players:
                if player.is_alive is True:
                    if enemy.check_potential_collision(player) is True:
                        player.kill()

            enemy.update_position()
