import sqlite3

from faker import Faker


def create_customers():
    con = sqlite3.connect("flask_sql.db")
    cur = con.cursor()
    create_table_customers = """
    CREATE TABLE IF NOT EXISTS customers (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        gender VARCHAR(255),
        phone_number VARCHAR(255)
        )
    """
    cur.execute(create_table_customers)

    fake = Faker()
    for _ in range(100):
        gender = fake.random_element(elements=('Male', 'Female'))
        first_name = fake.first_name_male() if gender=="Male"\
        else fake.first_name_female()
        last_name = fake.last_name_male() if gender=="Male"\
        else fake.last_name_female()
        phone_number = f'+{fake.random_number(digits=12, fix_len=True)}'
        with sqlite3.connect("flask_sql.db") as conn:
            cursor = conn.cursor()
            insert_query = """
                INSERT INTO customers (
                first_name, last_name, gender, phone_number)
                VALUES (?, ?, ?, ?)
                """
            cursor.execute(insert_query, \
                (first_name, last_name, gender, phone_number))
    con.commit()
    con.close()


def create_tracks():
    con = sqlite3.connect("flask_sql.db")
    cur = con.cursor()
    create_table_tracks = """
    CREATE TABLE IF NOT EXISTS tracks (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        artist VARCHAR(255),
        song VARCHAR(255),
        duration INTEGER,
        release_date DATE
        )
    """
    cur.execute(create_table_tracks)

    fake = Faker()
    for _ in range(100):
        artist = fake.name_nonbinary()
        song = fake.sentence(nb_words=5)
        duration = fake.random_int(min=30, max=600)
        release_date = fake.year()
        with sqlite3.connect("flask_sql.db") as conn:
            cursor = conn.cursor()
            insert_query = """
                INSERT INTO tracks (
                artist, song, duration, release_date)
                VALUES (?, ?, ?, ?)
                """
            cursor.execute(insert_query, \
                (artist, song, duration, release_date))
    con.commit()
    con.close()
