# Family name: Vida Dujmovic 
# Student number:  123456
# Course: IT1 1120 
# impAssignment Number 1

import turtle

###################################################################
# Question 1
###################################################################
def f2k(t):
    ''' (number)->number
    Returns the temperature t expressed in fahrenheight as kelvin'''

    return (t - 32) * 5 / 9 + 273.15


###################################################################
# Question 2
###################################################################
def bibformat_apa(author, title, city, publisher, year):
    ''' (str, str, str, str, int)->str
    Return an APA style bibliographic entry'''
    
    return author+" "+"("+str(year)+"). "+title+". "+city+": "+publisher+"."


###################################################################
# Question 3
###################################################################
def joker():
    ''' (None)->None
    Print a joke using a name input by the user'''
    
    name = input("Enter your name: ")
    print ("Why did", name, "dump ground beef on his head?")
    print ("She wanted a meatier shower!")


###################################################################
# Question 4
###################################################################
def bibformat_apa_display():
    '''(None)->None
    Print an APA style bibliographic entry'''

    title = input("Enter the title of a book: ")
    author = input("Enter the name of the author? ")
    year = int(input("What year was the book published? "))
    publisher= input("Enter the name of the publisher: ")
    city= input("In what city are the headquarters of the publisher? ")
    s=bibformat_apa(author, title, city, publisher, year)
    print(s)

###################################################################
# Question 5
###################################################################
def bmi(w,h):
    '''
    (number, number)->number
    Return the bmi for someone h inches tall and weighing w pounds'''

    return (w/(h**2))*703

###################################################################
# Question 6
###################################################################
def f2fi(f):
    '''(number)->(int, number)
    Return feet f expressed as feet fh and inches i'''

    fh=int(f)
    i=(f-fh)*12
    return (fh, i)


