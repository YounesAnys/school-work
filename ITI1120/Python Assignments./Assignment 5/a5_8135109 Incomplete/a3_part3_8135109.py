#Assignment 5 part 3
#Mahyar Gorji 8135109
#ITI1120

class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In the case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'



class rectangle:
    
    def __init__(self, bottom_left, top_right, color):
        """(Point, Point, Point, str) -> None"""
        
        self.bottom_left = bottom_left
        self.top_right = top_right
        self.color = color

    def get_bottom_left(self):
        """Rectangle Instance -> Point"""
        return self.bottom_left

    def get_top_right(self):
        """Rectangle Instance -> Point"""
        return self.top_right

    def get_color(self):
        """Rectangle Instance -> Point"""
        return self.color

    def reset_color(self, color):
        """(Rectangle Instance, str) -> None"""
        self.color = color

    def get_perimeter(self):
        """Rectangle Instance -> float"""
        xaxisrectangle = (self.top_right.x) - (self.bottom_left.x) #Subtracts and finds 1 side length based on
                                                                                                                  #the x axis (width)
        yaxisrectangle = (self.top_right.y) - (self.bottom_left.y) #Subtracts and finds 1 side length based on
                                                                                                                  #the y axis (height)
        perimeter = (2*xaxisrectangle) + (2*yaxisrectangle)     #2*length + 2*Width = perimeter
        return perimeter

    def get_area(self):
        """Rectangle Instance -> float"""
        xaxisrectangle = (self.top_right.x) - (self.bottom_left.x) #Subtracts and finds 1 side length based on
                                                                                                                  #the x axis (width)
        yaxisrectangle = (self.top_right.y) - (self.bottom_left.y) #Subtracts and finds 1 side length based on
                                                                                                                  #the y axis (height)
        area = xaxisrectangle*yaxisrectangle
        return area

    def move(self, dx, dy):
        """(Rectangle Instance, int/float, int/float) -> None"""
        self.bottom_left.move(dx, dy) #moves bottom left x-coord by dx value, same as y-coord by dy value. 
        self.top_right.move(dx, dy) #moves top right x-coord by dx value, same as y-coord by dy value.

    #def intersects(self, intersects_other): I don't know

    def contains(self, xpoint, ypoint):
        """(Rectangle Instance, int/float, int/float) -> bool"""
        if (self.top_right.x >= x and self.bottom_left.x <= x and self.top_right.y >= y and self.bottom_left.y <=y):
            return True
        else:
            return False

    #Following three functions are the override functions.
        
    def __repr__(self):
        """Rectangle Instance -> str"""
        #Remember that __repr__ is an unambiguous description of the function when just the instance is typed.
        #This should follow the same format as __init__. Concatenate anything you want to add to it.
        strbottomleft = str(self.bottom_left)
        strtopright = str(self.top_right)
        #Color is already a string. No need to convert it.
        reprvar = "Rectangle(" + strbottomleft + "," + strtopright + "," + self.color + ")"
        return reprvar

    def __str__(self):
        strbottomleft = str(self.bottom_left)
        strtopright = str(self.top_right)
        #Color is already a string. No need to convert it.
        strvar = "This rectangle is has a bottom left corner at " + strbottomleft + " and a top right corner at " + strtopright + " which also is colored " + self.color + "."
        return strvar
    
    def __eq__(self, other):
        """(Rectangle Instance, Other Rectangle Instance) -> boolean"""
        return (self.bottom_left == other.bottom_left and self.top_right == other.top_right and self.color == other.color)

#class Canvas:

    #def __init__(
    
    
