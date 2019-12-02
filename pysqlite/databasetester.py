import sqlite3
from sqlite3 import Error
import random
import string
from faker import Faker
from pydbgen import pydbgen




conn = sqlite3.connect('Zillow.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS Houses(id integer, stateid, price integer)')



def clear_column():
    c.execute("UPDATE Users SET id = null")

def insert_values():
    name = random_name()
    for i in range(2):
        #c.execute("INSERT INTO UserTest(name) VALUES (?)", ([random_name()]))
        c.execute("INSERT INTO UserTest(username, name, email) VALUES (?, ?, ?)", ([random_string(12), random_name(), random_email()]))
    conn.commit()


def random_date():
    fake2 = pydbgen.pydb()
    testing = fake2.realistic_email()


def random_string(length=12):
    characters = string.ascii_letters
    return ''.join(random.choice(characters) for i in range(length))
#hello
def random_name():
    fake = Faker()
    return (fake.name())

def random_email():
    fake = Faker()
    return (fake.email())




def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


# if __name__ == '__main__':
#     create_connection(r"C:\sqlite\db\pythonsqlite.db")

# create_table()
insert_values()
