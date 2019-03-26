from time import sleep
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
import config as cfg


class KeyNotifier(QObject):

    key_signal = pyqtSignal(int)

    def __init__(self):

        super().__init__()

        self.keys = []
        self.is_done = False

        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.__work__)

    def start(self):

        self.thread.start()

    def add_key(self, key):

        self.keys.append(key)

    def rem_key(self, key):

        self.keys.remove(key)

    def die(self):

        self.is_done = True
        self.thread.quit()

    @pyqtSlot()
    def __work__(self):

        while not self.is_done:
            for key in self.keys:
                self.key_signal.emit(key)

            sleep(cfg.GAME_SPEED / 5000)
