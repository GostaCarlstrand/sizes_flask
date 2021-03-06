from ml_handler import get_neighbors, sk_knn, decision_tree

sizes_values = {
    'XS': 0,
    'S': 1,
    'M': 2,
    'L': 3,
    'XL': 4,
    'XXL': 5
}


class CM:
    XS = (0, 81)
    S = (86, 91)
    M = (97, 102)
    L = (107, 112)
    XL = (116, 122)
    XXL = (122, 150)


class WM:
    XS = (0, 76)
    S = (76, 81)
    M = (81, 84)
    L = (84, 87)
    XL = (87, 97)
    XXL = (97, 120)


class CF:
    XS = (0, 76)
    S = (76, 81)
    M = (81, 86)
    L = (91, 98)
    XL = (98, 107)
    XXL = (107, 150)


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
    return person_size, max_size_value, swim_size


class Person:

    def __init__(self, data):
        self.chest_c = data['chest_c']
        self.waist_c = data['waist_c']
        self.gender = data['gender']
        self.size, self.size_value, self.swim_size = size(self.chest_c, self.waist_c, self.gender)
        self.height = data['height']
        self.weight = data['weight']


def calculate_person_size(height, weight, persons, gender, model):
    test_row = [height, weight]
    if model == 'knn_euclidean':
        neighbors = get_neighbors(persons, test_row, 3)

    if model == 'dec_tree':
        #person = [chest_c, waist_c, gender, height, weight]
        #    decision_tree(person)
        pass
    if model == 'knn_sklearn':
        # Using sklearn knn algorithm
        nr_neighbors = 3
        index = sk_knn(test_row, persons, nr_neighbors) #Tuple with indices to nn
        neighbors = []
        for i in range(len(index)):
            neighbors.append(persons[index[i]])

    chest_c, waist_c, size_v = calculate_person_data(neighbors) #Contains tuple of chest_c, waist_c and size_value
    return round(chest_c, 2), round(waist_c, 2), size_v, values_sizes[size_v]


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