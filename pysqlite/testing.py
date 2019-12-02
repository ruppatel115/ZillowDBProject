from faker import Faker
import random, datetime, time

fake=Faker()


def randomshit():
    for i in range(10):
        print(fake.name())

def random_date(seed):
    random.seed(seed)
    d = random.randint(1, int(time.time()))
    return datetime.fromtimestamp(d).strftime('%Y-%m-%d')

randomshit('2000-13-42')