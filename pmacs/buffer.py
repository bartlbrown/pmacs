from PyQt4 import QtGui, QtCore

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
        self.move_op_dict = {}
        # stop markmode if the text changed
        self.textChanged.connect(self.onTextChanged)
        #self.cursorPositionChanged.connect(self.onCursorPositionChanged)
        self.init_move_op_dict()
        
        self.cursors = []
        self.new_cursor()
        
        self.textCursor().insertText(text+" ")
        self.moveCursor(QtGui.QTextCursor.Left)

    def new_cursor(self):
        cursor = QtGui.QTextEdit.ExtraSelection()
        cursorColor = QtGui.QColor(QtCore.Qt.red).lighter(160)
        cursor.format.setBackground(cursorColor)
        cursor.cursor = self.textCursor()
        cursor.cursor.clearSelection()
        self.cursors.append(cursor)
        self.setExtraSelections(self.cursors)
        
#    @QtCore.pyqtSlot()
#     def onCursorPositionChanged(self):
#         cursor_pos = self.textCursor().position()
#         text = self.toPlainText()
#         average_width = self.fontMetrics().averageCharWidth()
#         if cursor_pos < len(text):
#             current_char = self.toPlainText()[cursor_pos]
#             if str(current_char).isspace():
#                 self.setCursorWidth(average_width)
#             else:
#                 self.setCursorWidth(self.fontMetrics().charWidth(current_char, 0))
#         else:
#             self.setCursorWidth(average_width)
                
    
    @QtCore.pyqtSlot()
    def onTextChanged(self):
        self.unset_mark_mode()

    def copy(self):
        newBuffer = Buffer(self.parent, self.id, self.name, self.filepath, "", self.std_modes, self.primary_mode)
        newBuffer.setTextCursor(self.textCursor())
        newBuffer.setDocument(self.document())
        return newBuffer

    def unset_mark_mode(self):
        self.mark_mode = False
        cursor = self.textCursor()
        cursor.setPosition(cursor.position())
        self.setTextCursor(cursor)

    def init_move_op_dict(self):
        self.move_op_dict[QtGui.QTextCursor.NoMove] = self.cursorNoMove
        self.move_op_dict[QtGui.QTextCursor.Start] = self.cursorStart
        self.move_op_dict[QtGui.QTextCursor.StartOfLine] = self.cursorStartOfLine
        self.move_op_dict[QtGui.QTextCursor.StartOfBlock] = self.cursorStartOfBlock
        self.move_op_dict[QtGui.QTextCursor.StartOfWord] = self.cursorStartOfWord
        self.move_op_dict[QtGui.QTextCursor.PreviousBlock] = self.cursorPreviousBlock
        self.move_op_dict[QtGui.QTextCursor.PreviousCharacter] = self.cursorPreviousCharacter
        self.move_op_dict[QtGui.QTextCursor.PreviousWord] = self.cursorPreviousWord
        self.move_op_dict[QtGui.QTextCursor.Up] = self.cursorUp
        self.move_op_dict[QtGui.QTextCursor.Left] = self.cursorLeft
        self.move_op_dict[QtGui.QTextCursor.WordLeft] = self.cursorWordLeft
        self.move_op_dict[QtGui.QTextCursor.End] = self.cursorEnd
        self.move_op_dict[QtGui.QTextCursor.EndOfLine] = self.cursorEndOfLine
        self.move_op_dict[QtGui.QTextCursor.EndOfWord] = self.cursorEndOfWord
        self.move_op_dict[QtGui.QTextCursor.EndOfBlock] = self.cursorEndOfBlock
        self.move_op_dict[QtGui.QTextCursor.NextBlock] = self.cursorNextBlock
        self.move_op_dict[QtGui.QTextCursor.NextWord] = self.cursorNextWord
        self.move_op_dict[QtGui.QTextCursor.Down] = self.cursorDown
        self.move_op_dict[QtGui.QTextCursor.Right] = self.cursorRight
        self.move_op_dict[QtGui.QTextCursor.WordRight] = self.cursorWordRight
        self.move_op_dict[QtGui.QTextCursor.NextCell] = self.cursorNextCell
        self.move_op_dict[QtGui.QTextCursor.PreviousCell] = self.cursorPreviousCell
        self.move_op_dict[QtGui.QTextCursor.NextRow] = self.cursorNextRow
        self.move_op_dict[QtGui.QTextCursor.PreviousRow] = self.cursorPreviousRow

    def moveCursor(self, MoveOperation, MoveMode=QtGui.QTextCursor.MoveAnchor, cursor=None):
        if self.mark_mode:
                    MoveMode = QtGui.QTextCursor.KeepAnchor 
        if cursor == None:
            for cursor in self.cursors:
                self.moveCursor(MoveOperation, MoveMode, cursor)
            else:
                cursor.cursor.clearSelection()
                self.setTextCursor(cursor.cursor)
                super(Buffer, self).moveCursor(QtGui.QTextCursor.Left)
                self.move_op_dict[MoveOperation](MoveMode)

                super(Buffer, self).moveCursor(QtGui.QTextCursor.Right, QtGui.QTextCursor.KeepAnchor)
                cursor.cursor = self.textCursor()

                newcursor = self.textCursor()
                newcursor.clearSelection()
                self.setTextCursor(newcursor)
                
                self.setExtraSelections(self.cursors)
                
    def cursorNoMove(self, MoveMode):
        super(Buffer, self).moveCursor(QtGui.QTextCursor.NoMove, MoveMode)
        
    def cursorStart(self, MoveMode):
        super(Buffer, self).moveCursor(QtGui.QTextCursor.Start, MoveMode)
    
    def cursorStartOfLine(self, MoveMode):
        super(Buffer, self).moveCursor(QtGui.QTextCursor.StartOfLine, MoveMode)
    
    def cursorStartOfBlock(self, MoveMode):
        super(Buffer, self).moveCursor(QtGui.QTextCursor.StartOfBlock, MoveMode)
    
    def cursorStartOfWord(self, MoveMode):
        super(Buffer, self).moveCursor(QtGui.QTextCursor.StartOfWord, MoveMode)
    
    def cursorPreviousBlock(self, MoveMode):
        super(Buffer, self).moveCursor(QtGui.QTextCursor.PreviousBlock, MoveMode)
    
    def cursorPreviousCharacter(self, MoveMode):
        super(Buffer, self).moveCursor(QtGui.QTextCursor.PreviousCharacter, MoveMode)
    
    def cursorPreviousWord(self, MoveMode):
        super(Buffer, self).moveCursor(QtGui.QTextCursor.PreviousWord, MoveMode)
    
    def cursorUp(self, MoveMode):
        super(Buffer, self).moveCursor(QtGui.QTextCursor.Up, MoveMode)
    
    def cursorLeft(self, MoveMode):
        super(Buffer, self).moveCursor(QtGui.QTextCursor.Left, MoveMode)
    
    def cursorWordLeft(self, MoveMode):
        super(Buffer, self).moveCursor(QtGui.QTextCursor.WordLeft, MoveMode)
    
    def cursorEnd(self, MoveMode):
        super(Buffer, self).moveCursor(QtGui.QTextCursor.End, MoveMode)
        self.moveCursor(QtGui.QTextCursor.Left)
        
    def cursorEndOfLine(self, MoveMode):
        super(Buffer, self).moveCursor(QtGui.QTextCursor.EndOfLine, MoveMode)
        if self.textCursor().position() == len(self.toPlainText()):
            self.moveCursor(QtGui.QTextCursor.Left)
            
    def cursorEndOfWord(self, MoveMode):
        super(Buffer, self).moveCursor(QtGui.QTextCursor.EndOfWord, MoveMode)
        if self.textCursor().position() == len(self.toPlainText()):
            self.moveCursor(QtGui.QTextCursor.Left)
            
    def cursorEndOfBlock(self, MoveMode):
        super(Buffer, self).moveCursor(QtGui.QTextCursor.EndOfBlock, MoveMode)
        if self.textCursor().position() == len(self.toPlainText()):
            self.moveCursor(QtGui.QTextCursor.Left)
            
    def cursorNextBlock(self, MoveMode):
        super(Buffer, self).moveCursor(QtGui.QTextCursor.NextBlock, MoveMode)
    
    def cursorNextWord(self, MoveMode):
        super(Buffer, self).moveCursor(QtGui.QTextCursor.NextWord, MoveMode)
        if self.textCursor().position() == len(self.toPlainText()):
            self.moveCursor(QtGui.QTextCursor.Left)
    
    def cursorDown(self, MoveMode):
        super(Buffer, self).moveCursor(QtGui.QTextCursor.Down, MoveMode)
        if self.textCursor().position() == len(self.toPlainText()):
            self.moveCursor(QtGui.QTextCursor.Left)
    
    def cursorRight(self, MoveMode):
        super(Buffer, self).moveCursor(QtGui.QTextCursor.Right, MoveMode)
        if self.textCursor().position() == len(self.toPlainText()):
            self.moveCursor(QtGui.QTextCursor.Left)
    
    def cursorWordRight(self, MoveMode):
        super(Buffer, self).moveCursor(QtGui.QTextCursor.WordRight, MoveMode)
        if self.textCursor().position() == len(self.toPlainText()):
            self.moveCursor(QtGui.QTextCursor.Left)
    
    def cursorNextCell(self, MoveMode):
        super(Buffer, self).moveCursor(QtGui.QTextCursor.NextCell, MoveMode)
    
    def cursorPreviousCell(self, MoveMode):
        super(Buffer, self).moveCursor(QtGui.QTextCursor.PreviousCell, MoveMode)
    
    def cursorNextRow(self, MoveMode):
        super(Buffer, self).moveCursor(QtGui.QTextCursor.NextRow, MoveMode)
    
    def cursorPreviousRow(self, MoveMode):
        super(Buffer, self).moveCursor(QtGui.QTextCursor.PreviousRow, MoveMode)
        
