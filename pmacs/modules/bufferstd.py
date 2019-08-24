from PyQt4 import (QtGui, QtCore)

# Search Functions
def select_all(self):
    text = self.current_stack.currentWidget().toPlainText()
    extraselections = []
    for i in range(text.count('test')):
        print i
        self.current_stack.currentWidget().find('test')
        selection = QtGui.QTextEdit.ExtraSelection()

        lineColor = QtGui.QColor(QtCore.Qt.red).lighter(160)

        selection.format.setBackground(lineColor)
        #selection.setStyleSheet('background-color: rgb(59, 59, 59);')
        #selection.format.setProperty(QtGui.QTextFormat.FullWidthSelection, QtCore.QVariant(True))
        
        selection.cursor = self.current_stack.currentWidget().textCursor()

        cursor = self.current_stack.currentWidget().textCursor()
        cursor.clearSelection()
        self.current_stack.currentWidget().setTextCursor(cursor)
        
        extraselections.append(selection)
        
    self.current_stack.currentWidget().setExtraSelections(extraselections)

# Focus
def focus_next_stack(self):
    index = self.stacks.index(self.current_stack)
    index = index + 1
    self.stacks[index % len(self.stacks)].currentWidget().setFocus()
    
# Stack Creation
def new_hstack(self):
    newStack = self.copy_stack(self.current_stack)
    self.current_stack.hlayout.addLayout(newStack.vlayout)
    newStack.currentWidget().setFocus()

def new_vstack(self):
    newStack = self.copy_stack(self.current_stack)
    self.current_stack.vlayout.addLayout(newStack.vlayout)
    newStack.currentWidget().setFocus()

# Stack Navigation
def next_buffer(self):
    activeBufferIndex = self.current_stack.currentIndex()
    activeBufferIndex = activeBufferIndex + 1
    if activeBufferIndex == self.current_stack.count():
        activeBufferIndex = 0
    self.current_stack.setCurrentIndex(activeBufferIndex)
    self.current_widget = self.current_stack.currentWidget()

def previous_buffer(self):
    activeBufferIndex = self.current_stack.currentIndex()
    activeBufferIndex = activeBufferIndex - 1
    if activeBufferIndex < 0:
        activeBufferIndex = self.current_stack.count() - 1
    self.current_stack.setCurrentIndex(activeBufferIndex)
    self.current_widget = self.current_stack.currentWidget()
