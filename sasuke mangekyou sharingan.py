import turtle as t

#eye circle
t.title("Sasuke Mangekyou Sharingan")
t.bgcolor('#bf0404')
t.pensize(10)
t.speed(5)
t.color('black')
t.pu()
t.goto(0,200)
t.pd()
t.fillcolor('black')
t.begin_fill()
t.circle(-200)
t.end_fill()

# internal red eyes
t.color('black')
t.pu()
t.goto(0,190)
t.pd()
t.seth(-60)
t.fillcolor('red')
t.begin_fill()
t.circle(-380,60)
t.rt(120)
t.circle(-380,60)
t.end_fill()

t.pu()
t.goto(-164.5,95)
t.pu
t.seth(0)
t.fillcolor('red')
t.begin_fill()
t.circle(-380,60)
t.rt(120)
t.circle(-380,60)
t.end_fill()

t.color('black')
t.pu()
t.goto(170.5,100)
t.pu
t.seth(-118)
t.fillcolor('red')
t.begin_fill()
t.circle(-380,60)
t.rt(120)
t.circle(-380,60)
t.end_fill()

# internal Red eyes black borders
t.color('black')
t.pu()
t.goto(0,190)
t.pd()
t.seth(-60)
t.circle(-380,60)
t.rt(120)
t.circle(-380,60)

t.color('black')
t.goto(-164.5,95)
t.seth(0)
t.circle(-380,60)
t.rt(120)
t.circle(-380,60)
t.end_fill()
t.penup()

t.goto(170.5,100)
t.seth(-118)
t.pendown()
t.circle(-380,60)
t.rt(120)
t.circle(-380,60)
t.end_fill()
t.penup()

#last internal eye circle
t.goto(5.0,-14.0)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(13)
t.end_fill()

t.done()
