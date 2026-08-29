  
def equilateral(sides): #sides
    a, b, c = sides
    if a != 0 and b != 0 and c != 0:     #a + b >= c and a + c >= b and b + c >= a
       return a == b and b == c  #in case correct
   

def isosceles(sides):
    a, b, c = sides
    if a != 0 and b != 0 and c != 0:  
       return a == b or a == c or b == c 
    


def scalene(sides):
    a, b, c = sides
    if a != 0 and b != 0 and c != 0: 
       return a != b != c 
    
    