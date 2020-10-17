from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5 import QtCore
from overlay import Window

class Fullscreen:
    def __init__(self):
        self.app = QApplication([])
        self.label = QLabel()
        # self.label.setAttribute(Qt.WA_TranslucentBackground, True)
        self.label.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.label.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label.setStyleSheet("background:transparent;")
        self.label.showFullScreen()
        self.app.exec_()


    # def keyPressEvent(self, event):
    #     if event.key() == QtCore.Qt.Key_Escape:
    #         print("esc pressed")
    #         self.label.close()

