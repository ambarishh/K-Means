'''
Created on Nov 7, 2013
@author: Ambarish Hazarnis
'''
from Point import *

class KMeansCluster():
    """This is a class that will cluster your data. Clustering helps us summarize
    data, showing similarities between data points.
    """
    def __init__(self, new_K, new_data_points):
        """ Create a new clusterer with new_K clusters, using new_data_points
        """
        if new_K > len(new_data_points):
            raise ValueError("K (%s) cannot be larger than the number of datapoints (%s)!" % (new_K, new_data_points))
        self.K = new_K
        self.initialize_clusters(new_data_points)
        self.initialize_centroids()
        self.assign_all_data_to_nearest_centroids()

    
    def iterate(self):
        """ Go through one iteration of k-means clustering.
        """
        self.update_centroid_positions()
        self.assign_all_data_to_nearest_centroids()

    
    def initialize_clusters(self, new_data_points):
        """ Create a dictionary whose keys are from 0 to K and whose values
        are a list of Points (the class Point) assigned to each cluster.
        """
        self.clusters = {}  # TODO: fill in this dictionary
        cluster=0
        for i in range(self.K):
            self.clusters[i]=[]
            
        for x in new_data_points:
            if cluster==self.K: cluster=0
            self.clusters[cluster].append(x)
            cluster+=1
    
    def initialize_centroids(self):
        """ Create a list of K points representing the cluster centers.
        """
        self.centroids = []
        for i in range(self.K):
            self.centroids.append((self.clusters[i])[0])
        
        
    def get_nearest_centroid_for_point(self, other_point):
        """ Return the INDEX of the centroid that is closest to other_point
        """
        return other_point.closest_point(self.centroids)
    
    
    def assign_all_data_to_nearest_centroids(self):
        """ For each datapoint, assign the point to its nearest centroid
        by modifying which list the datapoint is a part of in self.clusters.
        """
        new_clusters={}
        for i in range(self.K):
            new_clusters[i]=[]
            
        for k in self.clusters:
            for x in self.clusters[k]:
                closest=self.get_nearest_centroid_for_point(x)
                new_clusters[closest].append(x)
        
        self.clusters=new_clusters
        

    
    def update_centroid_positions(self):
        """ For each centroid, update the centroid's location to the
        mean of the points that belong to this centroid's cluster
        """
        for i in range(self.K):
            self.centroids[i]=self.get_mean_of_points(self.clusters[i])
        
    
    def get_mean_of_points(self, list_of_points):
        """ Calculate the mean of the list of points.  Return a new Point
        whose x and y are the respective mean values.
        """
        sum_x,sum_y=0.0,0.0
        for p in list_of_points:
            sum_x+=p.x
            sum_y+=p.y
        x,y = sum_x/len(list_of_points), sum_y/len(list_of_points)
        mean_point = Point(x,y)
        return mean_point


def read_points_from_file(filename):
    """ Last but not least, read in a set of datapoints from a file and create
    a list of points.  The file will be formatted like this:
    
50<TAB>40
20<TAB>11
7<TAB>12
60<TAB>46

    """
    all_points = []
    
    infile=open(filename,"r")
    for line in infile.readlines():
        line=line.split("\t")
        x=line[0].rstrip(" \n\t")
        y=line[1].rstrip(" \n\t")
        p=Point(int(x),int(y))
        all_points.append(p)
    infile.close()
    return all_points


def kmeans_plot():
    """ This function tests the complete KMeans classification algorithm and
    plots intermediate steps. 
    """
    print 'testing K means clustering on some overlapping gaussians'
    import scipy
    from matplotlib import pyplot


    # generate some data from several different gaussians
    data = [Point(x,y) for x,y in scipy.random.normal([[0,2]] * 800, .5)]
    data.extend([Point(x,y) for x,y in scipy.random.normal([[2,2]] * 800, .5)])
    data.extend([Point(x,y) for x,y in scipy.random.normal([[1,0]] * 300, .5)])
    data.extend([Point(x,y) for x,y in scipy.random.normal([[1.4,.2]] * 300, .5)])
    data.extend([Point(x,y) for x,y in scipy.random.normal([[.6,.2]] * 300, .5)])
        
    # initialize
    num_clusters = 10
    kmeans = KMeansCluster(num_clusters, data)
    for i in range(10):
        # cluster
        print 'iteration', i
        kmeans.iterate()
        
        # plot
        pyplot.figure()
        for k in range(num_clusters):
            # draw the clusters in different colors
            xs, ys = zip(*[(p.x,p.y) for p in kmeans.clusters[k]])
            pyplot.plot(xs, ys, 'o', label='cluster %s' % k)
            pyplot.plot(kmeans.centroids[k].x, kmeans.centroids[k].y, 'k+', lw=3)
        #pyplot.legend()
        pyplot.savefig('kmeans_iteration_%s.png' % i)

#kmeans_plot()