from PyQt4 import (QtGui, QtCore)
import glob
import os

def ON_LOAD(self):
    self.bind('Ctrl+X, Ctrl+F', 'bufferstd', self.minibuffer_open_file)
    self.bind('Ctrl+X, Ctrl+S', 'bufferstd', self.save_current_buffer_to_file)
    self.opening_file= False
    
def INIT(self):
    self.minibuffer.returnPressed.disconnect()
    self.minibuffer.returnPressed.connect(self.minibuffer_open_or_save_file)
    self.bind('Tab, Tab', 'minibufferfile', self.minibuffer_file_autocomplete)

def minibuffer_open_or_save_file(self):
    if self.opening_file:
        self.open_file_in_new_buffer()
        self.opening_file = False
    else:
         self.saveas_current_buffer_to_file()
    
def minibuffer_open_file(self):
    self.set_primary_mode(self.minibuffer, 'minibufferfile')
    self.opening_file = True
    self.focus_minibuffer()
    
def open_file_in_new_buffer(self):
    id = self.new_buffer("", self.minibuffer.text(), "", self.settings['std_buffer_modes'])
    self.current_stack.setCurrentWidget(self.get_buffer_with_id(id))
    self.unfocus_minibuffer()
    text = self.open_file(str(self.minibuffer.text()))
    self.current_widget.setPlainText(text)

def save_current_buffer_to_file(self):
    buffer = self.current_widget
    if issubclass(type(buffer), QtGui.QTextEdit):
        if buffer.filepath:
            f =  open(buffer.filepath,"w+")
            f.write(buffer.toPlainText())
            f.close()
        else:
            self.log_message("Buffer does not have a filepath set.")
            self.set_primary_mode(self.minibuffer, 'minibufferfile')
            self.focus_minibuffer()

def saveas_current_buffer_to_file(self):
    buffer = self.current_widget
    if issubclass(type(buffer), QtGui.QTextEdit):
        buffer.filepath = str(self.minibuffer.text())
        self.save_current_buffer_to_file()
            
def minibuffer_file_autocomplete(self):
    filepath = self.minibuffer.filepath
    text = self.minibuffer.text()
    text = os.path.expanduser(str(text))
    options = glob.glob(str(str(text)+'*'))
    if len(options) == 1:
        self.minibuffer.infobuffer.hide()
        text = options[0]
        if os.path.isdir(text):
            text = text + "/"
    elif len(options):
        text = os.path.commonprefix(options)
        options =  [os.path.basename(o) for o in options]
        ac = "\t".join(options)
        self.minibuffer.infobuffer.show()
        self.minibuffer.infobuffer.setText(ac)
        self.minibuffer.infobuffer.setFixedHeight(self.minibuffer.infobuffer.document().size().height())
    else:
        self.minibuffer.infobuffer.hide()
    self.minibuffer.setText(text)
