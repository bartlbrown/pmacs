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

        self.cursor = Cursor(self)
        self.mark_mode = False
        self.setText(text)
        self.cursor.moveCursor(QtGui.QTextCursor.EndOfLine)
        # stop markmode if the text changed
        self.textChanged.connect(self.onTextChanged)
        self.setCursorWidth(0)


    def setText(self, text):
        text = text + " "
        super(Buffer, self).setText(text)

    def toPlainText(self):
        text = super(Buffer, self).toPlainText()
        return text[:-1]
        
    def insertPlainText(self, text):
        super(Buffer, self).insertPlainText(text)
        
    @QtCore.pyqtSlot()
    def onTextChanged(self):
        self.unset_mark_mode()

    def unset_mark_mode(self):
        self.mark_mode = False
        self.cursor.clear()
        
    def copy(self, parent):
        newBuffer = Buffer(parent, self.id, self.name, self.filepath, "", self.std_modes, self.primary_mode)
        newBuffer.setTextCursor(self.textCursor())
        newBuffer.cursor = self.cursor.copy(newBuffer)
        doc = self.document()
        newBuffer.setDocument(doc)
        return newBuffer

    def moveCursor(self, MoveOperation, MoveMode=QtGui.QTextCursor.MoveAnchor):
        self.cursor.moveCursor(MoveOperation, MoveMode)

    def insert(self, char):
        self.cursor.insert(char)
        
    def backspace(self):
        self.cursor.backspace()

    def enter(self):
        self.cursor.enter()
