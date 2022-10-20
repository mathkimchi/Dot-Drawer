'''
any point in S furthest from any point P is garunteed to be in the hull.
Conjecture: if we have a shape that surrounds the 
'''
'''
Wrapping method: if a point in S and on the perimeter of the C Hull is chosen as a "pivot",
then you can have a line to seperate it from everything else and then rotate the line 
and every time the line intersects a point, then use that point as a new pivot and 
repeat until you reach the og point.

If we find a point with the lowest X value, then we can use that as a pivot
And I realize that the line that has all points on one side is just a vertical line

I did something similar with y bc tan works with - being 0rad
'''

import math

def counterClockChange(original, new):
    if(new<original): return new-original+2*math.pi
    return new-original
    # just (new-original)//2*math.pi?

def angleFinder(original, new):
    x=new[0]-original[0]
    y=new[1]-original[1]
    if(x==0 and y==0): return 9001
    if(x==0): return 0
    # could be rewritten
    if(y>=0): # q1 q2
        if(x>0): # q1
            return math.atan(y/x)
        else: # q2
            return math.atan(y/x)+math.pi
    else: # q3 q4
        if(x>0): # q4
            return 2*math.pi+math.atan(y/x)
        else: # q3
            return math.atan(y/x)+math.pi


def nextPoint(pivot, angle, points):
    return min(points, key=lambda point: counterClockChange(angle, angleFinder(pivot, point)))

def convexHullFinder(points): # if point is on perimeter you can include or exclude, doesn't matter
    pivot=min(points, key=lambda point: point[1])
    angle=0
    hull=[pivot]
    while True:
        pivot=nextPoint(pivot, angle, points)
        print(pivot)
        if(pivot==hull[0]): return hull
        hull.append(pivot)
        angle=angleFinder(hull[-2], pivot)

if __name__=="__main__":
    print(convexHullFinder([[30, 60], [50, 40], [0, 30], [15 ,25], [70, 30], [55, 20], [50, 10], [20, 0]]))