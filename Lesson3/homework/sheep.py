ls = [9,29,10,65,78,147,350,210]

print('Please press Enter key to continue seeing results')
input()
#2.1
print('Hello, my name is Dung and these are my sheeps sizes')
print(ls,end='')

input()

print()


#2.2-2.5

n = int(input('Number of years: '))
for t in range(n):
    i=0
    for v in ls:
        x=v+50
        ls[i]=x
        i+=1
    input()

    print('Month',t+1,':',end='')

    input() 

    print('One month has passed, now here is my flock\n',ls,sep='')
    print('Now my biggest sheep has size:',max(ls),"\nLet's shear it!",end='')

    input()

    ls[ls.index(max(ls))]=8
    print('After shearing, here is my flock\n',ls,sep='')
    print()
input()

#2.6

total = 0
for s in ls:
    total += s
print('My flock has size in total:',total)
print('I would get ',total,' *$2 = ',' $',total*2,sep='')


