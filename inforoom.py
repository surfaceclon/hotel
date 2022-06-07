from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sqlite3

def InfoRoom(self):
    self.wid_5 = QWidget(self)
    self.wid_5.setGeometry(20, 60, 855, 577)
    self.wid_5.setStyleSheet(
        'background-color: lightgray;\n'
        'border-radius: 7px;\n'
    )
    #----------------------------------

    self.style = QLabel(self.wid_5)
    self.style.setGeometry(70, 300, 900, 200)
    self.style.setStyleSheet(
        'font-weight: bold;\n'
        'background-color: white;\n'
    )
    #----------------------------------
    self.field_num = QLineEdit(self.wid_5)
    self.field_num.setStyleSheet(
        'background-color: white;\n'
        'font-weight: bold;\n'
    )
    self.field_num.setGeometry(10,100,150,30)

    #----------------------------------
    def room():
        field_num = self.field_num.text()
        try:
            data = []
            data.clear()
            conn = sqlite3.connect('hostel.db')
            cur = conn.cursor()
            cur.execute('''
                SELECT list_of_numbers.id_number, room_information.class_number, room_information.num_of_rooms,
                room_information.num_of_beds, room_information.price FROM
                list_of_numbers JOIN room_information ON room_information.id_number = list_of_numbers.id_number
                WHERE list_of_numbers.number = '{}';
            '''.format(field_num))
            for i in cur.fetchall():
                for _ in i:
                    data.append(_)
            self.number_s.setText(str(data[0]))
            self.class_ss.setText(str(data[1]))
            self.num_of_rums_s.setText(str(data[2]))
            self.num_of_beds_s.setText(str(data[3]))
            self.price_s.setText(str(data[4]))
        except:
            pass
        finally:
            conn.close()

    def clears():
        self.number_s.clear()
        self.class_ss.clear()
        self.num_of_rums_s.clear()
        self.num_of_beds_s.clear()
        self.price_s.clear()
        self.field_num.clear()

    #----------------------------------
    self.butShow = QPushButton(self.wid_5)
    self.butShow.setText('SHOW')
    self.butShow.setStyleSheet(
        'background-color: #808080;\n'
        'border-radius: 7px;\n'
        'font-weight: bold;\n'
    )
    self.butShow.setGeometry(180,100,150,30)
    self.butShow.clicked.connect(room)

    self.clear = QPushButton(self.wid_5)
    self.clear.setText('CLEAR')
    self.clear.setStyleSheet(
        'background-color: #808080;\n'
        'border-radius: 7px;\n'
        'font-weight: bold;\n'
    )
    self.clear.setGeometry(350,100,150,30)
    self.clear.clicked.connect(clears)
    #----------------------------------

    self.number = QLabel(self.wid_5)
    self.number.setText('ID number')
    self.number.setGeometry(40, 155, 65, 20)
    self.number.setStyleSheet(
        'font-weight: bold;\n'
    )

    self.class_s = QLabel(self.wid_5)
    self.class_s.setText('Class')
    self.class_s.setGeometry(215, 155, 65, 20)
    self.class_s.setStyleSheet(
        'font-weight: bold;\n'
    )

    self.num_of_rums = QLabel(self.wid_5)
    self.num_of_rums.setText('Num of rooms')
    self.num_of_rums.setGeometry(390, 155, 65, 20)
    self.num_of_rums.setStyleSheet(
        'font-weight: bold;\n'
    )

    self.num_of_beds = QLabel(self.wid_5)
    self.num_of_beds.setText('Num of beds')
    self.num_of_beds.setGeometry(565, 155, 65, 20)
    self.num_of_beds.setStyleSheet(
        'font-weight: bold;\n'
    )

    self.price = QLabel(self.wid_5)
    self.price.setText('Price')
    self.price.setGeometry(740, 155, 65, 20)
    self.price.setStyleSheet(
        'font-weight: bold;\n'
    )
    #------------------------------------------

    self.number_s = QLineEdit(self.wid_5)
    self.number_s.setStyleSheet(
        'background-color: white;\n'
        'font-weight: bold;\n'
    )
    self.number_s.setGeometry(10,180,150,30)

    self.class_ss = QLineEdit(self.wid_5)
    self.class_ss.setStyleSheet(
        'background-color: white;\n'
        'font-weight: bold;\n'
    )
    self.class_ss.setGeometry(180,180,150,30)


    self.num_of_rums_s = QLineEdit(self.wid_5)
    self.num_of_rums_s.setStyleSheet(
        'background-color: white;\n'
        'font-weight: bold;\n'
    )
    self.num_of_rums_s.setGeometry(350,180,150,30)

    self.num_of_beds_s = QLineEdit(self.wid_5)
    self.num_of_beds_s.setStyleSheet(
        'background-color: white;\n'
        'font-weight: bold;\n'
    )
    self.num_of_beds_s.setGeometry(520,180,150,30)

    self.price_s = QLineEdit(self.wid_5)
    self.price_s.setStyleSheet(
        'background-color: white;\n'
        'font-weight: bold;\n'
    )
    self.price_s.setGeometry(690,180,150,30)

    self.wid_5.show()