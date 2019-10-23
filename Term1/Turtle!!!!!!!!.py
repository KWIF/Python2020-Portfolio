import turtle



 
colors = ['white', 'midnight blue', 'medium slate blue', 'steel blue', 'cyan', 'cadet blue',
          'dark green', 'dark slate gray', 'azure'] 
t = turtle.Pen() 
turtle.bgcolor('black') 
for x in range(9999):
    t.speed(0)
    t.pencolor(colors[x%6]) 
    t.width(x/100 + 10) 
    t.forward(x) 
    t.left(865)
    
