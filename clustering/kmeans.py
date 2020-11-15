from math import sqrt
import random


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
    for c, data in (cluster, data_set):
        if not cluster_set.has_key(c):
            cluster_set[c] = []
        cluster_set[c].append(data)

    new_centers = []
    for c in cluster_set:
        dimensions = len(c[0])
        new_center = []
        for d in range(dimensions):
            d_sum = 0
            for point in c:
                d_sum += point[d]
            new_center.append(d_sum / float(len(c)))
        new_centers.append(new_center)
    return new_centers


def k_means(data_set, k):
    centers = random.sample(data_set, k)        # randomly select k points
    clusters = find_closest_cluster(centers, data_set)
    prev_clusters = None
    while clusters != prev_clusters:
        centers = generate_new_centers(data_set, clusters)
        prev_clusters = clusters
        clusters = find_closest_cluster(centers, data_set)
    return centers, clusters
