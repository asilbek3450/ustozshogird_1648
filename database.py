import sqlite3

conn = sqlite3.Connection('month5/ustoz_shogird/ustoz_shogird.db')
cur = conn.cursor()

def create_table(dp):
    query = """CREATE TABLE IF NOT EXISTS HodimKerak(
user_id INT,
username VARCHAR(50),
idora VARCHAR(50),
texnologiya VARCHAR(50),
telefon VARCHAR(50),
hudud VARCHAR(50),
ism_familiya VARCHAR(50),
murojaat_vaqti VARCHAR(50),
ish_vaqti VARCHAR(50),
maosh INT,
qoshimcha TEXT
);"""
    cur.execute(query)
    conn.commit()


def insert_data(data):
    query = """INSERT INTO HodimKerak(user_id, username, idora, texnologiya, telefon, hudud, ism_familiya, murojaat_vaqti, ish_vaqti, maosh, qoshimcha)
            VALUES
            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            """
    cur.execute(query, data)
    conn.commit()


def select_data():
    query = """SELECT * FROM HodimKerak;"""
    cur.execute(query)
    return cur.fetchall()


def select_data_by_id(user_id):
    query = f"""SELECT * FROM HodimKerak WHERE user_id={user_id};"""
    cur.execute(query)
    return cur.fetchall()

