from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("my awesome app")

        label = QLabel('this is awesome')

        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon("acorn.png"), "your button", self)
        button_action.setStatusTip('this is your button')
        button_action.triggered.connect(self.on_mytoolbar_button_click)
        button_action.setCheckable(True)
        button_action.setShortcut(QKeySequence("Ctrl+p"))
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon('animal.png'), 'your button2', self)
        button_action2.setStatusTip(('this is your button2'))
        button_action2.triggered.connect(self.on_mytoolbar_button2_click)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel('Hello'))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)
        file_menu.addSeparator()

        file_submenu = file_menu.addMenu("Submenu")
        file_submenu.addAction(button_action2)

    def on_mytoolbar_button_click(self, s):
        print('on_mytoolbar_button_click : ', s)

    def on_mytoolbar_button2_click(self, s):
        print('on_mytoolbar_button2_click : ', s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()

