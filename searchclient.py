from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sqlite3

def SearchClient(self):
    self.wid_4 = QWidget(self)
    self.wid_4.setGeometry(20, 60, 855, 577)
    self.wid_4.setStyleSheet(
        'background-color: lightgray;\n'
        'border-radius: 7px;\n'
    )
    #-------------------------------------

    self.name_a = QLabel(self.wid_4)
    self.name_a.setGeometry(50, 124, 65, 20)
    self.name_a.setText('Name')
    self.name_a.setStyleSheet(
        'font-weight: bold;\n'
    )

    self.surname_a = QLabel(self.wid_4)
    self.surname_a.setGeometry(210, 124, 65, 20)
    self.surname_a.setText('Surame')
    self.surname_a.setStyleSheet(
        'font-weight: bold;\n'
    )

    self.patronymic_a = QLabel(self.wid_4)
    self.patronymic_a.setGeometry(373, 124, 65, 20)
    self.patronymic_a.setText('Patronymic')
    self.patronymic_a.setStyleSheet(
        'font-weight: bold;\n'
    )

    self.birthday_a = QLabel(self.wid_4)
    self.birthday_a.setGeometry(542, 124, 65, 20)
    self.birthday_a.setText('Birthday')
    self.birthday_a.setStyleSheet(
        'font-weight: bold;\n'
    )

    self.phone_a = QLabel(self.wid_4)
    self.phone_a.setGeometry(720, 124, 65, 20)
    self.phone_a.setText('Phone')
    self.phone_a.setStyleSheet(
        'font-weight: bold;\n'
    )

    self.email_a = QLabel(self.wid_4)
    self.email_a.setGeometry(50, 203, 65, 20)
    self.email_a.setText('Email')
    self.email_a.setStyleSheet(
        'font-weight: bold;\n'
    )

    self.organization_a = QLabel(self.wid_4)
    self.organization_a.setGeometry(210, 203, 68, 20)
    self.organization_a.setText('Organization')
    self.organization_a.setStyleSheet(
        'font-weight: bold;\n'
    )

    self.id_client = QLabel(self.wid_4)
    self.id_client.setGeometry(740, 203, 68, 20)
    self.id_client.setText('ID Client')
    self.id_client.setStyleSheet(
        'font-weight: bold;\n'
    )

    self.style = QLabel(self.wid_4)
    self.style.setGeometry(70, 300, 900, 200)
    self.style.setStyleSheet(
        'font-weight: bold;\n'
        'background-color: white;\n'
    )

    #-----------------------------------

    self.name = QLineEdit(self.wid_4)
    self.name.setStyleSheet(
        'background-color: white;\n'
        'font-weight: bold;\n'
    )
    self.name.setGeometry(10,150,150,30)

    self.surname = QLineEdit(self.wid_4)
    self.surname.setStyleSheet(
        'background-color: white;\n'
        'font-weight: bold;\n'
    )
    self.surname.setGeometry(180,150,150,30)

    self.patronymic = QLineEdit(self.wid_4)
    self.patronymic.setStyleSheet(
        'background-color: white;\n'
        'font-weight: bold;\n'
    )
    self.patronymic.setGeometry(350,150,150,30)

    self.birthday = QLineEdit(self.wid_4)
    self.birthday.setStyleSheet(
        'background-color: white;\n'
        'font-weight: bold;\n'
    )
    self.birthday.setGeometry(520,150,150,30)

    self.phone = QLineEdit(self.wid_4)
    self.phone.setStyleSheet(
        'background-color: white;\n'
        'font-weight: bold;\n'
    )
    self.phone.setGeometry(690,150,150,30)

    self.email = QLineEdit(self.wid_4)
    self.email.setStyleSheet(
        'background-color: white;\n'
        'font-weight: bold;\n'
    )
    self.email.setGeometry(10,230,150,30)

    self.organization = QLineEdit(self.wid_4)
    self.organization.setFixedSize(150,30)
    self.organization.setStyleSheet(
        'background-color: white;\n'
        'font-weight: bold;\n'
    )
    self.organization.setGeometry(180,230,150,30)

    self.id_client = QLineEdit(self.wid_4)
    self.id_client.setStyleSheet(
        'background-color: white;\n'
        'font-weight: bold;\n'
    )
    self.id_client.setGeometry(690,230,150,30)

    #-----------------------------------
    def search():
        name = self.name.text()
        surname = self.surname.text()
        patronymic = self.patronymic.text()

        try:
            data = []
            data.clear()
            conn = sqlite3.connect('hostel.db')
            cur = conn.cursor()
            cur.execute('''
                SELECT name, surname, patronymic, birthday, phone, email, organization, id_client FROM list_of_clients
                WHERE name = '{}' AND surname = '{}' AND patronymic = '{}';
            '''.format(name, surname, patronymic))
            for i in cur.fetchall():
                for _ in i:
                    data.append(_)
            self.birthday.setText(data[3])
            self.phone.setText(str(data[4]))
            self.email.setText(str(data[5]))
            self.organization.setText(str(data[6]))
            self.id_client.setText(str(data[7]))
        except:
            pass
        finally:
            conn.close()

    def clears():
        self.name.clear()
        self.surname.clear()
        self.patronymic.clear()
        self.birthday.clear()
        self.phone.clear()
        self.email.clear()
        self.organization.clear()
        self.id_client.clear()

    self.search = QPushButton(self.wid_4)
    self.search.setText('SEARCH')
    self.search.setStyleSheet(
        'background-color: #808080;\n'
        'border-radius: 7px;\n'
        'font-weight: bold;\n'
    )
    self.search.setGeometry(350,230,150,30)
    self.search.clicked.connect(search)

    self.clear_f = QPushButton(self.wid_4)
    self.clear_f.setText('CLEAR')
    self.clear_f.setStyleSheet(
        'background-color: #808080;\n'
        'border-radius: 7px;\n'
        'font-weight: bold;\n'
    )
    self.clear_f.setGeometry(520,230,150,30)
    self.clear_f.clicked.connect(clears)

    self.wid_4.show()