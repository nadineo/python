##################################################
# IINI4014 Python for programmers (2018 HØST)
# Nadine Obwaller
# Exercise 5: Drawing with turtle
##################################################

import turtle
import math
import random
import argparse

def calc_circle_coord(divisions):
    dot_positions = []
    #calculate angle per division of circle
    angle_per_division = 360/divisions*math.pi/180
    #calculate coordinates per division
    for i in range(divisions):
        x = radius*math.cos(i*angle_per_division)
        y = radius*math.sin(i*angle_per_division)+radius
        dot_positions.append((x,y))
    return dot_positions
    
def drawCircle(divisions, times):
    #set color of pen
    myTurtle.pencolor(colors[1])
    #call function to calculate circle positions
    coord_positions = calc_circle_coord(divisions)
    myTurtle.pensize(1)
    #draw surrounding circle
    myTurtle.circle(radius)
    myTurtle.pensize(0)
    
    for i in range(divisions):
        myTurtle.penup()
        myTurtle.goto(coord_positions[i][0],coord_positions[i][1])
        myTurtle.pendown()
        myTurtle.pencolor(colors[i%3])
        myTurtle.goto(coord_positions[(i*times)%divisions][0], coord_positions[(i*times)%divisions][1])
        

colors = [(0.2, 0.8, 0.55),(0.2, 0.3, 0.43),(0.1, 0.5, 0.23)]
radius = 200
myTurtle = turtle.Turtle()
myTurtle.speed(0)

parser = argparse.ArgumentParser(description='Turtle Graphics - Mandelbrot.')
parser.add_argument('cnt_div', type=int,help='number of divisions of the circle')
parser.add_argument('cnt_times', type = int ,help='times to multiply division')

# call for example with:  python3 ex5.py 200 134  
args = parser.parse_args()
drawCircle(args.cnt_div, args.cnt_times)
turtle.mainloop()






