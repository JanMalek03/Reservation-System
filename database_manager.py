import sqlite3
import json
import datetime

DATABASE = "reservation.db"


def connect_db():
    return sqlite3.connect(DATABASE)


def init_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS reservations 
                      (date TEXT, start_time TEXT, end_time TEXT)''')
    conn.commit()
    conn.close()


def convert_date_to_db_format(date):
    return datetime.datetime.strptime(date, "%d.%m.%Y").strftime("%Y.%m.%d")


def convert_date_from_db_format(date):
    return datetime.datetime.strptime(date, "%Y.%m.%d").strftime("%d.%m.%Y")


def is_reservation_possible(date, start_time, end_time):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM reservations WHERE date = ? AND 
                      (start_time < ? AND end_time > ?) OR 
                      (start_time < ? AND end_time > ?)''', 
                   (date, end_time, start_time, start_time, end_time))
    conflicts = cursor.fetchall()
    conn.close()

    return len(conflicts) == 0


def data_to_string(data):
    if not data:
        return ""

    return ';'.join([','.join(map(str, item)) for item in data])


def make_reservation(data):
    if not data:
        return "ERROR"

    data = json.loads(data)

    date = convert_date_to_db_format(data['date'])
    start_time = data['start_time']
    end_time = data['end_time']

    if not is_reservation_possible(date, start_time, end_time):
        return "TAKEN"

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO reservations (date, start_time, end_time)
                        VALUES (?, ?, ?)''', (date, start_time, end_time))
    conn.commit()
    conn.close()

    return "SUCCESS"


def get_reservations_for_date(date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''SELECT start_time, end_time 
                      FROM reservations
                      WHERE date = ?
                      ORDER BY start_time''', (date, ))
    reservations = cursor.fetchall()
    conn.close()

    data = [(convert_date_from_db_format(r[0]), r[1], r[2]) for r in reservations]
    return data_to_string(data)


def get_all_reservations():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''SELECT date, start_time, end_time
                      FROM reservations
                      ORDER BY date, start_time''')
    reservations = cursor.fetchall()
    conn.close()

    data = [(convert_date_from_db_format(r[0]), r[1], r[2]) for r in reservations]
    return data_to_string(data)


def delete_past_reservations():
    current_date = datetime.datetime.now().strftime("%d.%m.%Y")
    current_date = convert_date_to_db_format(current_date)

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''DELETE
                      FROM reservations
                      WHERE date < ?''', (current_date, ))
    conn.commit()
    conn.close()
