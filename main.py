import pandas as pd
from math import sqrt

org_df = pd.read_csv('./org_csv/male.csv')
col_chest = org_df.head(50)['chestcircumference'] / 10
col_waist = org_df.head(50)['waistcircumference'] / 10
col_weight = org_df.head(50)['Weightlbs'] * 0.45359237
col_height = org_df.head(50)['Heightin'] * 2.54
col_gender = org_df.head(50)['Gender']
new_df = pd.concat([col_chest, col_waist, col_gender, col_height, col_weight], axis=1)
new_df.rename(columns={'Weightlbs': 'WeightKg', 'Heightin': 'HeightCm'}, inplace=True)
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



h_w_df = pd.concat([col_height, col_weight], axis=1)
h_w_df.rename(columns={'Weightlbs': 'WeightKg', 'Heightin': 'HeightCm'}, inplace=True)
df = new_df.reset_index()  # make sure indexes pair with number of rows
persons = []
for index, row in new_df.iterrows():
    persons.append(
        Person(row['chestcircumference'], row['waistcircumference'], row['Gender'], row['HeightCm'], row['WeightKg']))

#h_w_df.plot(x='WeightKg', y='HeightCm', kind='scatter')


# calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1)):
        distance += (row1[i] - row2[i])**2
    return sqrt(distance)


def get_neighbors(train, test_row, num_neighbors):
    dis_values = list()
    for train_row in train:
        dis = euclidean_distance(test_row, train_row)
        dis_values.append((train_row, dis))


    dis_values.sort(key=lambda tup: tup[1])
    list_neighbors = list()
    for i in range(num_neighbors):
        list_neighbors.append(dis_values[i][0])
    return list_neighbors


df_list = h_w_df.values.tolist()        #Dataframe to list

height = float(input("Enter height"))
weight = float(input("Enter weight"))

_ = [height, weight]
temp_person_df = pd.DataFrame({'HeightCm': [height],
                    'WeightKg' : [weight]})
h_w_df = pd.concat([h_w_df, temp_person_df], axis=0, ignore_index=True)


neighbors = get_neighbors(df_list, _, 3)

neighbors_persons = []      #List to fill neighbors as person objects
for neighbor in neighbors:
    for person in persons:
        if all(x in [person.height, person.weight] for x in [neighbor[0], neighbor[1]]):
            neighbors_persons.append(person)


def return_size():
    person_size_v = 0
    for person in neighbors_persons:
        person_size_v += person.size_value
    person_size_v /= len(neighbors_persons)     #Get the average size value
    print(values_sizes[round(person_size_v)])


return_size()