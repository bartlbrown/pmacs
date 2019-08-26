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

    def insert(self, char):
        self.parent.setTextCursor(self.highlighter.cursor)
        self.parent.insertPlainText(char)
        self.cursor.cursor = self.parent.textCursor()
        self.cursor.cursor.clearSelection()
        self.highlighter.cursor = self.parent.textCursor()
        self.indicate_cursor()

    def clear(self):
        self.highlighter.cursor.clearSelection()
        self.indicate_cursor()

    def default_event_handler(self, sourceObj, event):
        self.parent.setTextCursor(self.highlighter.cursor)
        value = super(type(self.parent), self.parent).eventFilter(sourceObj, event)
        self.cursor.cursor = self.parent.textCursor()
        self.indicate_cursor()
        return value

    def copy_highlighter(self):
        highlighter = QtGui.QTextEdit.ExtraSelection()
        highlighter.cursor = self.parent.textCursor()
        highlighter.cursor.setPosition(self.highlighter.cursor.anchor())
        highlighter.cursor.setPosition(self.highlighter.cursor.position(), QtGui.QTextCursor.KeepAnchor)
        return highlighter

    def copy_cursor(self):
        cursor = QtGui.QTextEdit.ExtraSelection()
        cursor.cursor = self.parent.textCursor()
        cursor.cursor.setPosition(self.cursor.cursor.anchor())
        cursor.cursor.setPosition(self.cursor.cursor.position(), QtGui.QTextCursor.KeepAnchor)
        return cursor
    
    def indicate_cursor(self):
        self.clear_textCursor()
        # move forward one character and then select backwards
        self.cursor.cursor.movePosition(QtGui.QTextCursor.Right)
        self.cursor.cursor.movePosition(QtGui.QTextCursor.Left, QtGui.QTextCursor.KeepAnchor)
        self.set_extraSelections()

    def set_extraSelections(self):
        self.parent.setExtraSelections([self.highlighter, self.cursor])

    def moveCursor(self, MoveOperation, MoveMode=QtGui.QTextCursor.MoveAnchor):
        self.cursor.cursor.clearSelection()
        self.cursor.cursor.movePosition(MoveOperation)
        self.highlighter.cursor.setPosition(self.cursor.cursor.position(), MoveMode)
        self.indicate_cursor()

    def clear_textCursor(self):
        cursor = self.parent.textCursor()
        cursor.clearSelection()
        self.parent.setTextCursor(cursor)
