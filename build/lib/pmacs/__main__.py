import sys

from PyQt4 import (QtGui, QtCore)
from frame import Frame

class Window(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # Create and set Frame as central widget
        self.frame = Frame(self)
        self.setCentralWidget(self.frame)
        
        # Close main window when frame closes
        self.frame.closed.connect(self.exit)

        # x and y coordinates on the screen, width, height
        self.setGeometry(*self.frame.settings['window_geometry'])
        
        # Window title
        self.setWindowTitle(self.frame.settings['window_title'])

    def exit(self):
        self.close()



if __name__== "__main__":
    app = QtGui.QApplication(sys.argv)
    app.setCursorFlashTime(0)
    main = Window()

    main.show()
    sys.exit(app.exec_())
