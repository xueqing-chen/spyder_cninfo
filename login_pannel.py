from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QLineEdit, QPushButton, QMessageBox, \
    QLabel, QGridLayout, QComboBox, QMenu, QInputDialog


class Login(QDialog):
    def __init__(self, parent=None):

        super(Login, self).__init__(parent)

        self.userNameLabel = QLabel('User:')
        self.userName = QLineEdit()
        self.userPwdLabel = QLabel('Password:')
        self.userPwd = QLineEdit()
        self.userPwd.setEchoMode(QLineEdit.Password)
        self.mysql_hive = QLabel('Type:')
        self.mysql_hive_combo = QComboBox()
        self.mysql_hive_combo.addItem("MySQL")
        self.mysql_hive_combo.addItem("Hive")
        self.buttonLogin = QPushButton('Login')
        self.buttonLogin.clicked.connect(self.handleLogin)
        self.setWindowTitle('Login')
        self.layout = QGridLayout()
        self.layout.setSpacing(10)
        self.layout.addWidget(self.userNameLabel, 0, 0)
        self.layout.addWidget(self.userName, 0, 1)
        self.layout.addWidget(self.userPwdLabel, 1, 0)
        self.layout.addWidget(self.userPwd, 1, 1)
        self.layout.addWidget(self.mysql_hive, 2, 0)
        self.layout.addWidget(self.mysql_hive_combo, 2, 1)
        # self.layout.addWidget(self.userNameLabel, 3, 0)
        self.layout.addWidget(self.buttonLogin, 3, 1)
        self.setLayout(self.layout)

    def handleLogin(self):
        if (self.userName.text() == 'admin' and
                    self.userPwd.text() == '0'):
            self.accept()
        else:
            QMessageBox.warning(
                self, 'Error', 'Bad user or password')



if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    login = Login()

    if login.exec_() == QDialog.Accepted:
        window = Window()
        window.show()
        sys.exit(app.exec_())