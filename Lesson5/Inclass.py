# n = int(input('Nhap so phan tu: '))
# ls_n = []
# for i in range(n):
#     x = float(input('Nhap so thu '+str(i+1)+':'))
#     ls_n.append(x)

# total = 0
# for v in ls_n:
#     total += v
# print('Tong day so vua nhap la:',total)


####
# ls_m = []
# m = int(input('Nhap so phan tu: '))
# for s in range(m):
#     y = int(input('Nhap so '))
#     ls_m.append(y)

# T=0
# for s in ls_m:
#     T += s

# print('Trung binh cong day so vua nhap la:',T/len(ls_m))


####### FUNCTION

# FUNCTION k tham so
# def say_hi():
#     print('hi')
# print('bye')   #k thuoc ham tren

# say_hi()


# FunCTtion co tham so - k return

# def add_two_number(a,b):
#     # a = int(input('Nhap so thu nhat: '))
#     # b = int(input('Nhap so thu hai: '))
#     print('Tong hai so la',a+b)

# add_two_number(4,5)

#FUNCTION co tham so - co RETURN
# def add(x,y):
#     return x+y

# a=3
# b=6
# c=9
# sum_all = add(add(a,b),c)
# print(sum_all)


#Example:
# def evaluate(a,b,c):
#     if c == '+':
#         return a+b
#     elif c =='-':
#         return a-b
#     elif c == '*':
#         return a*b
#     elif c == '/':
#         return a/b
    

# print(evaluate(1,3,'+'))


def is_prime(a):
    
    ls_prime=[]
    for num in range (2,1000):
        prime=True
        for i in range(2,num):
            if num%i==0:
                prime=False
        if prime:
            ls_prime.append(num)
    print(ls_prime)
    print(a in ls_prime)

is_prime(12)