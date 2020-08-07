import turtle

vic = turtle.Turtle()
vic.color('black', 'blue')
vic.speed(3)
vic.shape('turtle')

vic.begin_fill()
for i in range (100):
    vic.forward(300)
    vic.left(165)
    
vic.end_fill()

turtle.done()