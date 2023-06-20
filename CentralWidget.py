from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QSlider, QTextEdit, QTextBrowser, QGridLayout, QLabel, QPushButton, QLineEdit, \
    QApplication, QMessageBox


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.loginbutton = QPushButton(self)
        self.loginbutton.setText("Login")
        self.loginbutton.clicked.connect(self.einloggen)


        self.benutzername = QLabel(self)
        self.benutzername.setText("Benutzername")

        self.passwort = QLabel(self)
        self.passwort.setText("Passwort")


        self.loginline = QLineEdit(self)

        self.lineschliesen = QLineEdit(self)
        self.lineschliesen.setEchoMode(QLineEdit.EchoMode.Password)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.benutzername, 1, 1)
        self.layout.addWidget(self.loginline, 1, 2)
        self.layout.addWidget(self.passwort, 2, 1)
        self.layout.addWidget(self.lineschliesen, 2, 2)
        self.layout.addWidget(self.loginbutton, 3, 1, 1, 2)

        self.setLayout(self.layout)

    def einloggen (self):
        if self.lineschliesen.text() == "asdf1234" and self.loginline.text() == "Julian":
            QMessageBox.information(self, "Success", "Success")
        else:
            QMessageBox.information(self, "Passwort Falsch", "Passwort Falsch")

