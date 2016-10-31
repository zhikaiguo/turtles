######################################################
# Author: Zhikai Guo
# trutle_draw_fractal_tree.py draw a fractal tree
######################################################
import turtle

# Init a window screen for turtle to draw on
playground = turtle.Screen()
playground.bgcolor("black")

#Create the turtle Brad and some properties
brad = turtle.Turtle()
brad.setpos(0,-200) # setting start point to be bottom mid of screen
brad.shape("turtle") # setting the shape
brad.color("yellow") # setting the color of line
brad.speed(20) # drawing speed
brad.left(90) # setting turtle to face north

# define the angle of the tree, can be adjusted to have different shape
angle = 30

# call draw() to draw the fractal tree
def draw():
	branch(100)

def branch(len):
	# draw a line
	brad.forward(len)

	# Setting break point for recurive call
	if len > 4:
		# adjust angle to right > pen down > 
		# get pos > draw > pen up > go back to pos > ajust angle back
		brad.right(angle)
		brad.down()
		root = brad.pos()
		branch(len * 0.67)
		brad.up()
		brad.setpos(root)
		brad.left(angle)

		# adjust angle to left > pen down > 
		# get pos > draw > pen up > go back to pos > ajust angle back
		brad.left(angle)
		brad.down()
		root = brad.pos()
		branch(len * 0.67)
		brad.up()
		brad.setpos(root)
		brad.right(angle)

# Draw the tree!!
draw()

# Once drawing done, click window to close program
playground.exitonclick()


