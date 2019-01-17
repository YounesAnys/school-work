import turtle
s=turtle.Screen()
t=turtle.Turtle()

# Place your code after this line

#First Circle
t.penup()
t.goto(0,15)
t.pendown()
t.circle(5)
t.penup()

#Second Circle
t.goto(0,-30)
t.pendown()
t.circle(50)
t.penup()

#Third Circle
t.goto(0,-50)
t.pendown()
t.circle(70)
t.penup()

#Fourth Circle
t.goto(0,-70)
t.pendown()
t.circle(90)
t.penup()

#Horizontal Line Left to Right
t.goto(-150,20)
t.pendown()
t.goto(150,20)
t.penup()

#Horizontal Line Top to Bottom
t.goto(0,170)
t.pendown()
t.goto(0,-130)
t.penup()

#Diagonal Line BLeft to TRight
t.goto(-115,-95)
t.pendown()
t.goto(115,135)
t.penup()

#Diagonal Line TLeft to BRight.
t.goto(-110, 130)
t.pendown()
t.goto(120,-100)
t.penup()
