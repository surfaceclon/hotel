from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from insertBooking import insertbooking
import showRoom
from showRoom import showroom
from delBook import delbooking
import sqlite3

def AddBooking(self):
    self.wid_1 = QWidget(self)
    self.wid_1.setGeometry(20, 60, 855, 577)
    self.wid_1.setStyleSheet(
        'background-color: lightgray;\n'
        'border-radius: 7px;\n'
    )
    #------------------------------------
    self.all_room_l = QLabel(self.wid_1)
    self.all_room_l.setText('All rooms')
    self.all_room_l.setGeometry(40, 15, 60, 20)
    self.all_room_l.setStyleSheet(
        'font-weight: bold;\n'
    )

    self.free_room_l = QLabel(self.wid_1)
    self.free_room_l.setText('Free rooms')
    self.free_room_l.setGeometry(215, 15, 65, 20)
    self.free_room_l.setStyleSheet(
        'font-weight: bold;\n'
    )

    self.id_number_l = QLabel(self.wid_1)
    self.id_number_l.setText('id room')
    self.id_number_l.setGeometry(40, 155, 65, 20)
    self.id_number_l.setStyleSheet(
        'font-weight: bold;\n'
    )

    self.id_client_l = QLabel(self.wid_1)
    self.id_client_l.setText('id client')
    self.id_client_l.setGeometry(215, 155, 65, 20)
    self.id_client_l.setStyleSheet(
        'font-weight: bold;\n'
    )

    self.data_in_l = QLabel(self.wid_1)
    self.data_in_l.setText('data in')
    self.data_in_l.setGeometry(390, 155, 65, 20)
    self.data_in_l.setStyleSheet(
        'font-weight: bold;\n'
    )

    self.data_out_l = QLabel(self.wid_1)
    self.data_out_l.setText('data out')
    self.data_out_l.setGeometry(565, 155, 65, 20)
    self.data_out_l.setStyleSheet(
        'font-weight: bold;\n'
    )

    self.number_l = QLabel(self.wid_1)
    self.number_l.setText('Room')
    self.number_l.setGeometry(740, 155, 65, 20)
    self.number_l.setStyleSheet(
        'font-weight: bold;\n'
    )

    self.style = QLabel(self.wid_1)
    self.style.setGeometry(70, 300, 900, 200)
    self.style.setStyleSheet(
        'font-weight: bold;\n'
        'background-color: white;\n'
    )

    #--------------------------------------

    self.list_view = QListWidget(self.wid_1)
    self.list_view.setStyleSheet(
        'background-color: white;\n'
        'font-weight: bold;\n'
    )
    self.list_view.setGeometry(10,40,150,100)

    self.numers = QListWidget(self.wid_1)
    self.numers.setStyleSheet(
        'background-color: white;\n'
        'font-weight: bold;\n'
    )
    self.numers.setGeometry(180,40,150,100)

    self.id_booking = QLabel(self.wid_1)
    self.id_booking.setText('ID booking')
    self.id_booking.setGeometry(375, 85, 65, 20)
    self.id_booking.setStyleSheet(
        'font-weight: bold;\n'
    )

    self.id_booking = QLineEdit(self.wid_1)
    self.id_booking.setStyleSheet(
        'background-color: white;\n'
        'font-weight: bold;\n'
    )
    self.id_booking.setGeometry(350,110,150,30)

    #--------------------------------------

    def update():
        self.numers.clear()
        self.list_view.clear()
        showroom()

        for i in showRoom.number:
            self.numers.addItem(f'Numers: {i}')

        for i in showRoom.number_all:
            self.list_view.addItem(f'Room: {i}')
    #------------------------------------

    self.id_namber = QLineEdit(self.wid_1)
    self.id_namber.setStyleSheet(
        'background-color: white;\n'
        'font-weight: bold;\n'
    )
    self.id_namber.setGeometry(10,180,150,30)

    self.id_client = QLineEdit(self.wid_1)
    self.id_client.setStyleSheet(
        'background-color: white;\n'
        'font-weight: bold;\n'
    )
    self.id_client.setGeometry(180,180,150,30)


    self.date_in = QLineEdit(self.wid_1)
    self.date_in.setStyleSheet(
        'background-color: white;\n'
        'font-weight: bold;\n'
    )
    self.date_in.setGeometry(350,180,150,30)

    self.date_out = QLineEdit(self.wid_1)
    self.date_out.setStyleSheet(
        'background-color: white;\n'
        'font-weight: bold;\n'
    )
    self.date_out.setGeometry(520,180,150,30)

    self.number = QLineEdit(self.wid_1)
    self.number.setStyleSheet(
        'background-color: white;\n'
        'font-weight: bold;\n'
    )
    self.number.setGeometry(690,180,150,30)

    #------------------------------------
    def add():
        id_namber = self.id_namber.text()
        id_client = self.id_client.text()
        date_in = self.date_in.text()
        date_out = self.date_out.text()
        number = self.number.text()
        insertbooking(id_namber, id_client, date_in, date_out, number)
        self.id_namber.clear()
        self.id_client.clear()
        self.date_in.clear()
        self.date_out.clear()
        self.number.clear()
        update()

    def delete():
        delet = self.id_booking.text()
        delbooking(delet)
        self.id_booking.clear()
        self.id_namber.clear()
        self.id_client.clear()
        self.date_in.clear()
        self.date_out.clear()
        self.number.clear()
        update()

    def search():
        data = []
        data.clear()
        serch = self.number.text()
        try:
            conn = sqlite3.connect('hostel.db')
            cur = conn.cursor()
            cur.execute('''
                SELECT * FROM booking WHERE number='{}';
            '''.format(int(serch)))
            for i in cur.fetchall():
                for _ in i:
                    data.append(_)
            self.id_booking.setText(str(data[0]))
            self.id_namber.setText(str(data[1]))
            self.id_client.setText(str(data[2]))
            self.date_in.setText(str(data[3]))
            self.date_out.setText(str(data[4]))
        except:
            pass
        finally:
            conn.close()

    def clear():
        self.id_booking.clear()
        self.id_namber.clear()
        self.id_client.clear()
        self.date_in.clear()
        self.date_out.clear()
        self.number.clear()

    self.search = QPushButton(self.wid_1)
    self.search.setText('SEARCH')
    self.search.setStyleSheet(
        'background-color: #808080;\n'
        'border-radius: 7px;\n'
        'font-weight: bold;\n'
    )
    self.search.setGeometry(10,230,150,30)
    self.search.clicked.connect(search)

    self.okBook = QPushButton(self.wid_1)
    self.okBook.setText('ADD')
    self.okBook.setStyleSheet(
        'background-color: #808080;\n'
        'border-radius: 7px;\n'
        'font-weight: bold;\n'
    )
    self.okBook.setGeometry(180,230,150,30)
    self.okBook.clicked.connect(add)
    

    self.delBook = QPushButton(self.wid_1)
    self.delBook.setText('DEL')
    self.delBook.setStyleSheet(
        'background-color: #808080;\n'
        'border-radius: 7px;\n'
        'font-weight: bold;\n'
    )
    self.delBook.setGeometry(350,230,150,30)
    self.delBook.clicked.connect(delete)

    self.update = QPushButton(self.wid_1)
    self.update.setText('UPDATE')
    self.update.setStyleSheet(
        'background-color: #808080;\n'
        'border-radius: 7px;\n'
        'font-weight: bold;\n'
    )
    self.update.setGeometry(520,230,150,30)
    self.update.clicked.connect(update)

    self.clears = QPushButton(self.wid_1)
    self.clears.setText('CLEAR')
    self.clears.setStyleSheet(
        'background-color: #808080;\n'
        'border-radius: 7px;\n'
        'font-weight: bold;\n'
    )
    self.clears.setGeometry(690,230,150,30)
    self.clears.clicked.connect(clear)

    self.wid_1.show()