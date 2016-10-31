##########################################################################
# Author: Zhikai Guo
# turtule_draw_circle.py draws by drawing 36 squres, each tilted 10 degree
##########################################################################

import turtle

# Init a window screen for turtle to draw on
playground = turtle.Screen()
playground.bgcolor("red")

#Create the turtle Brad and some properties
brad = turtle.Turtle()
brad.shape("turtle")
brad.color("yellow")
brad.speed(5)

def draw_square(a_turtle, width):
	for i in range(4):
		a_turtle.forward(width)
		a_turtle.right(90)

def draw_circle(a_turtle, radius):
	for i in range(36):
		draw_square(a_turtle, radius)
		brad.right(10)

draw_circle(brad, 100)

playground.exitonclick()
