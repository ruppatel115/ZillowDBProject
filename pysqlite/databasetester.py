import sqlite3
from sqlite3 import Error
import random
import string
from faker import Faker
import time
from pydbgen import pydbgen
from random import randrange, choice
from datetime import timedelta, datetime
import secrets
import string







conn = sqlite3.connect('/Users/ruppatel/DatagripProjects/ZillowDB/pysqlite/Zillow.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS Houses(id integer, stateid, price integer)')



def clear_column():
    c.execute("UPDATE Users SET id = null")

def insert_values():
    name = random_name()
    answer = choice(['yes','no'])
    for i in range(101004):
        d1 = datetime.strptime('1/1/2000', '%m/%d/%Y')
        d2 = datetime.strptime('12/1/2019', '%m/%d/%Y')


        c.execute("INSERT INTO Agents(specialtyid, Name, Location, stateid) VALUES (?, ?, ?,?)", ([random.randint(1,5), random_name(), random_city(), random.randint(1,50)]))
        c.execute("INSERT INTO AgentReviews(comments, userid, agentid) VALUES (?, ?, ?)", ([random_comment(), random.randint(1, 101004), random.randint(1,100000)]))
        c.execute("INSERT INTO House(price, ForTypeid, bedrooms, SquareFeet, HomeTypeid, dateAdded, Address) VALUES (?, ?, ?, ?, ?, ?,?)", ([random.randint(25000,100000000), random.randint(1,3), random.randint(1,10), random.randint(1000, 100000), random.randint(1,5), random_date(d1,d2), random_address() ]))
        c.execute("INSERT INTO Users(username, name, email, datejoined, password) VALUES (?, ?, ?,?,?)", ([random_string(12), random_name(), random_email(), random_date(d1,d2), random_password()]))
        c.execute("Insert into Listings(Houseid, agentid) VALUES (?,?)", ([random.randint(1, 100000), random.randint(1,100000)]))
        c.execute("INSERT INTO SavedHouses(userid, houseid)  VALUES (?, ?)", ([random.randint(1,10402), (random.randint(1,10402))]))
        c.execute("INSERT INTO Mortgages(stateid, TypeRateid, LoanTypeid,LoanAmount, DownPayment, CreditScore, Veteran, userid, rateAmount) VALUES (?, ?, ?, ?, ?, ?, ?,?,?)", ([random.randint(1,50), random.randint(1,2), random.randint(1,5), random.randint(1,1000000), random.randint(1000, 50000), random.randint(300,850), answer, random.randint(1,115512), random.uniform(1.0,12.0)]))


    conn.commit()


def random_password():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(20))
    return(password)

def random_comment():
    fake = Faker()

    sentence = [
        'great', 'professional', 'smart', 'helped', 'find', 'a',
        'home', 'really', 'cares','about', 'finding', 'beautiful',
        'late', 'patient', 'with', 'us', 'in', 'the', 'process', 'maintained', 'lowkey'
    ]
    return fake.sentence()

def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def random_address():
    fake=Faker()
    return fake.address()

def random_city():
    my_db = pydbgen.pydb()
    return (my_db.city_real())

def random_string(length=15):
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

