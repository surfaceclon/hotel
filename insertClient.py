import sqlite3

def insertclient(name, surname, patronymic, birthday, phone, email, organization):
    data = [
        (name, surname, patronymic, birthday, int(phone), email, organization),
    ]

    try:
        conn = sqlite3.connect('hostel.db')
        cur = conn.cursor()
        cur.executemany('''
            INSERT INTO list_of_clients(name, surname, patronymic, birthday, phone, email, organization) 
            VALUES(?, ?, ?, ?, ?, ?, ?);
        ''', data)
        conn.commit()
    except:
        pass
    finally:
        conn.close()