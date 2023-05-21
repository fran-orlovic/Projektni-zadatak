from PyQt5 import QtWidgets, QtGui, QtCore
import sys

from korisnik import TipKorisnika
from korisnik import PoslovniKorisnik, PrivatniKorisnik
from utilities import provjera_informacija

korisnici = []


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 400)
        self.setWindowTitle('Objektno')
        self.setWindowIcon(QtGui.QIcon('images/python.png'))
        self.initUI()

    def initUI(self):
        offset = 30
        self.font = QtGui.QFont('Helvetica', 10)

        # Input tip korisnika
        self.tip_korisnika = QtWidgets.QComboBox(self)

        for korisnik in TipKorisnika:
            self.tip_korisnika.addItem(str(korisnik.value))

        self.tip_korisnika.setGeometry(QtCore.QRect(150, offset, 150, 25))
        self.tip_korisnika.currentTextChanged.connect(self.on_combobox_changed)

        # Label telefon
        self.label_telefon = QtWidgets.QLabel(self)
        self.label_telefon.setFont(self.font)
        self.label_telefon.setText('Telefon')
        self.label_telefon.move(50, offset * 2)

        # Input telefon
        self.text_telefon = QtWidgets.QLineEdit(self)
        self.text_telefon.setGeometry(QtCore.QRect(150, offset * 2, 150, 25))

        # Label email
        self.label_email = QtWidgets.QLabel(self)
        self.label_email.setFont(self.font)
        self.label_email.setText('Email')
        self.label_email.move(50, offset * 3)

        # Input email
        self.text_email = QtWidgets.QLineEdit(self)
        self.text_email.setGeometry(QtCore.QRect(150, offset * 3, 150, 25))

        # Label naziv
        self.label_naziv = QtWidgets.QLabel(self)
        self.label_naziv.setFont(self.font)
        self.label_naziv.setText('Naziv')
        self.label_naziv.move(50, offset * 4)

        # Input naziv
        self.text_naziv = QtWidgets.QLineEdit(self)
        self.text_naziv.setGeometry(QtCore.QRect(150, offset * 4, 150, 25))

        # Label web
        self.label_web = QtWidgets.QLabel(self)
        self.label_web.setFont(self.font)
        self.label_web.setText('Web')
        self.label_web.move(50, offset * 5)

        # Input web
        self.text_web = QtWidgets.QLineEdit(self)
        self.text_web.setGeometry(QtCore.QRect(150, offset * 5, 150, 25))

        # Label ime
        self.label_ime = QtWidgets.QLabel(self)
        self.label_ime.setFont(self.font)
        self.label_ime.setText('Ime')
        self.label_ime.move(50, offset * 4)

        # Input ime
        self.text_ime = QtWidgets.QLineEdit(self)
        self.text_ime.setGeometry(QtCore.QRect(150, offset * 4, 150, 25))

        # Label prezime
        self.label_prezime = QtWidgets.QLabel(self)
        self.label_prezime.setFont(self.font)
        self.label_prezime.setText('Prezime')
        self.label_prezime.move(50, offset * 5)


        # Input prezime
        self.text_prezime = QtWidgets.QLineEdit(self)
        self.text_prezime.setGeometry(QtCore.QRect(150, offset * 5, 150, 25))

        # Mora se hideat zbog pocetnog stanja
        self.label_prezime.hide()
        self.text_prezime.hide()
        self.label_ime.hide()
        self.text_ime.hide()

        # Error label
        self.label_error = QtWidgets.QLabel(self)
        self.label_error.setFont(self.font)
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setStyleSheet('color: red;')
        self.label_error.setGeometry(QtCore.QRect(50, offset * 6, 250, 30))

        # Gumb unos korisnika
        self.unos_korisnika_button = QtWidgets.QPushButton(self)
        self.unos_korisnika_button.setText('Unesi korisnika')
        self.unos_korisnika_button.setGeometry(QtCore.QRect(100, offset * 7, 150, 30))
        self.unos_korisnika_button.clicked.connect(self.unos_korisnika)

    def on_combobox_changed(self):
        if self.tip_korisnika.currentText() == TipKorisnika.POSLOVNI.value:
            self.label_naziv.show()
            self.text_naziv.show()
            self.label_web.show()
            self.text_web.show()
            self.label_ime.hide()
            self.text_ime.hide()
            self.label_prezime.hide()
            self.text_prezime.hide()
        elif self.tip_korisnika.currentText() == TipKorisnika.PRIVATNI.value:
            self.label_naziv.hide()
            self.text_naziv.hide()
            self.label_web.hide()
            self.text_web.hide()
            self.label_ime.show()
            self.text_ime.show()
            self.label_prezime.show()
            self.text_prezime.show()

    def unos_korisnika(self):
        error = provjera_informacija(self.text_telefon.text(), self.text_email.text())

        if error is None:
            if self.tip_korisnika.currentText() == TipKorisnika.POSLOVNI.value:
                korisnici.append(PoslovniKorisnik(self.text_telefon.text(), self.text_email.text(),
                                                  self.text_naziv.text(), self.text_web.text()))
                trenutni_korisnik = PoslovniKorisnik(self.text_telefon.text(), self.text_email.text(),
                                                     self.text_naziv.text(), self.text_web.text())
            elif self.tip_korisnika.currentText() == TipKorisnika.PRIVATNI.value:
                korisnici.append(PrivatniKorisnik(self.text_telefon.text(), self.text_email.text(),
                                                  self.text_ime.text(), self.text_prezime.text()))
                trenutni_korisnik = PrivatniKorisnik(self.text_telefon.text(), self.text_email.text(),
                                                     self.text_ime.text(), self.text_prezime.text())

            self.text_ime.setText('')
            self.text_prezime.setText('')
            self.text_naziv.setText('')
            self.text_web.setText('')
            self.text_telefon.setText('')
            self.text_email.setText('')
            self.label_error.setText('')

            trenutni_korisnik.ispis()
        else:
            self.label_error.setText(error)


app = QtWidgets.QApplication(sys.argv)
win = App()
win.show()
sys.exit(app.exec_())
