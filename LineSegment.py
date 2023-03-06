# Author: Aubrey Floyd
# GitHub username: aubreyfloyd2
# Date: 3/6/2023
# Description: Class named Point with x and y coordinates with function to return distance between two
#              points. Class named LineSegment with endpoints that returns length, slope, and T/F if parallel.

class Point:
    """Class with two coordinate data points"""
    def __init__(self, x_coord, y_coord):
        """Initializes data members x and y coordinates"""
        self._x_coord = x_coord
        self._y_coord = y_coord

    def get_x_coord(self):
        return self._x_coord

    def get_y_coord(self):
        return self._y_coord

    def distance_to(self, point):
        """Returns distance between two points"""
        x_dist = ((self._x_coord - point.get_x_coord()) ** 2)
        y_dist = ((self._y_coord - point.get_y_coord()) ** 2)
        distance = (x_dist + y_dist) ** 0.5
        return distance

class LineSegment:
    """Creates class with two endpoints of a line segment"""
    def __init__(self, endpoint_1, endpoint_2):
        """Initializes data members for the endpoints"""
        self._endpoint_1 = endpoint_1
        self._endpoint_2 = endpoint_2

    def get_endpoint_1(self):
        return self._endpoint_1

    def get_endpoint_2(self):
        return self._endpoint_2

    def length(self):
        """returns the distance between its two endpoints"""
        return self._endpoint_1.distance_to(self._endpoint_2) # use of the Point's distance_to method

    def slope(self):
        """Returns the slope of the LineSegment"""
        y_slope = self._endpoint_2.get_y_coord() - self._endpoint_1.get_y_coord()
        x_slope = self._endpoint_2.get_x_coord() - self._endpoint_1.get_x_coord()
        return y_slope / x_slope

    def is_parallel_to(self, line_seg_2):
        """Takes LineSegments and returns True if parallel or False is not"""
        if abs(self.slope() - line_seg_2.slope()) < 1e-7:
            # compare float values for equality because of possible lack of precision or round-off errors
            return True
        else:
            return False


# point_1 = Point(7,4)
# point_2 = Point(-6,18)
# print(point_1.distance_to(point_2))
# line_seg_1 = LineSegment(point_1,point_2)
# print(line_seg_1.length())
# print(line_seg_1.slope())

# point_3 = Point(-2,2)
# point_4 = Point(24, 12)
# line_seg_2 = LineSegment(point_3,point_4)
# print(line_seg_1.is_parallel_to(line_seg_2))
