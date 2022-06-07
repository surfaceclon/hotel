import sqlite3


number_all = []
number = []
def showroom():
    number_all.clear()
    number.clear()
    try:
        conn = sqlite3.connect('hostel.db')
        cur = conn.cursor()
        cur.execute('''
            SELECT number FROM list_of_numbers;
        ''')
        for numbers in cur.fetchall():
            for _ in numbers:
                number_all.append(_)
        cur.execute('''
            SELECT number FROM list_of_numbers WHERE number NOT IN(SELECT number FROM booking);
        ''')
        for numbers in cur.fetchall():
            for _ in numbers:
                number.append(_)
    except:
        pass
    finally:
        conn.close()
showroom()