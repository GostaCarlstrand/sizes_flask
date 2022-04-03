import random
from abc import ABC
from math import sqrt

from pymongo import MongoClient
from df_handler import get_person_dict

conn_string = "mongodb://root:qwerty@localhost:27017"
client = MongoClient(conn_string)
db = client.sizes
persons = []


def save(data):
    db.insert_one(data.__dict__)


def main():

    # persons = get_person_dict('male')
    # for person in persons:
    #     Person(person).save()







    user = {
        'gender': 'male',
        'Heightin': 180,
        'Weightlbs': 75
    }

    Person(user).add()


if __name__ == "__main__":
    main()
