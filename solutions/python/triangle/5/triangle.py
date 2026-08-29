  
def equilateral(sides): #sides
    a, b, c = sorted(sides)
    if a != 0 and b != 0 and c != 0:     #a + b >= c and a + c >= b and b + c >= a
       return a == b and b == c  #in case correct
    else: return False
   

def isosceles(sides):
    a, b, c = sorted(sides)
    if a != 0 and b != 0 and c != 0:  
       return a == b or a == c or b == c 
    else: return False


def scalene(sides):
    a, b, c = sorted(sides)
    if a != 0 and b != 0 and c != 0: 
       return a != b != c 
    else: return False
    