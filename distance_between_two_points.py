import math
# TAKES IN TWO POINTS AS THEIR X AND Y COORDINATES AS ARGUMENTS
# RETURNS THE DISTANCE BETWEEN THEM
def distance_between_points(x1,y1,x2,y2):
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    print(distance)
    return distance
    
# EXAMPLE
distance_between_points(2, 5, -3, 8)    
