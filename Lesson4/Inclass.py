#Tim gia tri min va max trong 1 list and index cua no

# n=int(input('Enter a number '))
# numb=[]
# min_numb=0
# max_numb=0



# for i in range(n):
#     v=input('Enter your number ')
#     while type(int(v)) != int:
#         v=input('Error! Re-enter ')
#     v_numb=int(v)
#     numb.append(v_numb)

# #MIN Value
# if len(numb) != 0:
#     min_numb=numb[0]
#     min_index=0
#     for i in range(1,len(numb)):
#         if numb[i]<min_numb:
#             min_numb=numb[i]
#     print('min is',min_numb)
#     print('So thu tu la:',min_index)
# else:
#     print('Your list is empty')

# #MAX Value
# if len(numb) != 0:
#     max_numb=numb[0]
#     max_index=0
#     for i in range(1,len(numb)):
#         if numb[i]>max_numb:
#             max_numb=numb[i]
#             max_index=i
#     print('max is',max_numb)
#     print('So thu tu la:',max_index)
# else:
#     print('Your list is empty')

##############

#DICTION

# bien  |   if
# list  |   for
# Dict  |   while
# cau truc du lieu +|+ Thuat toan  = program

#MD5checksum ==> check for virus

#Program: tu dien Anh-Viet

dic = {'computer':'may tinh','mouse':'chuot','keyboard':'ban phim'}

while True:
    word = input('Nhap tu can tra cuu: ')
    # if word in dic:
    #     print('Nghia cua tu la:',dic[word])
    # elif word =='quit' or word =='exit':
    #     break
    # else:
    #     print('Tu nay ko co trong tu dien')
    
    if word in ['quit','exit']:
        break


    if word in dic:
        print('Nghia cua tu la',dic[word])
    else:
        print('Tu nay ko co trong tu dien')


####

ls = [2,2,2,2,3,5,7,7,7,11]

dic  = {}

for v in ls:
    if v not in dic:
        dic[v]=0
    dic[v]+=1

s = ""
for v in dic:
    if dic[v] == 1:
        s = s + str(v) + ' x '
    else:
        s = s + '{}^{} x '.format(v,dic[v])

if len(s) > 0:
    s = s[0:len(s)-2]
print(s)


####

people = []

person1={
    'name':'nguyen van a'
    'age': 21
    'phone': ['0914367865','0913495035']
}

person2={
    'name':'nguyen van b'
    'age': 22
    'phone': ['0914367865','0913495035']
}

people.append(person1)
people.append(person2)

print(people)

#tim sdt

phone ='0914367865'

for v in people:
    if phone in v['phone']:
        print(v['name'])
