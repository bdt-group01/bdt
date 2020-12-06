from math import sqrt
import random
from matplotlib import pyplot as plt
import numpy as np



def calculate_distance(a, b):
    """
    given two points a and b, calculate the distance between a and b
    """

    dimensions = len(a)  # getting the dimensions. Excepting the dimensions of a and b are the same
    sum = 0  # sum is to save the calculation result
    for d in range(dimensions):
        sum += (a[d] - b[d]) ** 2
    return sqrt(sum)


def find_closest_cluster(centers, data_set):
    cluster = []
    for data in data_set:
        shortest_distance = -1
        shortest_distance_index = 0
        for i in range(len(centers)):
            dist = calculate_distance(centers[i], data)
            if shortest_distance == -1:
                shortest_distance_index = i
                shortest_distance = dist
            elif shortest_distance > dist:
                shortest_distance_index = i
                shortest_distance = dist
        cluster.append(shortest_distance_index)
    return cluster


def generate_new_centers(data_set, cluster):
    cluster_set = {}
    for c, data in zip(cluster, data_set):
        if c not in cluster_set:
            cluster_set[c] = []
        cluster_set[c].append(data)

    new_centers = []
    for c in cluster_set.values():
        dimensions = len(c[0])
        new_center = []
        for d in range(dimensions):
            d_sum = 0
            for point in c:
                d_sum += point[d]
            new_center.append(d_sum / float(len(c)))
        new_centers.append(new_center)
    return new_centers

'''
k means algorithm
'''
def k_means(data_set, k):
    centers = random.sample(data_set, k)        # randomly select k points
    #centers = [data_set[0], data_set[1], data_set[2], data_set[3]]
    clusters = find_closest_cluster(centers, data_set)
    prev_clusters = None
    while clusters != prev_clusters:
        centers = generate_new_centers(data_set, clusters)
        prev_clusters = clusters
        clusters = find_closest_cluster(centers, data_set)
    return centers, clusters

'''
used to get the largest radius in order to draw circles around centers. Temporarily not usable
'''
def get_largest_radius(centers, clusters, data_set):
    radius = [0] * len(centers)
    for i in range(len(data_set)):
        dist = calculate_distance(data_set[i], centers[clusters[i]])
        if dist > radius[clusters[i]]:
            radius[clusters[i]] = dist
    return radius

'''
# fake data used to test
points = [
     [1, 2],
     [2, 1],
     [3, 1],
     [5, 4],
     [5, 5],
     [6, 5],
     [10, 8],
     [7, 9],
     [11, 5],
     [14, 9],
     [14, 14],
     ]
'''

'''
read points from file
'''
points = []
with open('mapreduceUserBehavior.txt') as f:
    for line in f:
        splits = line.strip().split(',')
        print(splits)
        points.append([int(splits[0]), int(splits[1])])

'''
draw points from data set
'''
figure, axes = plt.subplots()
data = np.array(points)
x, y = data.T
plt.scatter(x, y)

'''
draw centers
centers: the centers of clusters
'''
centers, cluster = k_means(points, 10)
centers_data = np.array(centers)
centers_x, centers_y = centers_data.T
plt.scatter(centers_x, centers_y)

'''
# This is for draw circles around the centers, but there are some problems with the way i calculate the radius
# Temporarily comment out this feature
radius = get_largest_radius(centers, cluster, points)
for r, center in zip(radius, centers):
    cir = plt.Circle(center, r, color='r', fill=False)
    axes.add_artist(cir)
'''
plt.show()
