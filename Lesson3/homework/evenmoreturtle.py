colors = ['red','blue','brown','yellow','grey']

# from turtle import*
# shape('turtle')

# for x in range (3,8):
#     for i in range(x):
#         color(colors[x-3])
#         forward(100)
#         left(360/x)
        

# mainloop()


from turtle import*
shape('turtle')

for i in range(5):
    color(colors[i])
    fillcolor(colors[i])
    begin_fill()

    forward(50)
    left(90)
    forward(100)
    left(90)
    forward(50)
    left(90)
    forward(100)
    left(90)
    forward(50)

    end_fill()

mainloop()


