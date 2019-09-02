from PyQt4 import QtGui, QtCore
from buffer import Buffer
from cursor import Cursor

class MiniBuffer(Buffer):
    def __init__(self, parent, filepath="", text="", std_modes=[], primary_mode=None):
        super(MiniBuffer, self).__init__(parent, 0, "MiniBuffer", filepath, text, std_modes, primary_mode)

        # child objects
        self.vlayout = QtGui.QVBoxLayout() # layout holds minibuffer and infobuffer
        self.infobuffer = Buffer(self)

        # init
        self.init_infobuffer()
        self.init_layout()

        self.set_height()
        self.verticalScrollBar().hide()

    def set_height(self):
        # height of window
        font_metrics = QtGui.QFontMetrics(self.currentFont())
        height = font_metrics.size(0, "ABCDEFGHIJKLMNOPQRSTUVWXYZ").height() + 30
        self.setFixedHeight(height)

    def copy(self, parent):
        newMiniBuffer = MiniBuffer(parent, self.id, self.name, self.filepath, "", self.std_modes, self.primary_mode)
        newMiniBuffer.setTextCursor(self.textCursor())
        newMiniBuffer.cursor = self.cursor.copy(newMiniBuffer)
        doc = self.document()
        newMiniBuffer.setDocument(doc)
        return newMiniBuffer

    def enter(self):
        pass
        
    def init_infobuffer(self):
        self.infobuffer.id = 0
        self.infobuffer.name = "infobuffer"        

    def init_layout(self):
        self.vlayout.addWidget(self.infobuffer)
        self.infobuffer.hide()
        self.vlayout.addWidget(self)
