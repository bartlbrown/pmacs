
from stack import Stack
from buffer import Buffer
from minibuffer import MiniBuffer

import copy

from PyQt4 import (QtGui, QtCore)

import os
import sys
import importlib
import inspect

# Style Functions

def init_layout(self):
    self.setLayout(self.vlayout)
    self.vlayout.addLayout(self.current_stack.vlayout)
    self.vlayout.addLayout(self.minibuffer.vlayout)

def load_theme(self):
    with open(self.settings['stylesheet_path'], 'r') as f:
        text = f.read()
    self.setStyleSheet(text)


# Key Binding Functions

def add_keystr_to_widget(self, widget, keystr, scope):
    self.remove_keystr_from_widget(widget, keystr)
    action = self.create_action(keystr, scope)
    widget.actions[keystr] = action
    widget.addAction(action)

def remove_keystr_from_widget(self, widget, keystr):
    if widget.actions.get(keystr, False):
        widget.removeAction(widget.actions[keystr])
        del widget.actions[keystr]
    
def create_action(self, keystr, scope):
    action = QtGui.QAction(self)
    action.setShortcut(keystr)
    action.setShortcutContext(scope)
    action.triggered.connect(self.keystr_closure(keystr))
    return action

def bind(self, keystr, mode, function, scope=QtCore.Qt.WidgetShortcut):
    keystr = keystr.replace(" ", "")  # strip all white space

    # Make sure widgets with the specified mode have the keystr shortcut
    for widget in self.widgets:
        if mode in widget.std_modes or mode == widget.primary_mode:
            if not widget.actions.get(keystr, False):
                self.add_keystr_to_widget(widget, keystr, scope)

    # Add shortcut to dictionary
    if not self.shortcut_dict.get(mode, False):
        self.shortcut_dict[mode] = {keystr: function}
    else:
        self.shortcut_dict[mode][keystr] = function


def keystr_run(self, keystr):
    modes = copy.copy(self.current_widget.std_modes)
    modes.append(self.current_widget.primary_mode)
    modes.reverse()
    for mode in modes:
        if mode:
            if self.shortcut_dict.get(mode, False) and self.shortcut_dict[mode].get(keystr, False):
                print mode + " " + keystr
                self.shortcut_dict[mode][keystr]()
                self.last_cmd = self.shortcut_dict[mode][keystr]

        
def keystr_closure(self, keystr):
    def keystr_function():
        if self.macro_flag:
            self.macro.append(keystr) 
        self.keystr_run(keystr)
    return keystr_function


# Widget Functions

# Applies shortcuts to widget based on its std_modes list
def apply_std_modes(self, widget):
    for mode in widget.std_modes:
        if self.shortcut_dict.get(mode, False):
            for keystr in self.shortcut_dict[mode].keys():
                self.add_keystr_to_widget(widget, keystr, QtCore.Qt.WidgetShortcut)

# Applies shortcuts to widget based on its self.primary_mode
def apply_primary_mode(self, widget):
    if widget.primary_mode:
        if self.shortcut_dict.get(widget.primary_mode, False):
            for keystr in self.shortcut_dict[widget.primary_mode].keys():
                self.add_keystr_to_widget(widget, keystr, QtCore.Qt.WidgetShortcut)

# Sets the primary mode of a widget and then calls 
def set_primary_mode(self, widget, primary_mode):
    widget.primary_mode = primary_mode
    self.apply_primary_mode(widget)
    self.primary_mode_dict[primary_mode](self)

    
# Buffer Functions

def create_scratch(self):
    self.new_buffer('Scratch', None, self.settings['scratch_message'], self.settings['std_buffer_modes'])

def create_debug(self):
    self.new_buffer('Debug', None, self.settings['debug_message'], self.settings['std_buffer_modes'])

def get_buffer_with_id(self, id):
    for buffer in self.current_stack.children():
        if type(buffer) == Buffer:
            if buffer.id == id:
                return buffer
    return None
    
def get_buffer_with_name(self, name):
    for i in range(self.current_stack.count()):
        if self.current_stack.widget(i).name == name:
            return self.current_stack.widget(i)
    return None
    
# Creates a new buffer in each stack and applies the relevant shortcuts to each one.
# Every buffer copy has the same id
def new_buffer(self, name, filepath, text, std_modes, primary_mode=None):
    for stack in self.stacks:
        newBuf = Buffer(stack, self.next_buffer_id, name, filepath, text, std_modes, primary_mode)
        newBuf.installEventFilter(self)
        self.apply_std_modes(newBuf)
        self.apply_primary_mode(newBuf)
        stack.addWidget(newBuf)
        self.widgets.append(newBuf)
        newBuf.setCursorWidth(0)


    self.next_buffer_id = self.next_buffer_id + 1
    return int(self.next_buffer_id-1)    
    
# Stack Functions
    
def init_stacks(self):
    newStack = Stack(self)
    self.stacks.append(newStack)
    self.current_stack = newStack
    self.create_scratch()
    self.create_debug()
    self.current_widget = self.current_stack.currentWidget()

def copy_stack(self, stack):
    newStack = Stack(self)
    for i in range(stack.count()):
        bufCopy = stack.widget(i).copy()
        bufCopy.installEventFilter(self)
        self.apply_std_modes(bufCopy)
        self.apply_primary_mode(bufCopy)
        newStack.addWidget(bufCopy)
        self.widgets.append(bufCopy)
    self.stacks.append(newStack)
    return newStack

# Minibuffer Functions            

def init_minibuffer(self):
    self.minibuffer = self.new_minibuffer("", "~/", self.settings['std_minibuffer_modes'])
    self.widgets.append(self.minibuffer)
    
def new_minibuffer(self, filepath, text, std_modes, primary_mode=""):
    minibuffer = MiniBuffer(self, filepath, text, std_modes, primary_mode)
    minibuffer.installEventFilter(self)
    self.apply_std_modes(minibuffer)
    minibuffer.hide()
    return minibuffer

def focus_minibuffer(self):
    self.minibuffer.show()
    self.minibuffer.setFocus()

def unfocus_minibuffer(self):
    self.minibuffer.hide()
    self.minibuffer.infobuffer.hide()
    self.current_stack.currentWidget().setFocus()
    
def open_file(self, filename):
    try:
        filepath = os.path.abspath(filename)
        self.current_widget.filepath = filepath
        with open(filepath, 'r') as f:
            text = f.read()
        return text
    except:
        self.log_message(filename + " does not exist, creating new buffer.")
        return ""

    
# Error Logging

def log_message(self, message):
    debug = self.get_buffer_with_name("Debug")
    if debug:
        debug.moveCursor(QtGui.QTextCursor.End) # move cursor to end of buffer
        debug.insertPlainText(message + "\n")
    else:
        self.create_debug()
        self.log_message(message)
