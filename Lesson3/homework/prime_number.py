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