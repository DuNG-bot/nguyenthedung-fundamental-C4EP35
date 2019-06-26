# n=int(input())

# if n > 0:
#     print(n)
# else:
#     print(-n)

# v=0
# while v<10:
#     print('Hi',v)
#     v+=1

# dem=0
# while True:
#     print('Hi',dem)

#     dem += 1
#     if dem >= 3:
#         break

# v=0
# while True:
#     v+=1
#     if v>10:
#         continue #break vong lap hien tai va tiep tuc vong lap tiep theo
#     if v>10:
#         break    #break khoi cac vong lap
#     print('Hi2')


# for v in range(10):
#     # print(v)
#     if v==3:
#         break
#     print(v)

# loop=True
# v=0
# while loop:
#     print('Hi')
#     v+=1
#     loop=v>3


# t=0
# while True:
#     passwd=input('Nhap pass: ')
    
#     if len(passwd)>=8:
#         break
#     else:
#         if t>3:
#             print('Ban nhap sai 5 lan')
#             break
#         else:
#             print('nhap sai r')
#             t += 1
# if t<=3:
#     print('pass vua nhap la: ',passwd)
# else: 
#     print('De nghi ban thu lan sau 30p')



#LIST:

#Value type: int, float
#Reference type: str, list

#CRUD - Create, read, update, delete

# t = 21
# x = 6.5/100

# n=1
# while t< 1200:
#     for i in range(n-1,n):
#         t*=(1+x)
#         n+=1
    
# print('Anh can gui ngan hang',n-1,'nam')

# n=int(input('so so nguyen '))

# ls=[]
# x=0
# for i in range(n):
#     x=int(input('Nhap so:'))
#     ls.append(x)
# print(ls)

# ss=0
# count=0
# for v in ls:
#     if v%2==0:
#         ss+=v
#         count+=1
# print('trung binh cong cac so chan la', ss/count



n=int(input('Nhap so can phan tich: '))
while True:
    if 0<=n<=1000000:
        break
    else:
        n=int(input('Nhap lai so can phan tich: '))
so_ptich=n



ls_prime=[]
for num in range (2,1000):
    prime=True
    for i in range(2,num):
        if num%i==0:
            prime=False
    if prime:
        ls_prime.append(num)

x=0
ls=[]
for i in range(len(ls_prime)):
    while n % ls_prime[i] == 0:
        n=n/ls_prime[i]
        ls.append(ls_prime[i])
        

print('So ban vua nhap la:',so_ptich,'\nla tich cac so nguyen to sau:',ls)




        

    

