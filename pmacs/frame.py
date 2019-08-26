from PyQt4 import (QtGui, QtCore)

import os
import sys
import importlib
import inspect
import re


class Frame(QtGui.QWidget):
    closed = QtCore.pyqtSignal()                # signal to close window

    def __init__(self, parent=None):
        super(Frame, self).__init__(parent)   # call parent constructor
        self.parent = parent

        # load config paths
        if 'PMACSDIR' in os.environ:
            self.PMACSDIR = os.environ['PMACSDIR']
        else:
            self.PMACSDIR = None

        self.SRCDIR = os.path.dirname(os.path.abspath(__file__))
        self.INITFILE = "init"
        self.MODULEDIR = self.SRCDIR + "/modules/"
        sys.path.append(self.MODULEDIR)
        self.CONFIGDIR = self.SRCDIR + "/config/"
        self.THEMEDIR = self.SRCDIR + "/themes/"

        # initialize class variables
        self.vlayout = QtGui.QVBoxLayout()  # main layout container
        self.shortcut_dict = {}                       # contains functions mapped to keystr. Used for keybinding
        self.macro = []                                   # record commands for the current macro
        self.macro_flag = False
        self.stacks = []                                   # record all stacks
        self.widgets = []                                # record ALL widgets
        self.minibuffer = None
        self.next_buffer_id = 0                      # ID given to next buffer. ID is the same for every stack.
        self.current_stack = None
        self.current_widget = None
        self.primary_mode_dict = {}            # list of available modes with init functions
        self.settings = {}

        self.special_chars = re.compile('[@_!#$%^&*()<>?/\|}{~:\[\]\\\,.\'\"+-=\` ]')

        # load core pmacs init
        self.load_core_init_file()
        
        # load all other functions and configuration from init file
        # self.load_init_file()

        # run initialization functions
        self.load_theme() # load qss theme and apply to Frame
        self.init_stacks() # create a stack and scratch and debug buffers
        self.init_minibuffer()
        self.init_layout() # initialize layout of windows

        
    # Event Filter used for all objects to capture keypresses
    def eventFilter(self, sourceObj, event):
        if event.type() == QtCore.QEvent.FocusIn:
            for stack in self.stacks:
                if sourceObj in stack.children():
                    self.current_stack = stack
                    break
            if sourceObj in self.widgets:
                self.current_widget = sourceObj
            return super(Frame, self).eventFilter(sourceObj, event)

        elif event.type() == QtCore.QEvent.ShortcutOverride:
            return True
        elif event.type() == QtCore.QEvent.KeyPress:
            char = str(event.text())
            key = event.key()
            if char.isalnum() or self.special_chars.search(char):
                self.current_widget.cursor.insert(char)
            else:
                return self.current_widget.cursor.default_event_handler(sourceObj, event)
            return True
        else:
            return super(Frame, self).eventFilter(sourceObj, event)
    
    # load module from py file in module directory
    def require(self, module_name, obj=None):
        module_name = os.path.splitext(os.path.split(str(self.MODULEDIR+module_name))[1])[0]
        module = importlib.import_module(module_name)
        if not obj:
            obj = "Frame"

        functions = [f[0] for f in inspect.getmembers(module) if inspect.isfunction(f[1])] # only get functions from the module
        on_load = False
        for f in functions:
            if f == "INIT":
                exec (str('self.primary_mode_dict[\'' + module_name + '\'] = module.' + f), globals(), locals())
            elif f == "ON_LOAD":
                on_load = True
            else:
                exec (str(obj + "." + f + "= module." + f), globals(), locals())
        if on_load:
            module.ON_LOAD(self)

    # executes configuration commands from init file
    def load_core_init_file(self):
        self.eval_file(self.CONFIGDIR + self.INITFILE + ".pm")
            
    # executes configuration commands from init file
    def load_init_file(self):
        self.eval_file(self.PMACSDIR + self.INITFILE + ".pm")

        
    # Eval Functions

    def eval_file(self, filename):
        try:
            lines = []
            with open(filename, 'r') as f:
                line = f.readline()
                while line:
                    lines.append(line)
                    line = f.readline()
            self.eval_lines(lines)
        except IOError:
            self.log_message(filename + " does not exist.")


    def eval_lines(self, lines):
        for line in lines:
            self.eval_line(line)


    def eval_line(self, line):
        #try:
        exec (str(line), globals(), locals())
        #except:
            #self.log_message("Eval Failed: " + line)
            
    # temp error logging function
    def log_message(self, message):
        print message
