from math import sqrt

from sklearn.neighbors import NearestNeighbors
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


def get_multi_array(samples):
    sample_array = []
    for person in samples:
        col = [person['height'], person['weight']]
        sample_array.append(col)
    return sample_array


def sk_knn(test_row, samples, nr_neighbors):
    neigh = NearestNeighbors(n_neighbors=nr_neighbors, radius=1)
    sample_array = get_multi_array(samples)
    neigh.fit(sample_array)
    index = neigh.kneighbors([test_row], nr_neighbors, return_distance=False)
    list_with_indices = []
    for i in range(nr_neighbors):
        list_with_indices.append(index[0][i])
    return list_with_indices


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


def decision_tree(person):
    df = pd.read_csv('persons_csv.csv')
    df.loc[df['gender'] == 'Male', 'gender'] = 1    # Change from string to numeric value
    df.loc[df['gender'] == 'Female', 'gender'] = 0
    X = df.drop(['size_value', 'size'], axis=1).copy()  # New df without size or size value column
    y = df.size_value.copy()  # y column contains only the size_value series
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.33)
    clf_dt_pruned = DecisionTreeClassifier(random_state=42, ccp_alpha=0.015311, max_depth=10)
    clf_dt_pruned = clf_dt_pruned.fit(X_train, y_train)
    if isinstance(person.gender, str):
        if person.gender == 'Male':
            person.gender = 1
        else:
            person.gender = 0
    size_result = clf_dt_pruned.predict([person])
    return size_result


"""
Egen implementerad knn och sklearn knn genererar samma grannar och resulterar därför också i samma storlek mot en ny kandidat.
Decision tree har inte alltid resulterat i samma storlek som de andra algoritmerna. Detta skulle kunna t ex bero på
1. Jag har valt att retunera genomsnittet på storlekarna från de grannar som algoritmen hittar. En granne som skiljer kraftigt kan då påverka resultatet rejält. 
2. Knn har endast fått resultera i tre stycken grannar. Hade man valt att ta flera skulle detta kunna ge ett mer rättvist resultat.  
"""