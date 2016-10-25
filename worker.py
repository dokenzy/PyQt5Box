import time

from PyQt5.QtCore import QThread, pyqtSignal


class Worker(QThread):
    update = pyqtSignal(float)
    finish = pyqtSignal()

    def __del__(self):
        self.wait()

    def run(self):
        for i in range(10):
            time.sleep(1)
            self.update.emit(time.clock())
        self.finish.emit()
