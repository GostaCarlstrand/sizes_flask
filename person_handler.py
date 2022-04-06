
sizes_values = {
    'XS': 0,
    'S': 1,
    'M': 2,
    'L': 3,
    'XL': 4,
    'XXL': 5
}


# class CM:
#     XS = (0, 90)
#     S = (91, 96)
#     M = (96, 101)
#     L = (101, 106)
#     XL = (106, 111)
#     XXL = (111, 150)

class CM:
    XS = (0, 81)
    S = (86, 91)
    M = (97, 102)
    L = (107, 112)
    XL = (116, 122)
    XXL = (122, 150)


# class WM:
#     XS = (0, 78)
#     S = (79, 84)
#     M = (84, 89)
#     L = (89, 94)
#     XL = (94, 99)
#     XXL = (99, 120)
class WM:
    XS = (0, 76)
    S = (76, 81)
    M = (81, 84)
    L = (84, 87)
    XL = (87, 97)
    XXL = (97, 120)

# class CF:
#     XS = (81, 85)
#     S = (85, 89)
#     M = (89, 94)
#     L = (94, 99)
#     XL = (99, 104)
#     XXL = (104, 150)
class CF:
    XS = (0, 76)
    S = (76, 81)
    M = (81, 86)
    L = (91, 98)
    XL = (98, 107)
    XXL = (107, 150)


# class WF:
#     XS = (63, 68)
#     S = (68, 73)
#     M = (73, 78)
#     L = (78, 83)
#     XL = (83, 88)
#     XXL = (88, 120)
class WF:
    XS = (0, 64)
    S = (64, 68)
    M = (68, 75)
    L = (75, 82)
    XL = (82, 91)
    XXL = (91, 120)

# Hips male for swimming
class HM:
    XS = (0, 88)
    S = (88, 96)
    M = (96, 104)
    L = (104, 112)
    XL = (112, 120)
    XXL = (120, 128)


# Hips female for swimming
class HF:
    XS = (84, 91)
    S = (91, 98)
    M = (98, 105)
    L = (105, 112)
    XL = (112, 120)
    XXL = (120, 150)


# Bust female for swimming
class BF:
    XS = (76, 83)
    S = (83, 90)
    M = (90, 97)
    L = (97, 104)
    XL = (104, 114)
    XXL = (114, 130)


def swimming_size_value(*args):
    # g_class = gender class
    size_v = 0
    rounds = 1
    g_class = HM
    if args[2] == 'Female':
        rounds = 2
        g_class = HF

    for i in range(rounds):
        swim_measurements = args[i]
        if i == 1:
            g_class = BF

        if swim_measurements > (max(g_class.M)):
            if swim_measurements > (max(g_class.XL)):
                size_v += sizes_values['XXL']
            elif swim_measurements < (min(g_class.XL)):
                size_v += sizes_values['L']
            else:
                size_v += sizes_values['XL']
        elif swim_measurements > (max(g_class.S)):
            size_v += sizes_values['M']
        elif swim_measurements < (min(g_class.S)):
            size_v += sizes_values['XS']
        else:
            size_v += sizes_values['S']
    return round(size_v/rounds)


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

    swim_size = swimming_size_value(waist_c, chest_c, gender)
    swim_size = values_sizes[swim_size]

    max_size_value = max(chest_size_w_value, chest_size_c_value)
    person_size = values_sizes[max_size_value]
    #      xs, s, m     size as value   swim xs, s, m
    return person_size, max_size_value, swim_size


class Person:

    def __init__(self, data):
        self.chest_c = data['chest_c']
        self.waist_c = data['waist_c']
        self.gender = data['gender']
        self.size, self.size_value, self.swim_size = size(self.chest_c, self.waist_c, self.gender)
        self.height = data['height']
        self.weight = data['weight']


def calculate_person_size(height, weight, persons):
    test_row = [height, weight]
    neighbors = get_neighbors(persons, test_row, 3)
    chest_c, waist_c, size_v = calculate_person_data(neighbors) #Contains tuple of chest_c, waist_c and size_value
    return round(chest_c, 2), round(waist_c, 2), size_v, values_sizes[size_v]


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
    dis_values.sort(key=lambda tup: tup[1])
    list_neighbors = list()
    for i in range(num_neighbors):
        list_neighbors.append(dis_values[i][0])

    return list_neighbors


def calculate_person_data(neighbors_persons):
    person_size_v = 0
    chest_c = 0
    waist_c = 0
    for person in neighbors_persons:
        person_size_v += person['size_value']
        chest_c += person['chest_c']
        waist_c += person['waist_c']

    chest_c /= len(neighbors_persons)
    waist_c /= len(neighbors_persons)
    person_size_v /= len(neighbors_persons)
    return chest_c, waist_c, round(person_size_v)

