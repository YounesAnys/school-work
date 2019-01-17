import math
import random
import turtle

################################################
# Question 1 
###############################################

def f2k(t):
    k = (t + 459.67) * (5/9)
    return (k)

#########################################
# Question 2 
#########################################

def bibformat_apa(author, title, city, publisher, year):
    apa = (str(author) + "(" + str(year) + ")"+ "," + str(title) + "," + str(city) + "," + str(publisher) + ".")
    return (apa)
#Credit to fellow student Ashwin Anand, student number 8154187,
#for telling me that variables can be added to strings with plus signs.

#########################################
# Question 3 
#########################################

def joker():
    name = input("What is your name ")
    print("How many software engineers named", name, "does it take to change a light bulb? None. That's a hardware problem.")

#########################################
# Question 4 
#########################################
#call this one first, then call question 2 from a variable assignment.
def bibformat_apa_display():
    authorStr = input('What is the author name? ')
    titleStr = input ('what is the title? ')
    cityStr = input ('what is the city? ')
    publisherStr = input('what the publisher? ')
    yearStr = input('what is the year? ')
    newStr = bibformat_apa(authorStr, titleStr, cityStr, publisherStr, yearStr)
    return (str(newStr))

#########################################
# Question 5 
#########################################

def bmi(w, h):
    bmiamerican = float(703*w)/(h**2)
    return bmiamerican

#########################################
# Question 6 
#########################################

def f2fi(f):
    i = random.randrange(0, 12, 1)
    fh = (f - i/12)
    return (fh, i)
#I learned about the 'random' module using effbot.org. The link is as follows:
#http://effbot.org/pyfaq/how-do-i-generate-random-numbers-in-python.htm

#########################################
# Question 7 
#########################################

def bmi_calculator():
    Weight = float(input('What is your weight, in pounds? '))
    Height = float(input('What is your height, in inches? '))
    FirstName = str(input('What is your first name? '))
    LastName = str(input('What is your last name? '))
    Appelation = str(input('Please enter your appelation. '))
    newbmi = float(bmi(Weight, Height))
    HeightConversionFeet = int(Height//12)
    HeightConversionInches = int(Height%12)
    print ('BMI Record for ' + str(Appelation) + ' ' + str(FirstName) + ' ' + str(LastName) + ':')
    print ('Subject is ' + str(HeightConversionFeet) + ' feet, ' + str(HeightConversionInches) + ' inches tall and weighs ' + str(Weight) + ' pounds.')
    print ('BMI is ' + str(newbmi))

#########################################
# Question 8 
#########################################

def draw_court():
    s=turtle.Screen()
    t=turtle.Turtle(shape='arrow')

    #rectangle outside court
    t.speed(100)
    t.penup()
    t.goto(0,200)
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(500)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(250)

    #respective sides of court (right side)
    t.penup()
    t.goto(250,175)
    t.right(180)
    t.pendown()
    t.forward(30)
    t.circle(100, 180)
    t.forward(30)
    t.penup()
    t.goto(140,95)
    t.pendown()
    t.circle(-20)
    t.penup()
    t.goto(140,95)
    t.pendown()
    t.forward(111)
    t.penup()
    t.goto(140,55)
    t.pendown()
    t.forward(111)
    t.penup()
    t.goto(140,95)
    t.right(90)
    t.pendown()
    t.forward(50)
    t.left(90)
    t.forward(111)
    t.penup()
    t.goto(140,95)
    t.left(90)
    t.pendown()
    t.forward(10)
    t.right(90)
    t.forward(111)
    t.penup()
    t.backward(30)
    t.right(90)
    t.forward(10)
    t.pendown()
    t.forward(20)
    t.circle(-5)
    t.forward(20)
    t.penup()
    t.goto(0,200)

    #centercourt
    t.pendown()
    t.goto(0,-50)
    t.penup()
    t.goto(50, 75)
    t.pendown()
    t.circle(-50)

    #left side court
    t.penup()
    t.goto(-250,175)
    t.pendown()
    t.left(90)
    t.forward(30)
    t.circle(-100,180)
    t.forward(30)
    t.penup()
    t.goto(-120,75)
    t.right(90)
    t.pendown()
    t.circle(20)
    t.penup()
    t.forward(30)
    t.left(90)
    t.forward(19)
    t.pendown()
    t.forward(110)
    t.backward(110)
    t.left(90)
    t.forward(60)
    t.right(90)
    t.forward(110)
    t.backward(110)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.forward(110)
    t.backward(110)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(110)
    t.backward(30)
    t.left(90)
    t.forward(20)
    t.circle(5)
    t.forward(20)
    t.penup()

#########################################
# Question 9 
#########################################

def forms_triangle(a,b,c):
    sortedsmall,sortedmiddle,sortedlargest = sorted([a,b,c])
    return sortedsmall+sortedmiddle>=sortedlargest

#########################################
#Question 10 
#########################################

def change_to_coins(x):
    xincents = int(round(x*100))
    #Use round because (for example) 1.25 registers as 1.24999
    #and screws up the code. Credits to Ashwin Anand, student number 8154187
    #for telling me about this bug. No information on how to solve it
    #was given, however.
    quarters = xincents//25
    xincents = xincents%25
    #Above is for quarters
    dimes = xincents//10
    xincents = xincents%10
    #Above is for dimes
    nickels = xincents//5
    xincents = xincents%5
    #Above is for nickels
    pennies = xincents
    #Above is for pennies.
    coincount = quarters + dimes + nickels + pennies
    return int(coincount)


        
