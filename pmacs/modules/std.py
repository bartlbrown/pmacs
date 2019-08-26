from PyQt4 import (QtGui, QtCore)

def exit(self):
    self.closed.emit()
    self.close()
    
# Mark Mode
def toggle_mark_mode(self):
    self.current_widget.mark_mode = not self.current_widget.mark_mode
    if not self.current_widget.mark_mode:
        self.current_widget.unset_mark_mode()

# Cursor Movement
def move_cursor_char_right(self):
    if self.current_widget.mark_mode:
        self.current_widget.moveCursor(QtGui.QTextCursor.Right, QtGui.QTextCursor.KeepAnchor)
    else:
        self.current_widget.moveCursor(QtGui.QTextCursor.Right)

def move_cursor_char_left(self):
    if self.current_widget.mark_mode:
        self.current_widget.moveCursor(QtGui.QTextCursor.Left, QtGui.QTextCursor.KeepAnchor)
    else:
        self.current_widget.moveCursor(QtGui.QTextCursor.Left)

def move_cursor_line_up(self):
    if self.current_widget.mark_mode:
        self.current_widget.moveCursor(QtGui.QTextCursor.Up, QtGui.QTextCursor.KeepAnchor)
    else:
        self.current_widget.moveCursor(QtGui.QTextCursor.Up)

def move_cursor_line_down(self):
    if self.current_widget.mark_mode:
        self.current_widget.moveCursor(QtGui.QTextCursor.Down, QtGui.QTextCursor.KeepAnchor)
    else:
        self.current_widget.moveCursor(QtGui.QTextCursor.Down)

def move_cursor_word_right(self):
    if self.current_widget.mark_mode:
        self.current_widget.moveCursor(QtGui.QTextCursor.WordRight, QtGui.QTextCursor.KeepAnchor)
    else:
        self.current_widget.moveCursor(QtGui.QTextCursor.WordRight)

def move_cursor_word_left(self):
    if self.current_widget.mark_mode:
        self.current_widget.moveCursor(QtGui.QTextCursor.WordLeft, QtGui.QTextCursor.KeepAnchor)
    else:
        self.current_widget.moveCursor(QtGui.QTextCursor.WordLeft)

def move_cursor_block_up(self):
    if self.current_widget.mark_mode:
        self.current_widget.moveCursor(QtGui.QTextCursor.PreviousBlock, QtGui.QTextCursor.KeepAnchor)
        self.current_widget.moveCursor(QtGui.QTextCursor.StartOfBlock, QtGui.QTextCursor.KeepAnchor)
    else:
        self.current_widget.moveCursor(QtGui.QTextCursor.PreviousBlock)
        self.current_widget.moveCursor(QtGui.QTextCursor.StartOfBlock)
        
def move_cursor_block_down(self):
    if self.current_widget.mark_mode:
        self.current_widget.moveCursor(QtGui.QTextCursor.NextBlock, QtGui.QTextCursor.KeepAnchor)
        self.current_widget.moveCursor(QtGui.QTextCursor.EndOfBlock, QtGui.QTextCursor.KeepAnchor)
    else:
        self.current_widget.moveCursor(QtGui.QTextCursor.NextBlock)
        self.current_widget.moveCursor(QtGui.QTextCursor.EndOfBlock)

# Mark mode
def move_cursor_char_right_mark(self):
    self.current_widget.moveCursor(QtGui.QTextCursor.Right, QtGui.QTextCursor.KeepAnchor)

def move_cursor_char_left_mark(self):
    self.current_widget.moveCursor(QtGui.QTextCursor.Left, QtGui.QTextCursor.KeepAnchor)

def move_cursor_line_up_mark(self):
    self.current_widget.moveCursor(QtGui.QTextCursor.Up, QtGui.QTextCursor.KeepAnchor)

def move_cursor_line_down_mark(self):
    self.current_widget.moveCursor(QtGui.QTextCursor.Down, QtGui.QTextCursor.KeepAnchor)

def move_cursor_word_right_mark(self):
    self.current_widget.moveCursor(QtGui.QTextCursor.WordRight, QtGui.QTextCursor.KeepAnchor)

def move_cursor_word_left_mark(self):
    self.current_widget.moveCursor(QtGui.QTextCursor.WordLeft, QtGui.QTextCursor.KeepAnchor)

def move_cursor_block_up_mark(self):
    self.current_widget.moveCursor(QtGui.QTextCursor.PreviousBlock, QtGui.QTextCursor.KeepAnchor)

def move_cursor_block_down_mark(self):
    self.current_widget.moveCursor(QtGui.QTextCursor.NextBlock, QtGui.QTextCursor.KeepAnchor)
    self.current_widget.moveCursor(QtGui.QTextCursor.EndOfBlock, QtGui.QTextCursor.KeepAnchor)
        
def move_cursor_line_end(self):
    if self.current_widget.mark_mode:
        self.current_widget.moveCursor(QtGui.QTextCursor.EndOfLine, QtGui.QTextCursor.KeepAnchor)
    else:
        self.current_widget.moveCursor(QtGui.QTextCursor.EndOfLine)
  
def move_cursor_line_start(self):
    if self.current_widget.mark_mode:
        self.current_widget.moveCursor(QtGui.QTextCursor.StartOfLine, QtGui.QTextCursor.KeepAnchor)
    else:
        self.current_widget.moveCursor(QtGui.QTextCursor.StartOfLine)

def move_cursor_line_end_mark(self):
    self.current_widget.moveCursor(QtGui.QTextCursor.EndOfLine, QtGui.QTextCursor.KeepAnchor)

def move_cursor_line_start_mark(self):
    self.current_widget.moveCursor(QtGui.QTextCursor.StartOfLine, QtGui.QTextCursor.KeepAnchor)
