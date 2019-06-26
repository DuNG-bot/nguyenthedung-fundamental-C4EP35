ques1 = {
    1:35,
    2:36,
    3:40,
    4:44,
}

ques2 = {
    1:'About 55',
    2:'About 65',
    3:'About 75',
    4:'About 85',
}
points=0
print('Answer the following algebra questions:')
print('If x = 8, then what is the value of 4(x+3) ?')
for i in ques1:
    print(i,'. ',ques1[i],sep='')
while True:
    answ1 = int(input('Your choice: '))
    if answ1 == 4:
        print('Bingo')
        points+=1
        break
    elif answ1 == 1 or 2 or 3:
        print(':(')
        break
    else:
        print('Please reenter your answer')
print('Estimate this answer (exact calcation is not required):')
print('Jack scored these marks in 5 tests: 49, 81, 72, 66 and 52. What is the median?')
for v in ques2:
    print(v,'. ',ques2[v],sep='')
while True:
    answ2 = int(input('Your choice: '))
    if answ2 == 2:
        print('Bingo')
        points+=1
        break
    elif answ2 == 1 or 4 or 3:
        print(':(')
        break
    else:
        print('Please reenter your answer')

print('You correctly answer',points,'out of 2 questions')