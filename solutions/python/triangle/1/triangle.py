def equilateral(sides):
    if(aretherezeroes(sides) == True or aretheretriangleviolation(sides) == False):
        return False
        
    return sides[0] == sides[1] == sides[2]


def isosceles(sides):
    if(aretherezeroes(sides) == True or aretheretriangleviolation(sides) == False):
        return False
    aresidesaandbthesame = sides[0] == sides[1]
    aresidesbandcthesame = sides[1] == sides[2]
    aresidesaandcthesame = sides[0] == sides[2]
    
    if(aresidesaandbthesame or aresidesbandcthesame or aresidesaandcthesame or equilateral(sides)):
        return True
    return False


def scalene(sides):
    if(aretherezeroes(sides) == True or aretheretriangleviolation(sides) == False):
        return False
    
    arethereanyequalsides = sides[0] == sides[1] or sides [1] == sides[2] or sides[2] == sides[0]
    
    if(arethereanyequalsides):
        return False
    
    return sides[0] != sides[1] != sides[2]

def aretherezeroes(sides):
    if sides[0] == 0:
        return True
    if sides[1] == 0:
        return True
    if sides[2] == 0:
        return True

def aretheretriangleviolation(sides):
    checkforc = (sides[0] + sides[1]) >= sides[2]
    checkfora = (sides[1] + sides[2]) >= sides[0]
    checkforb = (sides[0] + sides[2]) >= sides[1]
    
    return checkforc and checkfora and checkforb