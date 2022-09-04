from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys


class MainWindow(QMainWindow):
    def __init__(self, *argv, **kwargs):
        super().__init__(*argv, **kwargs)

        self.windowTitleChanged.connect(self.on_window_title_changed)

        self.windowTitleChanged.connect(lambda x: self.my_custom_fn())
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x))
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x, 25))

        self.setWindowTitle('My Awesome App')

        # label = QLabel("this is awesome!")
        # label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #
        # self.setCentralWidget(label)

        edit = QLineEdit()
        self.setCentralWidget(edit)

    def on_window_title_changed(self, title):
        print('title changed to ', title)

    def my_custom_fn(self, a="HELLLO!", b=5):
        print(a, b)

    def contextMenuEvent(self, event):
        print('context menu event!')
        super().contextMenuEvent(event)




app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()