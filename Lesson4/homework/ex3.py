ques1 = {
    1:35,
    2:36,
    3:40,
    4:44,
}
print('Answer the following algebra questions:')
print('If x = 8, then what is the value of 4(x+3) ?')
for i in ques1:
    print(i,'. ',ques1[i],sep='')
while True:
    answ1 = int(input('Your choice: '))
    if answ1 == 4:
        print('Bingo')
        break
    elif answ1 == 1 or 2 or 3:
        print(':(')
        break
    else:
        print('Please reenter your answer')