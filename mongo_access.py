import csv

from pymongo import MongoClient

from person_handler import Person, calculate_person_size

conn_string = "mongodb://root:qwerty@localhost:27017"
client = MongoClient(conn_string)
db = client["mydb"]
db_col = db['persons']


def save(person):
    db_col.insert_one(person)


def get_latest_persons(amount):
    persons = db_col.find().sort('_id', -1)
    latest_persons = []
    for i in range(amount):
        latest_persons.append(persons[i])
    return latest_persons


def save_persons_to_csv():
    males = get_persons('Male')
    females = get_persons('Female')
    fields = [
        'chest_c',
        'waist_c',
        'gender',
        'size',
        'size_value',
        'height',
        'weight'
    ]
    persons = []
    def list_by_gender(gender):
        for sex in gender:
            person_data = []
            person_data.append(sex['chest_c'])
            person_data.append(sex['waist_c'])
            person_data.append(sex['gender'])
            person_data.append(sex['size'])
            person_data.append(sex['size_value'])
            person_data.append(sex['height'])
            person_data.append(sex['weight'])
            persons.append(person_data)

    list_by_gender(males)
    list_by_gender(females)
    with open('persons_csv.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(persons)


def get_persons(gender):
    persons_gender = []
    for person in db_col.find():
        if gender in person['gender']:
            persons_gender.append(person)
    return persons_gender


def init_db():
    from df_handler import get_person_dict
    persons = get_person_dict('female')
    for person in persons:
        person = Person(person)
        save(person.__dict__)
    

def add(height, weight, gender):
    persons = get_persons(gender)
    chest_c, waist_c, size_v, size = calculate_person_size(height, weight, persons, gender)
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
    # # get_latest_persons(10)



if __name__ == "__main__":
    main()

