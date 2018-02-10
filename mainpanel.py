import sys

from PyQt5.QtCore import QFile
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QMenu, QAction, QApplication, QDesktopWidget, QFileDialog, QTextEdit, \
    QVBoxLayout, QPushButton, QWidget

from pyCreateIDE.codeHighlight import Highlighter


class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setWindowTitle('Database IDE')
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction("new...",self.newFile, "Ctrl+N")
        fileMenu.addAction("open...",self.openfile,"Ctrl+O")
        fileMenu.addAction("save...",self.savefile,"Ctrl+S")
        fileMenu.addAction("save_as...",self.save_asfile,"Ctrl+Shift+S")
        fileMenu.addAction("E&xit", QApplication.instance().quit, "Ctrl+Q")
        fileMenu2 = menubar.addMenu('Settings')
        fileMenu2.addAction("Preference", self.setting, "Ctrl+T")
        app.setStyleSheet('menuBar::item{spacing:100px;margin:100px;}')

        self.form_widget = FormWidget(self)
        self.setCentralWidget(self.form_widget)

        screen = QDesktopWidget().screenGeometry()
        self.setGeometry(50, 50, screen.width() - 100, screen.height() - 100)
        self.show()


    def newFile(self):
         pass

    # add file location
    def openfile(self,path=None):
        if not path:
            path, _ = QFileDialog.getOpenFileName(self, "Open File", '',
                    "SQL Files (*.sql,*.*)")

        if path:
            inFile = QFile(path)
            if inFile.open(QFile.ReadOnly | QFile.Text):
                text = inFile.readAll()

                try:
                    # Python v3.
                    text = str(text, encoding='ascii')
                except TypeError:
                    # Python v2.
                    text = str(text)

                self.editor.setPlainText(text)

    def savefile(self):
         ...
    def save_asfile(self):
         ...
    def setting(self):
        ...


class FormWidget(QWidget):

    def __init__(self, parent):
        super(FormWidget, self).__init__(parent)
        self.setupEditor()

    def setupEditor(self):
        font = QFont()
        font.setFamily('Courier')
        font.setFixedPitch(True)
        font.setPointSize(10)
        self.editor = QTextEdit()
        self.editor.setFont(font)
        self.highlighter = Highlighter(self.editor.document())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
    #
    #
    # def initUI(self):
    #     okButton = QPushButton("OK")
    #     cancelButton = QPushButton("Cancel")
    #
    #     hbox = QHBoxLayout()
    #     hbox.addStretch(1)
    #     hbox.addWidget(okButton)
    #     hbox.addWidget(cancelButton)
    #
    #     vbox = QVBoxLayout()
    #     vbox.addStretch(1)
    #     vbox.addLayout(hbox)
    #
    #     self.setLayout(vbox)
    #
    #     self.setGeometry(300, 300, 300, 150)
    #     self.setWindowTitle('Buttons')
    #     self.show()
