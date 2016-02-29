#!/usr/bin/env python

from PyQt5.QtWidgets import (QApplication, QWidget,
                             QGridLayout, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton)
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import sip
import cmdFWMain as cmdFW
from collections import namedtuple

class options(object):
    def __init__(self, input):
          self.input = input

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.inputLine = QLineEdit()
        self.outputLine = QLineEdit()
        self.outputLine.setReadOnly(True)

        self.calcButton = QPushButton("&Exec")
        self.calcButton.clicked.connect(self.start)

        lineLayout = QGridLayout()
        lineLayout.addWidget(QLabel("input"), 0, 0)
        lineLayout.addWidget(self.inputLine, 0, 1)

        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(self.calcButton)

        mainLayout = QHBoxLayout()
        mainLayout.addLayout(lineLayout)
        mainLayout.addLayout(buttonLayout)

        self.setLayout(mainLayout)
        self.setWindowTitle("Factorial")

    def start(self):
        param = options(self.inputLine.text())
        args = {}
        cmdFW.CmdFWMain(param, args)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    main_window = MainWindow()

    main_window.show()
    sys.exit(app.exec_())
