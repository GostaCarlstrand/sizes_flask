from math import sqrt

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
    # def __init__(self, chest_c, waist_c, gender, height, weight):
    #     self.chest_c = chest_c
    #     self.waist_c = waist_c
    #     self.gender = gender
    #     self.size, self.size_value = size(chest_c, waist_c, gender)
    #     self.height = height
    #     self.weight = weight

    def __init__(self, data):
        self.chest_c = data['chest_c']
        self.waist_c = data['waist_c']
        self.gender = data['Gender']
        self.size, self.size_value = size(self.chest_c, self.waist_c, self.gender)
        self.height = data['HeightCm']
        self.weight = data['WeightKg']


def calculate_person_size(height, weight, persons):
    # persons = list from database that contains persons with same gender
    test_row = [height, weight]
    neighbors = get_neighbors(persons, test_row, 3)
    chest_c, waist_c, size_v = calculate_person_data(neighbors) #Contains tuple of chest_c, waist_c and size_value
    return chest_c, waist_c, size_v, values_sizes[size_v]

    #values_sizes[round(person_size_v)]


def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(1):
        distance += (row1[0] - row2['height']) ** 2
        distance += (row1[1] - row2['weight']) ** 2
    return sqrt(distance)


def get_neighbors(train, test_row, num_neighbors):
    """test_row - contains height, weight from new person
    train - list of all persons in database
     """
    dis_values = list()
    for train_row in train:
        dis = euclidean_distance(test_row, train_row)
        dis_values.append((train_row, dis))
    print()
    dis_values.sort(key=lambda tup: tup[1])
    list_neighbors = list()
    for i in range(num_neighbors):
        list_neighbors.append(dis_values[i][0])

    # neighbors_persons = []  # List to fill neighbors as person objects
    # for neighbor in list_neighbors:
    #     for person in train:
    #         if all(x in [person.height, person.weight] for x in [neighbor[0], neighbor[1]]):
    #             neighbors_persons.append(person)

    return list_neighbors


def calculate_person_data(neighbors_persons):
    person_size_v = 0
    chest_c = 0
    waist_c = 0
    for person in neighbors_persons:
        person_size_v += person['size_value']
        chest_c += person['chest_c']
        waist_c += person['waist_c']

    # Get the average size value

    chest_c /= len(neighbors_persons)
    waist_c /= len(neighbors_persons)
    person_size_v /= len(neighbors_persons)
    return chest_c, waist_c, round(person_size_v)




