import json

from pymongo import MongoClient
from df_handler import get_person_dict
from person_handler import Person, calculate_person_size

conn_string = "mongodb://root:qwerty@localhost:27017"
client = MongoClient(conn_string)
db = client["mydb"]
db_col = db['persons']


def save(person):
    db_col.insert_one(person)


def get_latest_persons():
    persons = db_col.find().sort('_id', -1)
    latest_persons = []
    for i in range(10):
        latest_persons.append(persons[i])
    return latest_persons


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
        save(person.__dict__)
    

def add(height, weight, gender):
    persons = get_persons(gender)
    chest_c, waist_c, size_v, size = calculate_person_size(height, weight, persons)
    person = {
        'chest_c': chest_c,
        'waist_c': waist_c,
        'gender': gender,
        'size': size,
        'size_value': size_v,
        'height': height,
        'weight': weight
    }
    save(person)
    return size


def main():
    height = float(input('Enter height'))
    weight = float(input('Enter weight'))
    gender = input('Enter gender')
    add(height, weight, gender)

    get_latest_persons()


if __name__ == "__main__":
    main()

