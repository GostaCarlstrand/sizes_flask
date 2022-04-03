import json

from pymongo import MongoClient
from df_handler import get_person_dict
from person_handler import Person, calculate_person_size

conn_string = "mongodb://root:qwerty@localhost:27017"
client = MongoClient(conn_string)
db = client["mydb"]
db_col = db['persons']


def save(person):
    person = person.__dict__
    db_col.insert_one(person)


def get_persons(gender):
    persons_gender = []
    for person in db_col.find():
        if gender in person['gender']:
            persons_gender.append(person)
    return persons_gender


def init_db():
    persons = get_person_dict('male')
    for person in persons:
        person = Person(person)
        save(person)
    

def add(height, weight, gender):
    persons = get_persons(gender)
    height, weight, size = calculate_person_size(height, weight, persons)


def main():

    height = float(input('Enter height'))
    weight = float(input('Enter weight'))
    gender = input('Enter gender')

    add(height, weight, gender)

    

if __name__ == "__main__":
    main()

