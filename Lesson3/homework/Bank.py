t = 21
x = 6.5/100

print('Sau 9 nam, a co tat ca',t*(1+x)**9,' trieu trong tai khoan')

i=1
while True:
    s=t*(1+x)**i
    if s>1200:
        break
    else:
        i+=1

    
    
print('Anh can gui ngan hang',i,'nam')