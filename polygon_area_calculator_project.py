class Rectangle:
    ''' create Rectangle Objects'''    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, new_width):
        self.width = new_width
    
    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter = self.width*2 + self.height*2
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width**2 + self.height**2) ** 0.5
        return diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        picture = f"{'*' * self.width}\n" * self.height
        return picture 
    
    # still to be checked 
    def get_amount_inside(self, other):
        amount = self.get_area() // other.get_area()
        return amount





class Square(Rectangle):
    
    def __init__(self, side):
        super().__init__(side, side)  
        self.width = side
        self.height = side
        self.side = side
    
    def __str__(self):
        return f'Square(side={self.side})'

    # make the set methods set both width and height
    def set_side(self, new_side):
        self.width = new_side 
        self.height = new_side
        self.side = new_side
    
    def set_width(self, new_width):
        self.width = new_width
        self.height = new_width
        self.side = new_width

    
    def set_height(self, new_height):
        self.height = new_height
        self.width = new_height
        self.side = new_height
    
        











 


# Test zone:
rec1 = Rectangle(4, 8)
print('area:', rec1.get_area())
print('perimeter:', rec1.get_perimeter())
print('diagonal:', rec1.get_diagonal())
print('pic:')
print(rec1.get_picture())
rec2 = Rectangle(15, 10)
sq1 = Square(4)
print(rec1)
sq1.set_side(5)
print(sq1)
print(
    rec2.get_area(), '|',
 sq1.get_area()
 )
print(rec2.get_amount_inside(sq1))