# CTI-110
# P4LABa - Square & Triangle
# Angela Joplin
# 11/2/2022

# Use turtle to draw a square and a triangle
# Figure out range and angle then use for loop to replicate the sides

import turtle as t   

t.pensize(5)           
t.pencolor("skyblue")     
t.shape("turtle")

t.penup()
t.bk(100)
t.pendown()

for i in range(4):
    t.forward(100)         
    t.left(90)  

t.penup()
t.forward(120)
t.pendown()
t.pencolor("violet")

for i in range(3):
    t.forward(110)          
    t.left(120)

t.penup()
t.forward(130)
t.pendown()

t.done()       
