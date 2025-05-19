from matplotlib import pyplot as plt

x1 = [1.34, 1.16, 1.54, 0.46, 1.8, 1.86, 0.7, 0.52, 1.24, 1.32]
y1 = [1.8, 1.33, 1.37, 1.71, 0.68, 0.29, 1.3, 0.25, 1.07, 0.25]
x2 = [5.0, 5.88, 3.69, 2.61, 4.66, 2.09, 4.82]
y2 = [0.14, 0.61, 4.37, 1.74, 3.3, 2.98, 4.25]

points_class1 = [(x1[i], y1[i], 'c1') for i in range(len(x1))]
points_class2 = [(x2[i], y2[i], 'c2') for i in range(len(x2))]

features_num = 2

labels = ['c1', 'c2']

def euclidean_dinstance(points, new_point):
    distances = []

    for point in points:
        point_distance = 0

        for i in range(features_num):
            point_distance += (new_point[i] - point[i]) ** 2

        distances.append((point_distance, point[2]))  # расстояние до точки и ее класс

    return distances


def get_min_item(distances):  # найти минимальный элемент
    min_dist, min_item_idx, min_item_label = 1000000, 0, 'c1'