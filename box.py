import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from worker import Worker
from form import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.worker = Worker()
        self.worker.update.connect(self.updateTime)
        self.worker.finish.connect(self.finish)

    def onStart(self):
        jobs = []
        for i in range(10):
            jobs.append(i)
            self.worker.start()

    def updateTime(self, seconds):
        self.ui.lblSeconds.setText(str(seconds))

    def finish(self):
        self.ui.btnStart.setText('Finish')
        self.ui.btnStart.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = MainWindow()
    main.show()

    sys.exit(app.exec_())
