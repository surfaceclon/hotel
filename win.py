import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from addbooking import AddBooking
from addclient import AddClient
from searchclient import SearchClient
from inforoom import InfoRoom
from databse import createdb

class MainWin(QWidget):
    def __init__(self):
        super(MainWin, self).__init__()
        createdb()
        self.setGeometry(300, 300, 900, 650)
        self.setFixedSize(self.size())
        self.setWindowTitle('HOSTEL')
        self.setStyleSheet(
            'background-color: #FFFFFF;\n'
        )
        #--------------------------------------
        self.labelButton = QLabel(self)
        self.labelButton.setStyleSheet(
            'background-color: #C0C0C0;\n'
            'border-radius: 7px;\n'
        )
        self.labelButton.setGeometry(100, 5, 900, 40)
        #----------------------------------------
        self.addBooking = QPushButton(self.labelButton)
        self.addBooking.setText('Add Booking')
        self.addBooking.setStyleSheet(
            'background-color: #808080;\n'
            'border-radius: 7px;\n'
            'font-weight: bold;\n'
        )
        self.addBooking.setGeometry(5, 5, 80, 30)
        self.addBooking.clicked.connect(self.addB)

        self.addClient = QPushButton(self.labelButton)
        self.addClient.setText('Add Client')
        self.addClient.setStyleSheet(
            'background-color: #808080;\n'
            'border-radius: 7px;\n'
            'font-weight: bold;\n'
        )
        self.addClient.setGeometry(90, 5, 80, 30)
        self.addClient.clicked.connect(self.addC)

        self.SearchClient = QPushButton(self.labelButton)
        self.SearchClient.setText('Search Client')
        self.SearchClient.setStyleSheet(
            'background-color: #808080;\n'
            'border-radius: 7px;\n'
            'font-weight: bold;\n'
        )
        self.SearchClient.setGeometry(175, 5, 80, 30)
        self.SearchClient.clicked.connect(self.searchCli)

        self.infoRoom = QPushButton(self.labelButton)
        self.infoRoom.setText('Info Room')
        self.infoRoom.setStyleSheet(
            'background-color: #808080;\n'
            'border-radius: 7px;\n'
            'font-weight: bold;\n'
        )
        self.infoRoom.setGeometry(260, 5, 80, 30)
        self.infoRoom.clicked.connect(self.infoRo)
    #----------------------------------------------
    def addB(self):
        AddBooking(self)
        self.addBooking.setStyleSheet(
            'background-color: #FFFFFF;\n'
            'border-radius: 7px;\n'
            'font-weight: bold;\n'
        )
        self.addClient.setStyleSheet(
            'background-color: #808080;\n'
            'border-radius: 7px;\n'
            'font-weight: bold;\n'
        )
        self.SearchClient.setStyleSheet(
            'background-color: #808080;\n'
            'border-radius: 7px;\n'
            'font-weight: bold;\n'
        )
        self.infoRoom.setStyleSheet(
            'background-color: #808080;\n'
            'border-radius: 7px;\n'
            'font-weight: bold;\n'
        )

    def addC(self):
        AddClient(self)
        self.addBooking.setStyleSheet(
            'background-color: #808080;\n'
            'border-radius: 7px;\n'
            'font-weight: bold;\n'
        )
        self.addClient.setStyleSheet(
            'background-color: #FFFFFF;\n'
            'border-radius: 7px;\n'
            'font-weight: bold;\n'
        )
        self.SearchClient.setStyleSheet(
            'background-color: #808080;\n'
            'border-radius: 7px;\n'
            'font-weight: bold;\n'
        )
        self.infoRoom.setStyleSheet(
            'background-color: #808080;\n'
            'border-radius: 7px;\n'
            'font-weight: bold;\n'
        )

    def searchCli(self):
        SearchClient(self)
        self.addBooking.setStyleSheet(
            'background-color: #808080;\n'
            'border-radius: 7px;\n'
            'font-weight: bold;\n'
        )
        self.addClient.setStyleSheet(
            'background-color: #808080;\n'
            'border-radius: 7px;\n'
            'font-weight: bold;\n'
        )
        self.SearchClient.setStyleSheet(
            'background-color: #FFFFFF;\n'
            'border-radius: 7px;\n'
            'font-weight: bold;\n'
        )
        self.infoRoom.setStyleSheet(
            'background-color: #808080;\n'
            'border-radius: 7px;\n'
            'font-weight: bold;\n'
        )

    def infoRo(self):
        InfoRoom(self)
        self.addBooking.setStyleSheet(
            'background-color: #808080;\n'
            'border-radius: 7px;\n'
            'font-weight: bold;\n'
        )
        self.addClient.setStyleSheet(
            'background-color: #808080;\n'
            'border-radius: 7px;\n'
            'font-weight: bold;\n'
        )
        self.SearchClient.setStyleSheet(
            'background-color: #808080;\n'
            'border-radius: 7px;\n'
            'font-weight: bold;\n'
        )
        self.infoRoom.setStyleSheet(
            'background-color: #FFFFFF;\n'
            'border-radius: 7px;\n'
            'font-weight: bold;\n'
        )


def main():
    app = QApplication(sys.argv)
    ex = MainWin()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()