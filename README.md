# neighborhood
#in this program we build Neighborhood which includes houses and people of different appropriate sizes and sun.

#we are importing turtle library, math library, and random library in order to use the different drawing tools, math operators and to play with randomness
import turtle
import math
import random

#wn is assigned as a variable which now as a graphics windows where we can play with turtle
wn = turtle.Screen()   
#alex is used as a pen to draw different items.
alex = turtle.Turtle()
alex.speed(0) #the speed of the pen is made very fast that no animation takes place. instead turtle jumps instantly.
alex.hideturtle() #the turtle is hid to make the drawings look smooth

#the following block of code defines a function called that returns the random color code in hexadecimal
from random import choice
def random_color(): # name of the function is random_color

  hex_chars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
  colorcode = '#'
  colorcode = colorcode + choice(hex_chars)
  colorcode = colorcode + choice(hex_chars)
  colorcode = colorcode + choice(hex_chars)
  colorcode = colorcode + choice(hex_chars)
  colorcode = colorcode + choice(hex_chars)
  colorcode = colorcode + choice(hex_chars)
  return colorcode

#the following block of code defines a function called move moves the turtle to a absolute specified position 
def move(t,x,y):
  t.up()
  t.goto(x,y)
  t.down()

#the following block of code defines a function called moveRelative that moves turtle to a relatively from a given position
def moveRelative(t,x,y,d):
  t.up()
  t.goto(t.pos()[0]+x,t.pos()[1]+y)
  t.down()
  t.seth(d) #this line of code is used to determine the final direction of the turtle

#the following block of code defines a function called drawRectangle that draws a draws a rectangle of specified height and width and fills it with random color 
def drawRectangle(t,height,width):
  t.color(random_color())
  t.begin_fill()
  t.fillcolor(random_color())
  for i in range(2):
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
  t.end_fill()

#the following block of code defines a function called drawTriangle that draws a drawTriangle of given size in a given color 
def drawTriangle(t,size,color):
  i=0
  t.pencolor(color)
  while i<3:      # repeat four times
    t.forward(size)
    t.left(120)
    i+=1


#the following block of code defines a function called drawPolygon that draws a regular polygon of a random color of given number of side and size
def drawPolygon(t,sides,size):
  t.color(random_color())
  t.begin_fill()
  t.fillcolor(random_color())
  for i in range(sides): 
    t.forward(size) 
    t.right(360 / sides)
  t.end_fill()

#the following block of code defines a function called drawScalableShape that saves the start position  
def drawScalableShape(t,size):
  #Save start Position
  sPos=t.pos()

#the following block of code defines a function called sun that draws a yellow sun on position 500 * 500
def sun():
  move(alex, 500, 500)
  alex.color("orange")
  alex.begin_fill()
  alex.fillcolor("yellow")
  alex.circle(15)
  alex.end_fill()

#the following block of code defines a function called  drawScalableHouse that draws a house on the basis of a given scale size
def drawScalableHouse(t,size):
  sPos=t.pos()
  drawRectangle(t, size * 4 , size * 6)
  moveRelative(t, 0 , size*4,0)
  drawTriangle(t, size *6, "green")
  moveRelative(t, 0.75*size , -size*0.5,0)
  drawPolygon(t, 4, size)
  moveRelative(t, 3*size , 0 ,0)
  drawPolygon(t, 4, size)
  moveRelative(t, -1.25*size , -3.5*size ,0)
  drawRectangle(t, size * 2 , size)
  move(t,sPos[0],sPos[1])

#the following block of code defines a function called  drawScalablePerson that draws a person of random color on the basis of a given scale size
def drawScalablePerson(x,y,size):
  move(alex, x, y)
  alex.color(random_color())
  alex.begin_fill()
  alex.circle(size)
  alex.end_fill()
  alex.color(random_color())
  alex.right(90)
  alex.forward(size)
  alex.left(90)
  alex.forward(2*size/3)
  alex.backward(4*size/3)
  alex.forward(2*size/3)
  alex.right(90)
  alex.forward(2*size/3)
  alex.right(45)
  alex.forward(2*size/3)
  alex.backward(2*size/3)
  alex.left(90)
  alex.forward(2*size/3)
  alex.left(45)  

#the following block of code defines a function called  buildNeighborhood that draws 3 houses and 5 people and a sun
def buildNeighborhood(t,h,p):
  drawScalableHouse(alex, 50)
  move(alex, 500, 250)
  drawScalableHouse(alex, 25)
  move(alex, -500, 150)
  drawScalableHouse(alex, 45)
  drawScalablePerson(100,-150,15)
  drawScalablePerson(350, 50,20)
  drawScalablePerson(-150,0,14)
  drawScalablePerson(-150,140, 10)
  sun()
  drawScalablePerson(-150, -170, 18)

#we call the function sun 
sun()

##the following block of code defines a function called drawhouse to make it easy to call for the purpose of drawing a house on a clicked position on the screen 
def drawhouse(x,y):
  alex.up()
  alex.goto(x,y)
  alex.down()
  move(alex, x , y)
  size = random.randint(25,50)
  drawScalableHouse(alex,size)

##the following block of code defines a function called drawperson to make it easy to call for the purpose of drawing a person on a clicked position on the screen 
def drawperson(x,y):
  alex.up()
  alex.goto(x,y)
  alex.down()
  move(alex, x , y)
  size = random.randint(10,20)
  drawScalablePerson(x,y,size)


#The following 3 blocks of codes creates a house of a random size filled with a random color. 
move(alex, random.randint(-200,300), random.randint(-200,300))
drawScalableHouse(alex, random.randint(25,50))

move(alex, random.randint(-200,300), random.randint(-200,300))
drawScalableHouse(alex, random.randint(25,50))

move(alex, random.randint(-200,300), random.randint(-200,300))
drawScalableHouse(alex, random.randint(25,50))

##The following block of codes creates 5 persons of random sizes filled with a random color.
drawScalablePerson(random.randint(-200,300),random.randint(-200,300),random.randint(10,20))
drawScalablePerson(random.randint(-200,300), random.randint(-200,300),random.randint(10,20))
drawScalablePerson(random.randint(-200,300),random.randint(-200,300),random.randint(10,20))
drawScalablePerson(random.randint(-200,300),random.randint(-200,300), random.randint(10,20))
drawScalablePerson(random.randint(-200,300),random.randint(-200,300), random.randint(10,20))

#the following block of codes is used to draw house/person on the screen where the user clicks based on the user's respose, 
answer = input("What do you want to creat on a screen? Type \'h\' for house and \'p\' for person: ")
while answer == "h":
  print("click on any part on the screen to create a house. ")
  wn.onclick(drawhouse)
  answer = input("Continue clicking on the screen to create more houses. \n Type \'p\' to create person.")

print("----------------------------------------------------------")
while answer == "p":
  print("click on any part on the screen to create a person. ")

  wn.onclick(drawperson)
  answer = input("Continue clicking on the screent to create more people. \n Type \'done\' and click on any part of the screen to exit ")

#After the user is done with the program, he/she can click on anywhere on the screen to close the program. This is possible by the following code 
wn.exitonclick()

