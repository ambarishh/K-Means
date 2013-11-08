'''
Created on Nov 7, 2013

@author: Ambarish Hazarnis
'''
class Point():
    """A Point is a single point in 2 dimensional space"""
    def __init__(self, new_x, new_y):
        """Create a new point at coordinates (new_x, new_y)
        """
        self.x = new_x
        self.y = new_y
    
    def __str__(self):
        """This lets you convert points into a pretty string use the str() function.
        So now you can type:
            print 'here is a point', Point(3,2)
        And it won't print junk.
        """
        return '(%s,%s)' % (self.x, self.y)

    def __repr__(self):
        """More extras for pretty-printing.  This function applies when the Point
        is inside a list or other object.
        """
        return '(%s,%s)' % (self.x, self.y)

    
    def distance_to(self, other_point):
        """Return the distance from this point to other_point.
        """
        import math
        return math.sqrt(math.pow((self.x-other_point.x),2)+math.pow((self.y-other_point.y),2))
    
    def closest_point(self, list_of_other_points):
        """Return the INDEX of the point that is closest to me (NOT the distance)
        """
        min,i=1000,0
        for x in list_of_other_points:
            dist=self.distance_to(x)
            if min > dist:
                min=dist
                index=i
            i+=1
        return index
    
    def distance_to_origin(self):
        """Return the distance from this point to the origin, i.e.,
        from this point to (0,0).
        """
        import math
        return math.sqrt(math.pow((self.x),2)+math.pow((self.y),2))
