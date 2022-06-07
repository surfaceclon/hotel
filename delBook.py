import sqlite3

def delbooking(delet):

    try:
        conn = sqlite3.connect('hostel.db')
        cur = conn.cursor()
        cur.execute('''
            DELETE FROM booking WHERE id_booking='{}';
        '''.format(int(delet)))
        conn.commit()
    except:
        pass
    finally:
        conn.close()