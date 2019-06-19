# from turtle import*
# shape('turtle')
# color('red','red')

# left(120)
# for i in range (4):
#     right(150)
#     forward(80)
#     left(60)
#     forward(80)
#     left(120)
#     forward(80)
#     left(60)
#     forward(80)

# mainloop()

n = int(input('Enter the number of shapes: '))
from turtle import*
shape('turtle')

for x in range (3,n+1):
    for i in range (x):
        if x%2==1:
            color('red','red')
        else:
            color('blue','blue')
            
        forward(100)
        left(360/x)
        
mainloop()


