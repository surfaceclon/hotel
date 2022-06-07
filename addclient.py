from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from insertClient import insertclient
from deletClient import deletclient

def AddClient(self):
    self.wid_2 = QWidget(self)
    self.wid_2.setGeometry(20, 60, 855, 577)
    self.wid_2.setStyleSheet(
        'background-color: lightgray;\n'
        'border-radius: 7px;\n'
    )
    #----------------------------------
    self.style = QLabel(self.wid_2)
    self.style.setGeometry(70, 300, 900, 200)
    self.style.setStyleSheet(
        'font-weight: bold;\n'
        'background-color: white;\n'
    )
    #-----------------------------------

    self.name_a = QLabel(self.wid_2)
    self.name_a.setGeometry(50, 124, 65, 20)
    self.name_a.setText('Name')
    self.name_a.setStyleSheet(
        'font-weight: bold;\n'
    )

    self.surname_a = QLabel(self.wid_2)
    self.surname_a.setGeometry(210, 124, 65, 20)
    self.surname_a.setText('Surame')
    self.surname_a.setStyleSheet(
        'font-weight: bold;\n'
    )

    self.patronymic_a = QLabel(self.wid_2)
    self.patronymic_a.setGeometry(373, 124, 65, 20)
    self.patronymic_a.setText('Patronymic')
    self.patronymic_a.setStyleSheet(
        'font-weight: bold;\n'
    )

    self.birthday_a = QLabel(self.wid_2)
    self.birthday_a.setGeometry(542, 124, 65, 20)
    self.birthday_a.setText('Birthday')
    self.birthday_a.setStyleSheet(
        'font-weight: bold;\n'
    )

    self.phone_a = QLabel(self.wid_2)
    self.phone_a.setGeometry(720, 124, 65, 20)
    self.phone_a.setText('Phone')
    self.phone_a.setStyleSheet(
        'font-weight: bold;\n'
    )

    self.email_a = QLabel(self.wid_2)
    self.email_a.setGeometry(50, 203, 65, 20)
    self.email_a.setText('Email')
    self.email_a.setStyleSheet(
        'font-weight: bold;\n'
    )

    self.organization_a = QLabel(self.wid_2)
    self.organization_a.setGeometry(210, 203, 68, 20)
    self.organization_a.setText('Organization')
    self.organization_a.setStyleSheet(
        'font-weight: bold;\n'
    )

    self.id_clients = QLabel(self.wid_2)
    self.id_clients.setText('ID Client')
    self.id_clients.setStyleSheet(
        'font-weight: bold;\n'
    )
    self.id_clients.setGeometry(740, 203, 68, 20)

    #-----------------------------------

    self.name = QLineEdit(self.wid_2)
    self.name.setStyleSheet(
        'background-color: white;\n'
        'font-weight: bold;\n'
    )
    self.name.setGeometry(10,150,150,30)

    self.surname = QLineEdit(self.wid_2)
    self.surname.setStyleSheet(
        'background-color: white;\n'
        'font-weight: bold;\n'
    )
    self.surname.setGeometry(180,150,150,30)

    self.patronymic = QLineEdit(self.wid_2)
    self.patronymic.setStyleSheet(
        'background-color: white;\n'
        'font-weight: bold;\n'
    )
    self.patronymic.setGeometry(350,150,150,30)

    self.birthday = QLineEdit(self.wid_2)
    self.birthday.setStyleSheet(
        'background-color: white;\n'
        'font-weight: bold;\n'
    )
    self.birthday.setGeometry(520,150,150,30)

    self.phone = QLineEdit(self.wid_2)
    self.phone.setStyleSheet(
        'background-color: white;\n'
        'font-weight: bold;\n'
    )
    self.phone.setGeometry(690,150,150,30)

    self.email = QLineEdit(self.wid_2)
    self.email.setStyleSheet(
        'background-color: white;\n'
        'font-weight: bold;\n'
    )
    self.email.setGeometry(10,230,150,30)

    self.organization = QLineEdit(self.wid_2)
    self.organization.setFixedSize(150,30)
    self.organization.setStyleSheet(
        'background-color: white;\n'
        'font-weight: bold;\n'
    )
    self.organization.setGeometry(180,230,150,30)

    self.id_client = QLineEdit(self.wid_2)
    self.id_client.setFixedSize(150,30)
    self.id_client.setStyleSheet(
        'background-color: white;\n'
        'font-weight: bold;\n'
    )
    self.id_client.setGeometry(690,230,150,30)

    #------------------------------------------
    def add():
        name = self.name.text()
        surname = self.surname.text()
        patronymic = self.patronymic.text()
        birthday = self.birthday.text()
        phone = self.phone.text()
        email = self.email.text()
        organization = self.organization.text()
        insertclient(name, surname, patronymic, birthday, phone, email, organization)
        self.name.clear()
        self.surname.clear()
        self.patronymic.clear()
        self.birthday.clear()
        self.phone.clear()
        self.email.clear()
        self.organization.clear()

    def delete():
        delet = self.id_client.text()
        deletclient(delet)
        self.id_client.clear()


    self.okBook = QPushButton(self.wid_2)
    self.okBook.setText('ADD')
    self.okBook.setStyleSheet(
        'background-color: #808080;\n'
        'border-radius: 7px;\n'
        'font-weight: bold;\n'
    )
    self.okBook.setGeometry(350,230,150,30)
    self.okBook.clicked.connect(add)

    self.delClient = QPushButton(self.wid_2)
    self.delClient.setText('DEL')
    self.delClient.setStyleSheet(
        'background-color: #808080;\n'
        'border-radius: 7px;\n'
        'font-weight: bold;\n'
    )
    self.delClient.setGeometry(520,230,150,30)
    self.delClient.clicked.connect(delete)

    self.wid_2.show()