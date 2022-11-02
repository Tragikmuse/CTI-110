# CTI-110
# P4LABb - Initials
# Angela Joplin
# 11/2/2022

# Use the turtle to draw an A and a J
# approximately centered with the back command before writing

import turtle as t            

t.pensize(10)
t.pencolor("magenta")
t.shape("turtle")

t.penup()
t.bk(50)
t.pendown()

t.left(250)
t.forward(100)
t.bk(100)

t.left(45)
t.forward(100)
t.bk(45)

t.right(113)
t.forward(40)

t.penup()
t.bk(100)
t.right(90)

t.forward(50)
t.pendown()

t.right(92)
t.forward(80)
t.bk(40)
t.right(90)
t.forward(65)
t.circle(-27,180)

t.penup()
t.bk(20)
t.left(90)
t.forward(11)
t.right(90)
t.pendown()

t.done()

