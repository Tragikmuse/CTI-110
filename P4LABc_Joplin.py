# CTI-110
# P4LABc - Snowflake
# Angela Joplin
# 11/2/2022

# Make a branch and use a loop to replicate the original branch to create a snowflake
# Step by step is literally in the program below (please dont make me repeat it)

import turtle as t

t.pensize(5)
t.shape("turtle")
t.speed(2000)


for i in range(8):
    t.pencolor("skyblue")
    t.forward(250)
    t.bk(60)
    t.left(45)
    t.forward(70)
    t.bk(70)
    t.right(90)
    t.forward(70)
    t.bk(70)
    t.left(45)
    t.bk(70)
    t.left(45)
    t.forward(50)
    t.bk(50)
    t.right(90)
    t.forward(50)
    t.bk(50)
    t.left(45)
    t.pencolor("blue")
    t.bk(70)
    t.left(45)
    t.forward(50)
    t.bk(50)
    t.right(90)
    t.forward(50)
    for i in range(2):
        t.bk(50)
        t.left(45)

t.left(90)
    
t.done()
