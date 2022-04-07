from math import sqrt
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.linear_model import LinearRegression


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


def linearRegr(chest_c, waist_c, samples):
    sample_array = get_multi_array(samples)
    X = np.array(sample_array)
    # y = 1 * x_0 + 2 * x_1 + 3
    y = np.dot(X, np.array([chest_c, waist_c]))
    reg = LinearRegression().fit(X, y)
    reg.score(X, y)
    reg.coef_
    reg.intercept_
    reg.predict(np.array([[3, 5]]))