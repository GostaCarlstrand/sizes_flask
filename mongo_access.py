import random
from abc import ABC
from pymongo import MongoClient
from df_handler import get_person_df

conn_string = "mongodb://root:qwerty@localhost:27017"
client = MongoClient(conn_string)
db = client.sizes

sizes_values = {
        'XS': 0,
        'S': 1,
        'M': 2,
        'L': 3,
        'XL': 4,
        'XXL': 5
    }


class CM:
        XS = (0, 90)
        S = (91, 96)
        M = (96, 101)
        L = (101, 106)
        XL = (106, 111)
        XXL = (111, 150)
class WM:
        XS = (0, 78)
        S = (79, 84)
        M = (84, 89)
        L = (89, 94)
        XL = (94, 99)
        XXL = (99, 120)
class CF:
        XS = (81, 85)
        S = (85, 89)
        M = (89, 94)
        L = (94, 99)
        XL = (99, 104)
        XXL = (104, 150)
class WF:
        XS = (63, 68)
        S = (68, 73)
        M = (73, 78)
        L = (78, 83)
        XL = (83, 88)
        XXL = (88, 120)


def chest_size_value(chest_c, waist_c, gender, **kwargs):
    # CM and CF - ChestMale, ChestFemale
    # WM and WF - WaistMale, WaistFemale
    # g_class - gender class
    if gender == 'Male' and kwargs['chest']:
        g_class = CM
        body_c = chest_c
    elif gender == 'Male':
        g_class = WM
        body_c = waist_c
    if gender == 'Female' and kwargs['chest']:
        g_class = CF
        body_c = chest_c
    elif gender == 'Female':
        g_class = WF
        body_c = waist_c

    if body_c > (max(g_class.M)):
        if body_c > (max(g_class.XL)):
            return sizes_values['XXL']
        elif body_c < (min(g_class.XL)):
            return sizes_values['L']
        else:
            return sizes_values['XL']
    elif body_c > (max(g_class.S)):
        return sizes_values['M']
    elif body_c < (min(g_class.S)):
        return sizes_values['XS']
    else:
        return sizes_values['S']
values_sizes = {
    0: 'XS',
    1: 'S',
    2: 'M',
    3: 'L',
    4: 'XL',
    5: 'XXL'
}


def size(chest_c, waist_c, gender):
    chest_size_c_value = chest_size_value(chest_c, waist_c, gender, chest=True)
    chest_size_w_value = chest_size_value(chest_c, waist_c, gender, chest=False)
    max_size_value = max(chest_size_w_value, chest_size_c_value)
    person_size = values_sizes[max_size_value]
    return person_size, max_size_value


class Person:
    def __init__(self, chest_c, waist_c, gender, height, weight):
        self.chest_c = chest_c
        self.waist_c = waist_c
        self.gender = gender
        self.size, self.size_value = size(chest_c, waist_c, gender)
        self.height = height
        self.weight = weight

    # def __init__(self, data):
    #     self.chest_c = data['chest_c']
    #     self.waist_c = data['waist_c']
    #     self.gender = data['gender']
    #     self.size, self.size_value = size(self.chest_c, self.waist_c, self.gender)
    #     self.height = data['height']
    #     self.weight = data['weight']

    collection = db.users

    def save(self):
        self.collection.insert_one(self.__dict__)



def main():

    persons_df = get_person_df('male')
    persons_df = persons_df.reset_index()  # make sure indexes pair with number of rows
    for index, row in persons_df.iterrows():
        Person(row['chestcircumference'], row['waistcircumference'], row['Gender'], row['Heightin'],
                       row['Weightlbs']).save()





if __name__ == "__main__":
    main()
