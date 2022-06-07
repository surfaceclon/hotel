import sqlite3

def createdb():
    try:
        conn = sqlite3.connect('hostel.db')
        cur = conn.cursor()

        cur.execute('''
            CREATE TABLE IF NOT EXISTS list_of_numbers(
            id_number integer NOT NUll,
            number int(4) NOT NUll,
            floor int(20) NOT NUll,
            FOREIGN KEY (id_number) REFERENCES room_information(id_number)
            PRIMARY KEY (id_number));
        ''')

        cur.execute('''
            CREATE TABLE IF NOT EXISTS room_information(
            id_number INTEGER NOT NULL,
            class_number varchar(1) NOT NULL,
            num_of_rooms int(1) NOT NULL,
            num_of_beds int(1) NOT NULL,
            price int(6) NOT NULL CHECK(price>0),
            PRIMARY KEY (id_number));
        ''')

        cur.execute('''
            CREATE TABLE IF NOT EXISTS booking(
            id_booking INTEGER NOT NULL,
            id_number int NOT NULL,
            id_client int NOT NULL,
            date_in TEXT NOT NULL,
            date_out TEXT NOT NULL,
            number int(4) NOT NULL,
            PRIMARY KEY (id_booking),
            FOREIGN KEY (id_number) REFERENCES list_of_numbers(id_number),
            FOREIGN KEY (id_client) REFERENCES list_of_clients(id_client));
        ''')

        cur.execute('''
            CREATE TABLE IF NOT EXISTS list_of_clients(
            id_client INTEGER NOT NULL,
            name TEXT(50) NOT NULL,
            surname TEXT(50) NOT NULL,
            patronymic TEXT(50),
            birthday TEXT NOT NULL,
            phone INT(20) NOT NULL,
            email TEXT(50),
            organization TEXT(50),
            PRIMARY KEY (id_client));
        ''')
        conn.commit()
    except:
        pass

    finally:
        conn.close()

# INSERT INTO room_information(class_number, num_of_rooms, num_of_beds, price)
# VALUES('A', 1, 2, 5000);

# INSERT INTO list_of_numbers(id_number ,number, floor)
# VALUES(4, 4, 1);

# INSERT INTO list_of_clients(name, surname, patronymic, birthday, phone, email, organization) 
# VALUES('Andrey', 'Malkov', 'Ivanov', '22-05-1989', 78328762345, 'malk@mail.ru', '');

# INSERT INTO booking(id_number, id_client, date_in, date_out, number)
# VALUES(4, 3, '12-02-2020', '22-02-2020', 4);