###################################################################
# Question 7
###################################################################
def bmi_calculator():
    '''(None)->None
    A simple application for reporting a user's BMI information'''

    app = input("Enter you appelation (Mr., Mrs., Dr.,...): ")
    fn = input("Enter your first name: ")
    ln = input("Enter your last name: ")
    h = int(input("Enter your height in inches: "))
    w = int(input("Enter your weight in pounds: "))
    print ("BMI Record for", app, fn, ln)
    print ("Subject is", h//12, "feet", h%12, "inches tall")
    print ("and weighs", w ,"pounds")
    print ("Subject's BMI is", bmi(w,h))


###################################################################
# Question 9
###################################################################
def forms_triangle(a, b, c):
    '''(number, number, number)->bool
       Returns True if given sides, a, b and c can form a triangle.
       Otherwise it returns false
       Precondition: a, b and c are non-negative numbers'''
       
    return (a<=b+c) and (b<=a+c) and (c<=a+b)


###################################################################
# Question 10
###################################################################
def change_to_coins(amount):
    '''
       (number)->int
       Returns minumum number of coins given amount of dollars
       Precondtion: amount is a positive number 
    '''
    cents=round(amount*100) 
    print(cents)
    quarters=cents//25
    cents=cents%25    #this computes remaining number of cents after quarters are removed

    dimes=cents//10
    cents=cents%10

    nickels=cents//5
    pennies=cents%5
    
    return (quarters+dimes+nickels+pennies)


###################################################################
# Question 8 -- solution by Muraad Farah Hared
###################################################################
def draw_court():
    '''
    (None)->None
    Draws a basketball court with turtle graphics
    '''
    #initialize the turtle
        
    s=turtle.Screen() 
    t=turtle.Turtle()

    #Set colour of court and pen
    s.bgcolor("#A89261")
    t.pencolor("white")
    t.pensize(3)

    #Draw the Outer Rectangular Court
    t.penup()
    t.goto(-300,150)
    t.pendown()

    t.goto(300,150)
    t.goto(300,-150)
    t.goto(-300,-150)
    t.goto(-300,150)

    #Draw the center circle
    t.fillcolor("#F3974A")
    t.begin_fill()
    t.penup()
    t.goto(0,-40)
    t.pendown()
    t.circle(40)
    t.end_fill()

    #Draw the half-court line
    t.penup()
    t.goto(0,150)
    t.pendown()
    t.goto(0,-150)

    ##DRAWING FOR THE LEFT SIDE OF THE COURT

    #Draw the 3-pointer line
    t.penup()
    t.goto(-300, 120)
    t.pendown()
    t.goto(-265,120)
    t.circle(-120,180)
    t.goto(-300,-120)

    #The inner box
    t.begin_fill()
    t.penup()
    t.goto(-300,-40)
    t.pendown()
    t.goto(-185,-40)
    t.goto(-185,40)
    t.goto(-300,40)
    t.end_fill()

    #The outer box

    t.penup()
    t.goto(-300,-55)
    t.pendown()
    t.goto(-185,-55)
    t.goto(-185,55)
    t.goto(-300,55)

    #The circle
    t.penup()
    t.goto(-185,-40)
    t.setheading(0)
    t.pendown()
    t.circle(40,180)

    #Dashed line semi circle: need to perform multiple penup() and pendown() functions

    t.pensize(2) #set pensize to 2 for thinner line
    t.circle(40,15)
    t.penup()
    t.circle(40,8)
    t.pendown()

    t.circle(40,15)
    t.penup()
    t.circle(40,8)
    t.pendown()

    t.circle(40,15)
    t.penup()
    t.circle(40,8)
    t.pendown()

    t.circle(40,15)
    t.penup()
    t.circle(40,8)
    t.pendown()

    t.circle(40,15)
    t.penup()
    t.circle(40,8)
    t.pendown()

    t.circle(40,15)
    t.penup()
    t.circle(40,8)
    t.pendown()

    t.circle(40,15)
    t.penup()
    t.circle(40,8)
    t.pendown()

    t.circle(40,15)
    t.penup()
    t.circle(40,8)
    t.pendown()

    t.pensize(3) #set pensize back to 3 since the semi cirlce is complete
    #The net
    t.penup()
    t.goto(-282,-20)
    t.pendown()
    t.goto(-282,20)
    t.goto(-282,0)
    t.goto(-275,0)
    t.setheading(-90)
    t.fillcolor("white")
    t.begin_fill()
    t.circle(4)
    t.end_fill()

    ##DRAWING FOR THE RIGHT SIDE OF THE COURT

    #Draw the 3-pointer line
    t.penup()
    t.goto(300, 120)
    t.pendown()
    t.goto(265,120)
    t.setheading(180)
    t.circle(120,180)
    t.goto(300,-120)

    #The inner box
    t.fillcolor("#F3974A")
    t.begin_fill()
    t.penup()
    t.goto(300,-40)
    t.pendown()
    t.goto(185,-40)
    t.goto(185,40)
    t.goto(300,40)
    t.end_fill()

    #The outer box

    t.penup()
    t.goto(300,-55)
    t.pendown()
    t.goto(185,-55)
    t.goto(185,55)
    t.goto(300,55)

    #The circle
    t.penup()
    t.goto(185, 40)
    t.setheading(180)
    t.pendown()
    t.circle(40,180)

    #Dashed line semi circle

    t.pensize(2) #set pensize to 2 for a thinner line
    t.circle(40,15)
    t.penup()
    t.circle(40,8)
    t.pendown()

    t.circle(40,15)
    t.penup()
    t.circle(40,8)
    t.pendown()

    t.circle(40,15)
    t.penup()
    t.circle(40,8)
    t.pendown()

    t.circle(40,15)
    t.penup()
    t.circle(40,8)
    t.pendown()

    t.circle(40,15)
    t.penup()
    t.circle(40,8)
    t.pendown()

    t.circle(40,15)
    t.penup()
    t.circle(40,8)
    t.pendown()

    t.circle(40,15)
    t.penup()
    t.circle(40,8)
    t.pendown()

    t.circle(40,15)
    t.penup()
    t.circle(40,8)
    t.pendown()

    t.pensize(3) #Set pensize back to 3 to complete the court

    #The net
    t.penup()
    t.goto(282,-20)
    t.pendown()
    t.goto(282,20)
    t.goto(282,0)
    t.goto(275,0)
    t.fillcolor("white")
    t.begin_fill()
    t.setheading(90)
    t.circle(4)
    t.end_fill()

    #Hide the turtle
    t.hideturtle()
