import sys
from PyQt5.QtCore import (QSettings, Qt, QByteArray, QFile)
from PyQt5.QtWidgets import (QAction, QApplication, QListWidget,
                             QMainWindow, QSplitter, QTextBrowser, QTextEdit, QDesktopWidget, QFileDialog, QLabel,
                             QLineEdit, QComboBox, QPushButton, QGridLayout, QDialog, QCheckBox)
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.groupsList = QListWidget()
        self.listWidget.itemDoubleClicked.connect(self.grouplistshowItem)
        self.editor = QTextEdit()
        self.messageView = QTextBrowser()
        self.messageSplitter = QSplitter(Qt.Vertical)
        self.messageSplitter.addWidget(self.editor)
        self.messageSplitter.addWidget(self.messageView)
        self.mainSplitter = QSplitter(Qt.Horizontal)
        self.mainSplitter.addWidget(self.groupsList)
        self.mainSplitter.addWidget(self.messageSplitter)
        self.setCentralWidget(self.mainSplitter)
        self.mainSplitter.setStretchFactor(0, 1)
        self.mainSplitter.setStretchFactor(1, 3)
        self.messageSplitter.setStretchFactor(0, 1)
        self.messageSplitter.setStretchFactor(1, 2)

        self.createMenusAndToolbars()

        settings = QSettings()
        if settings.value("MainWindow/Geometry") or \
                      settings.value("MainWindow/State") or \
                      settings.value("MainSplitter"):
            self.restoreGeometry(
                    QByteArray(settings.value("MainWindow/Geometry")))
            self.restoreState(
                    QByteArray(settings.value("MainWindow/State")))
            self.messageSplitter.restoreState(
                    QByteArray(settings.value("MessageSplitter")))
            self.mainSplitter.restoreState(
                    QByteArray(settings.value("MainSplitter")))

        status = self.statusBar()
        status.setSizeGripEnabled(False)
        status.showMessage("Ready", 5000)
        self.setWindowTitle("News Reader")
        self.generateFakeData()


    def createMenusAndToolbars(self):

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


        screen = QDesktopWidget().screenGeometry()
        self.setGeometry(50, 50, screen.width() - 100, screen.height() - 100)


    def newFile(self):
        self.editor.clear()
        login = Login()
        login.show()
        login.exec_()
    def grouplistshowItem(self):

        self.databasename=split(self.currentItem().text(),".")[0]
        self.tablename=split(self.currentItem().text(),".")[1]



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



    def closeEvent(self, event):
        if self.okToContinue():
            settings = QSettings()
            settings.setValue("MainWindow/Geometry",
                              self.saveGeometry())
            settings.setValue("MainWindow/State",
                              self.saveState())
            settings.setValue("MessageSplitter",
                    self.messageSplitter.saveState())
            settings.setValue("MainSplitter",
                    self.mainSplitter.saveState())
        else:
            event.ignore()


    def okToContinue(self):
        return True


    def generateFakeData(self):
        for group in ("ada", "apl", "asm.*", "asm370", "awk", "basic.*",
                "beta", "c.*", "c++.*", "clarion", "clipper.*", "clos",
                "clu", "cobol", "dylan", "eiffel", "forth.*",
                "fortran.*", "functional", "haskell", "hermes", "icon",
                "idl", "idl-pvwave"):
            self.groupsList.addItem("comp.lang.{0}".format(group))
        for topic, author in (
                ):
            self.editor.addItem("{0} from {1}".format(topic, author))

class Login(QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.DataNameLabel = QLabel('DataBase:')
        self.DataName = QLineEdit()
        self.Tablenamelabel = QLabel('Table:')
        self.Tablename = QLineEdit()
        self.table_num = QLabel('Table_num:')
        self.Tablenum = QLineEdit()
        self.mysql_hive = QLabel('Type:')
        self.mysql_hive_combo = QComboBox()
        self.mysql_hive_combo.addItem("MySQL")
        self.mysql_hive_combo.addItem("Hive")
        self.buttonLogin = QPushButton('Submit')
        self.setWindowTitle('Submit')
        self.dictionary=QLabel("Dictionary:")
        self.texteditfile=QLineEdit()
        self.file_location=QPushButton("···")
        self.file_location.setStyleSheet('QPushButton {font: 7px}')

        self.layout = QGridLayout()
        self.layout.setSpacing(10)
        self.layout.addWidget(self.DataNameLabel, 0, 0)
        self.layout.addWidget(self.DataName, 0, 1)
        self.layout.addWidget(self.Tablenamelabel, 1, 0)
        self.layout.addWidget(self.Tablename, 1, 1)
        self.layout.addWidget(self.mysql_hive, 2, 0)
        self.layout.addWidget(self.mysql_hive_combo, 2, 1)
        self.layout.addWidget(self.dictionary, 3, 0)
        self.layout.addWidget(self.texteditfile, 3, 1)
        self.layout.addWidget(self.file_location, 3, 2)
        self.layout.addWidget(self.buttonLogin, 4, 1)

        self.setLayout(self.layout)

class QCheckBox_fieldlist(QCheckBox):
    def __init__(self,parent=none):
        super(QCheckBox_fieldlist, self).__init__(parent)
        data_set=





if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setOrganizationName("Qtrac Ltd.")
    app.setOrganizationDomain("qtrac.eu")
    app.setApplicationName("News Reader")
    form = MainWindow()
    form.show()
    app.exec_()