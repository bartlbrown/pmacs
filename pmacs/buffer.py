from PyQt4 import QtGui, QtCore
from cursor import Cursor

class Buffer(QtGui.QTextEdit, QtCore.QObject):
    def __init__(self, parent, id=0, name="", filepath="", text="", std_modes=[], primary_mode=None):
        super(Buffer, self).__init__(parent)
        self.parent = parent

        # initialize class variables
        self.id = id
        self.name = name
        self.filepath = filepath
        self.actions = {}
        self.std_modes = std_modes
        self.primary_mode = primary_mode
        self.mark_mode = False
        self.insertPlainText(text)
        # stop markmode if the text changed
        self.textChanged.connect(self.onTextChanged)
        self.cursor = Cursor(self)
                                
    @QtCore.pyqtSlot()
    def onTextChanged(self):
        self.unset_mark_mode()

    def unset_mark_mode(self):
        self.mark_mode = False
        self.cursor.clear()

        
    def copy(self):
        newBuffer = Buffer(self.parent, self.id, self.name, self.filepath, "", self.std_modes, self.primary_mode)
        newBuffer.setTextCursor(self.textCursor())
        newBuffer.setDocument(self.document())
        return newBuffer

    def moveCursor(self, MoveOperation, MoveMode=QtGui.QTextCursor.MoveAnchor):
        self.cursor.moveCursor(MoveOperation, MoveMode)
