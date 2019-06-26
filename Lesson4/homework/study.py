string = input('Please enter a sentence: \n')
string = string.lower()
dic = {}
ls=[]

for i in string:
    if i not in dic:
        dic[i]=0
    
    dic[i]+=1
if ' ' in dic:
    del dic[' ']

for v in dic:
    ls.append(v)
ls.sort()

print('The frequency of characters is:')
for s in ls:
    print(s,dic[s])
