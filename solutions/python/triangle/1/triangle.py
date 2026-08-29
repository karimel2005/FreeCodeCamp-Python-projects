  
def equilateral(a, b, c): #sides
    if a + b >= c and b + c >= a and a + c >= b:
       return a == b and b == c  #in case correct
    else:
        return "Oops! not a triangle."

def isosceles(a, b, c):
    if a + b >= c and a + c >= b and b + c >= a:  
       return a == b or a == c or b == c 
    else:
        return "Oops! not a triangle."


def scalene(a, b, c):
    if a + b >= c and a + c >= b and b + c >= a: 
       return a != b != c 
    else:
        return "Oops! not a triangle."