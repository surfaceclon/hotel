import sqlite3

def insertbooking(id_namber, id_client, date_in, date_out, number):

    try:
        conn = sqlite3.connect('hostel.db')
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO booking(id_number, id_client, date_in, date_out, number)
            VALUES('{}', '{}', '{}', '{}', '{}');
        '''.format(int(id_namber), int(id_client), date_in, date_out, int(number)))
        conn.commit()
    except:
        pass
    finally:
        conn.close()
