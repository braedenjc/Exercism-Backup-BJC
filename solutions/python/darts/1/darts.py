import math

OUTER_CIRC_RADIUS = 10
MIDDLE_CIRC_RADIUS = 5
CENTER_CIRC_RADIUS = 1

OUT_OF_BOUNDS_POINTS = 0
OUTER_CIRC_POINTS = 1
MIDDLE_CIRC_POINTS = 5
CENTER_CIRC_POINTS = 10


def score(x, y):
    distance = get_distance(x, y)
    if(distance > OUTER_CIRC_RADIUS ):
        return OUT_OF_BOUNDS_POINTS
    elif(MIDDLE_CIRC_RADIUS < distance <= OUTER_CIRC_RADIUS):
        return OUTER_CIRC_POINTS
    elif(CENTER_CIRC_RADIUS < distance <= MIDDLE_CIRC_RADIUS):
        return MIDDLE_CIRC_POINTS
    else:
        return CENTER_CIRC_POINTS
        
#use the point-distance formula to calculate distance from center/bullseye
def get_distance(x, y): 
    return math.sqrt(pow(x, 2) + pow(y, 2))