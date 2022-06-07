import sqlite3

def deletclient(id_client):

    try:
        conn = sqlite3.connect('hostel.db')
        cur = conn.cursor()
        cur.execute('''
            DELETE FROM list_of_clients WHERE id_client='{}';
        '''.format(int(id_client)))
        conn.commit()
    except:
        pass
    finally:
        conn.close()