from math import sqrt
import random
from matplotlib import pyplot as plt
import numpy as np


def calculate_distance(a, b):
    """
    given two points a and b, calculate the euclidean distance between a and b
    """

    dimensions = len(a)  # getting the dimensions. Excepting the dimensions of a and b are the same
    dist_sum = 0  # sum is to save the calculation result
    for d in range(dimensions):
        dist_sum += (a[d] - b[d]) ** 2
    return sqrt(dist_sum)


def find_closest_cluster(data_centers, data_set):
    """
    assign data points to the closest centers
    """
    data_cluster = []
    for data in data_set:
        shortest_distance = -1
        shortest_distance_index = 0
        for i in range(len(data_centers)):
            dist = calculate_distance(data_centers[i], data)
            if shortest_distance == -1:
                shortest_distance_index = i
                shortest_distance = dist
            elif shortest_distance > dist:
                shortest_distance_index = i
                shortest_distance = dist
        data_cluster.append(shortest_distance_index)
    return data_cluster


def generate_new_centers(data_set, data_cluster):
    """
    generate new centers based on the data point assignment
    """
    cluster_set = {}
    for c, data in zip(data_cluster, data_set):
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


def k_means(data_set, k_value):
    """
    k means algorithm
    """

    data_centers = initialize_k_centers(data_set, k_value)        # randomly select k points
    clusters = find_closest_cluster(data_centers, data_set)
    prev_clusters = None
    while clusters != prev_clusters:
        data_centers = generate_new_centers(data_set, clusters)
        prev_clusters = clusters
        clusters = find_closest_cluster(data_centers, data_set)
    return data_centers, clusters


def get_largest_radius(data_centers, clusters, data_set):
    """
    used to get the largest radius in order to draw circles around centers. Temporarily not usable
    """

    radius = [0] * len(data_centers)
    for i in range(len(data_set)):
        dist = calculate_distance(data_set[i], data_centers[clusters[i]])
        if dist > radius[clusters[i]]:
            radius[clusters[i]] = dist
    return radius


def cal_silhouette_coefficient(data_set, assignments):
    """
    calculate the silhouette coefficient for K-Means
    """
    final_clusters = dict()    # {centers: clusters_points}
    s_i_list = list()

    '''build a dictionary{centers: points}'''
    for point, assignment in zip(data_set, assignments):
        final_clusters.setdefault(assignment, list()).append(point)

    '''Go though all the centers'''
    for center in final_clusters.keys():

        '''go though each point in current center '''
        for i in final_clusters[center]:
            # get average distance between point i and all the other data points in the cluster to which point i belongs
            sum_avg_dist_center = sum(calculate_distance(i, p) for p in final_clusters[center])
            a_i = sum_avg_dist_center / float(len(final_clusters[center])-1)

            # get the minimum average distance from𝑖to all clusters to which point i does not belong.
            sum_avg_dist_else_center_list = list()
            for else_center in final_clusters.keys():
                if else_center != center:
                    sum_avg_dist_else_center = sum(calculate_distance(i, p) for p in final_clusters[else_center])
                    num_points_else_center_cluster = float(len(final_clusters[else_center]))
                    sum_avg_dist_else_center = sum_avg_dist_else_center / num_points_else_center_cluster
                    sum_avg_dist_else_center_list.append(sum_avg_dist_else_center)
            b_i = min(sum_avg_dist_else_center_list) if sum_avg_dist_else_center_list else float("inf")

            # calculate silhouette coefficient for this point and append to list
            s_i = (b_i - a_i) / max(a_i, b_i)
            s_i_list.append(s_i)

    # calculate the mean value of the silhouette coefficients
    sc = sum(s_i_list) / len(s_i_list)
    return sc


def draw_graph(data_points, data_centers, data_cluster):
    """
        draw centers
        centers: the centers of clusters
    """

    plt.figure(2)
    color = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 'dodgerblue',
             'greenyellow', 'teal', 'violet', 'lightskyblue', 'black', 'tan']
    data = np.array(data_points)
    x, y = data.T
    res_color = map(lambda x: color[x], data_cluster)
    list_res_color = list(res_color)
    plt.scatter(x, y, color=list_res_color)

    centers_data = np.array(data_centers)
    centers_x, centers_y = centers_data.T
    plt.scatter(centers_x, centers_y)
    '''
        draw points from data set
    '''
    # figure, axes = plt.subplots()
    # data = np.array(points)
    # x, y = data.T
    # plt.scatter(x, y)

    '''
    # This is for draw circles around the centers, but there are some problems with the way i calculate the radius
    # Temporarily comment out this feature
    radius = get_largest_radius(centers, cluster, points)
    for r, center in zip(radius, centers):
        cir = plt.Circle(center, r, color='r', fill=False)
        axes.add_artist(cir)
    '''


def read_file(filename):
    """
        read points from file
    """

    # fake data used to test
    # points = [[1, 2],[2, 1],[3, 1],[5, 4],[5, 5],[6, 5],[10, 8],[7, 9],[11, 5],[14, 9],[14, 14],]
    data_points = list()
    with open(filename) as f:
        for line in f:
            splits = line.strip().split(',')
            # print(splits)
            data_points.append([int(splits[0]), int(splits[1])])
    return data_points


def initialize_k_centers(data_points, k_value):
    """
    use kmeans++ to find all the initial centers
    """
    init_centers = list()
    init_point = random.sample(data_points, 1)
    init_centers.append(init_point[0])
    for i in range(k_value - 1):
        max_dist, temp_next_center = -1, init_centers[-1]
        for point in data_points:
            if point not in init_centers:
                dist = calculate_distance(point, init_centers[-1])
                if dist > max_dist:
                    max_dist = dist
                    temp_next_center = point
        init_centers.append(temp_next_center)
    return init_centers


def initialize_random_k_centers(data_points, k_value):
    """
    randomly pick k centers as the initial centers
    """
    return random.sample(data_points, k_value)


def calculate_best_fit_k(data_points, min_k, max_k):
    """
    compare the silhouette coefficients for k values range from min_k to max_k and return the one with highest value
    """
    si_co = list()  # silhouette coefficient ranges from -1 to 1
    for k_value in range(min_k, max_k):
        data_centers, data_cluster = k_means(data_points, k_value)
        si_co.append(cal_silhouette_coefficient(points, data_cluster))
    max_si_co = max(si_co)
    plt.figure(1)
    plt.plot(list(range(min_k, max_k)), si_co)
    return max_si_co, min_k + si_co.index(max_si_co)


if __name__ == "__main__":
    # figure, axes = plt.subplots()
    cal_sc, k = True, 8  # when cal_sc = True, the program will use silhouette analysis to find the best k value first
    points = read_file('mapreduceUserBehavior_100k.txt')
    if cal_sc:
        silhouette_coefficient, k = calculate_best_fit_k(points, 2, 12)
        print(silhouette_coefficient)
    centers, cluster = k_means(points, k)
    draw_graph(points, centers, cluster)
    plt.show()


