from PyQt4 import (QtGui, QtCore)
from buffer import Buffer


class Stack(QtGui.QStackedWidget):
    def __init__(self, parent=None):
        super(Stack, self).__init__(parent)
        self.parent = parent

        # create layout containers
        self.hlayout = QtGui.QHBoxLayout()
        self.vlayout = QtGui.QVBoxLayout()

        # Add self to layout
        self.initLayout()

    def initLayout(self):
        self.hlayout.addWidget(self)
        self.vlayout.addLayout(self.hlayout)
