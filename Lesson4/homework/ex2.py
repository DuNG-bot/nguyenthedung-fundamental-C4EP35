prices = {
    'banana':4,
    'apple':2,
    'orange':1.5,
    'pear': 3,
}

stock = {
    'banana':6,
    'apple':0,
    'orange':32,
    'pear': 15,
}


for i in prices:
    print(i,'\nprices:',prices[i],'\nstock:',stock[i],'\n')


total = 0
for v in prices:
    s = prices[v]*stock[v]
    total += s

print('Total amout of money you can make:',total)