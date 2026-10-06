from turtle import Turtle

t = Turtle()

t.fillcolor("blue")
t.begin_fill()

for i in range(6):
    t.forward(80)
    t.left(60)

t.end_fill()

t.screen.mainloop()