'''
Created on Nov 7, 2013
@author: Ambarish Hazarnis
'''

from KMeansCluster import *

def distance_to_test():
    print " Testing Point.distance_to: "
    pt1 = Point(3,5)
    pt2 = Point(5,6)
    assert pt1.distance_to(pt1) == 0  # distance from point to itself should be 0
    assert pt1.distance_to(pt2) == 2.23606797749979


def closest_point_test():
    print " Testing Point.closest_point: "
    pt1 = Point(3,5)
    pt2 = Point(5,6)
    pt3 = Point(10,12)
    assert pt1.closest_point([pt1, pt2]) == 0  # pt1 is closest to itself
    assert pt1.closest_point([pt2, pt3]) == 0  # pt1 is closest to pt2
    assert pt3.closest_point([pt1, pt2]) == 1  # pt3 is closest to pt2

def distance_to_origin_test():
    print " Testing Point.distance_to_origin: "
    pt1 = Point(0,0)
    pt2 = Point(0,1)
    pt3 = Point(1,1)
    assert pt1.distance_to_origin() == 0
    assert pt2.distance_to_origin() == 1
    assert pt3.distance_to_origin() == 1.4142135623730951
    

def initialize_clusters_test():
    print ' Testing initialize_clusters'
    # create a new clustering of 4 data points, using K = 2
    pt1 = Point(3,5)
    pt2 = Point(5,6)
    pt3 = Point(10,12)
    pt4 = Point(11,13)
    kmeans = KMeansCluster(2, [pt1, pt2, pt3, pt4])
    assert isinstance(kmeans.clusters, dict)  # make sure they're using the prescribed datatype
    assert len(kmeans.clusters) == 2  # make sure there are the right number of clusters
    assert all(len(c) > 0 for c in kmeans.clusters.values()) # make sure every cluster has at least one element
    assert sum(len(c) for c in kmeans.clusters.values()) == 4 # make sure every datapoint is used

def initialize_centroids_test():
    print ' Testing initialize_centroids'
    pt1 = Point(3,5)
    pt2 = Point(5,6)
    pt3 = Point(10,12)
    pt4 = Point(11,13)
    pt5 = Point(11,14)
    kmeans = KMeansCluster(2, [pt1, pt2, pt3, pt4, pt5])
    assert len(kmeans.centroids) == 2  # make sure you got the right number of centroids
    assert all(isinstance(c, Point) for c in kmeans.centroids)  # make sure you're using Point's inside
    assert isinstance(kmeans.centroids, list)  # make sure cluster indices are set up properly 

def get_nearest_centroid_for_point_test():
    print ' Testing get_nearest_centroid_for_point'
    pt1 = Point(3,5)
    pt2 = Point(5,6)
    pt3 = Point(10,12)
    pt4 = Point(11,13)
    pt5 = Point(11,14)
    kmeans = KMeansCluster(2, [pt1, pt2, pt3, pt4, pt5])
    kmeans.centroids = [pt1, pt4]
    assert kmeans.get_nearest_centroid_for_point(pt1) == 0  # pt1 should be closest to itself
    assert kmeans.get_nearest_centroid_for_point(pt2) == 0  # pt2 should be closest to pt1
    assert kmeans.get_nearest_centroid_for_point(pt3) == 1  # pt3 should be closest to pt4

def assign_all_data_to_nearest_centroids_test():
    print ' Testing assign_all_data_to_nearest_centroids'
    pt1 = Point(3,5)
    pt2 = Point(5,6)
    pt3 = Point(10,12)
    pt4 = Point(11,13)
    pt5 = Point(11,14)
    kmeans = KMeansCluster(2, [pt1, pt2, pt3, pt5])
    kmeans.centroids = [pt1, pt4]
    kmeans.assign_all_data_to_nearest_centroids()
    assert pt1 in kmeans.clusters[0]  # pt1 closest to pt1
    assert pt2 in kmeans.clusters[0]  # pt2 closest to pt1
    assert pt3 in kmeans.clusters[1]  # pt3 closest to pt4
    assert pt5 in kmeans.clusters[1]  # pt5 closest to pt4

def update_centroid_positions_test():
    print ' Testing update_centroid_positions'
    pt1 = Point(3,5)
    pt2 = Point(5,6)
    pt3 = Point(10,12)
    pt4 = Point(11,13)
    pt5 = Point(11,14)
    kmeans = KMeansCluster(2, [pt1, pt2, pt3, pt5])
    kmeans.clusters = {0 : [pt1, pt2], 1 : [pt3, pt5]}
    kmeans.update_centroid_positions()
    assert kmeans.centroids[0].x == 4
    assert kmeans.centroids[0].y == 5.5
    assert kmeans.centroids[1].x == 10.5
    assert kmeans.centroids[1].y == 13

def get_mean_of_points_test():
    print ' Testing get_mean_of_points'
    pt1 = Point(3,5)
    pt2 = Point(5,6)
    pt3 = Point(10,12)
    pt4 = Point(11,13)
    pt5 = Point(11,14)
    kmeans = KMeansCluster(2, [pt1, pt2, pt3, pt5])
    mean_point = kmeans.get_mean_of_points([pt1, pt2])
    assert mean_point.x == 4
    assert mean_point.y == 5.5
    mean_point = kmeans.get_mean_of_points([pt3, pt4, pt5])
    assert round(mean_point.x, 4) == 10.6667
    assert mean_point.y == 13

def read_points_from_file_test():
    print ' Testing read_points_from_file'
    filename = 'testme.txt'
    with open(filename, 'w') as outfile:
        outfile.write('50\t60\n20\t30')
    outfile.close()
    points = read_points_from_file(filename)
    assert points[0].x == 50
    assert points[0].y == 60
    assert points[1].x == 20
    assert points[1].y == 30



def main():
    distance_to_test()
    closest_point_test()
    distance_to_origin_test()
    initialize_clusters_test()
    initialize_centroids_test()
    get_nearest_centroid_for_point_test()
    assign_all_data_to_nearest_centroids_test()
    update_centroid_positions_test()
    get_mean_of_points_test()
    read_points_from_file_test()
    kmeans_plot()
    

main()

