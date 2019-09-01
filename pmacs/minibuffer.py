from PyQt4 import QtGui, QtCore
from buffer import Buffer
from cursor import Cursor

class MiniBuffer(QtGui.QLineEdit):
    def __init__(self, parent, filepath, text, std_modes, primary_mode=None):
        super(MiniBuffer, self).__init__(parent)
        self.parent = parent

        # initialize class variables
        self.filepath = filepath
        self.actions = {}
        self.move_op_dict = {}
        self.std_modes = std_modes
        self.primary_mode = primary_mode
        self.mark_mode = False

        # child objects
        self.vlayout = QtGui.QVBoxLayout() # layout holds minibuffer and infobuffer
        self.infobuffer = Buffer(self)

        # insert starting text
        self.textCursor().insertText(text)

        # initializers
        self.init_move_op_dict()
        self.init_infobuffer()
        self.init_layout()

        # unset mark mode if text changes
        self.textChanged.connect(self.onTextChanged)
        
    def init_infobuffer(self):
        self.infobuffer.id = 0
        self.infobuffer.name = "infobuffer"

    def init_move_op_dict(self):
        self.move_op_dict[QtGui.QTextCursor.Start] = self.home
        self.move_op_dict[QtGui.QTextCursor.StartOfLine] = self.home
        self.move_op_dict[QtGui.QTextCursor.StartOfWord] = self.cursorWordBackward
        self.move_op_dict[QtGui.QTextCursor.PreviousCharacter] = self.cursorBackward
        self.move_op_dict[QtGui.QTextCursor.PreviousWord] = self.cursorWordBackward
        self.move_op_dict[QtGui.QTextCursor.Left] = self.cursorBackward
        self.move_op_dict[QtGui.QTextCursor.Right] = self.cursorForward
        self.move_op_dict[QtGui.QTextCursor.WordLeft] = self.cursorWordBackward
        self.move_op_dict[QtGui.QTextCursor.End] = self.end
        self.move_op_dict[QtGui.QTextCursor.EndOfLine] = self.end
        self.move_op_dict[QtGui.QTextCursor.EndOfWord] = self.cursorWordForward
        self.move_op_dict[QtGui.QTextCursor.NextCharacter] = self.cursorForward
        self.move_op_dict[QtGui.QTextCursor.NextWord] = self.cursorWordForward
        self.move_op_dict[QtGui.QTextCursor.WordRight] = self.cursorWordForward


    def init_layout(self):
        self.vlayout.addWidget(self.infobuffer)
        self.infobuffer.hide()
        self.vlayout.addWidget(self)

    # Compatibility methods
    def textCursor(self):
        return self

    def insertText(self, text):
        self.insert(text)

    def setPosition(self, pos):
        self.setCursorPosition(pos)

    def position(self):
        return self.cursorPosition()

    def setTextCursor(self, cursor):
        pass

    def moveCursor(self, MoveOperation, MoveMode=QtGui.QTextCursor.MoveAnchor):
        mark = (MoveMode == QtGui.QTextCursor.KeepAnchor)
        self.move_op_dict[MoveOperation](mark)

    @QtCore.pyqtSlot()
    def onTextChanged(self):
        self.unset_mark_mode()

    def unset_mark_mode(self):
        self.mark_mode = False
        self.deselect()

    def backspace(self):
        super(MiniBuffer, self).backspace()

    def enter(self):
        pass
