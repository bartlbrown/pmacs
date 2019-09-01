from PyQt4 import QtGui, QtCore
from frame import Frame

class Cursor:
    def __init__(self, parent):
        self.parent = parent
        
        self.cursor = QtGui.QTextEdit.ExtraSelection()
        self.cursor.cursor = self.parent.textCursor()
        self.highlighter = QtGui.QTextEdit.ExtraSelection()
        self.highlighter.cursor = self.parent.textCursor()
        
        cursorColor = QtGui.QColor(QtCore.Qt.red).lighter(160)
        highlightColor = QtGui.QColor(QtCore.Qt.blue).lighter(160)
        
        self.cursor.format.setBackground(cursorColor)
        self.highlighter.format.setBackground(highlightColor)

        self.indicate_cursor()
        
    def set_textCursor_at_highlighter(self):
        self.parent.setTextCursor(self.highlighter.cursor)

    def set_textCursor_at_cursor(self):
        self.parent.setTextCursor(self.cursor.cursor)
        
    def insert(self, char):
        self.set_textCursor_at_highlighter()
        self.parent.insertPlainText(char)
        self.cursor.cursor = self.parent.textCursor()
        self.cursor.cursor.clearSelection()
        self.highlighter.cursor = self.parent.textCursor()
        self.indicate_cursor()

    def clear(self):
        self.highlighter.cursor.clearSelection()
        self.indicate_cursor()

    def indicate_cursor(self):
        self.clear_textCursor()
        # move forward one character and then select backwards
        self.cursor.cursor.movePosition(QtGui.QTextCursor.Right)
        self.cursor.cursor.movePosition(QtGui.QTextCursor.Left, QtGui.QTextCursor.KeepAnchor)
        self.set_textCursor_at_highlighter()
        self.set_extraSelections()
        

    def set_extraSelections(self):
        self.parent.setExtraSelections([self.highlighter, self.cursor])

    def moveCursor(self, MoveOperation, MoveMode=QtGui.QTextCursor.MoveAnchor):
        self.cursor.cursor.clearSelection()
        self.cursor.cursor.movePosition(MoveOperation)
        if self.cursor.cursor.atEnd():
            self.cursor.cursor.movePosition(QtGui.QTextCursor.Left)
        self.highlighter.cursor.setPosition(self.cursor.cursor.position(), MoveMode)
        self.indicate_cursor()

    def clear_textCursor(self):
        cursor = self.parent.textCursor()
        cursor.clearSelection()
        self.parent.setTextCursor(cursor)

    def backspace(self):
        self.highlighter.cursor.deletePreviousChar()
        self.parent.setTextCursor(self.highlighter.cursor)

    def enter(self):
        self.highlighter.cursor.insertText('\n')
        self.parent.setTextCursor(self.highlighter.cursor)
