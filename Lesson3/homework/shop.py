while True:
    n = input('Welcome to our shop, what do you want? ')
    ls=['T-Shirt','Sweater']


    if n == 'C' or n=='c':
        x=input('Enter new item ')
        ls.append(x)
        print('Our items:',ls)

    elif n == 'R' or n=='r':
        print('Our items:',ls)

    elif n == 'U' or n=='u':
        i=int(input('Update position? '))
        x=input('New items? ')
        ls[i]=x
        print('Our items:',ls)


    elif n == 'D' or n =='d':
        while True:
            i=int(input('Delete position? '))
            if -2<=i<=1:
                break
            else:
                print('Enter position again')

        del ls[i]
        print('Our item:',ls)

    else:
        print('Please reenter your action')
    
