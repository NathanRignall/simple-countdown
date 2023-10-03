import sys

from PySide6.QtWidgets import *
from PySide6.QtGui import *

from ui_main import Ui_MainWindow
from thread_timer import thread_timer

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.ui.thread_timer = thread_timer()
        self.ui.thread_timer.finished.connect(self.close)
        
        self.ui.thread_timer.timerValue.connect(self.setClock)
        self.ui.thread_timer.timerText.connect(self.setText)

        self.ui.thread_timer.start()

    def setClock(self, value):
        if (value == '00:00:00'):
            self.ui.clock.setStyleSheet('color: red')
        else:
            self.ui.clock.setStyleSheet('color: ')

        self.ui.clock.setText(value)

    def setText(self, value):
        self.ui.text.setText(value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    # window.setStyleSheet("background-image : url(background.jpeg);")
    sys.exit(app.exec())
