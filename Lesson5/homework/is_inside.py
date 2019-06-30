def is_inside (a,b):
    if b[0] <= a[0] <= (b[0]+b[2]) and b[1] <= a[1] <= (b[1]+b[3]):
        return True
    else:
        return False
    

#Test:

Test = is_inside([200,120],[140,60,100,200]) 
if Test == True:
    print("Your function is correct")
else:
    print("There's a bug somewhere")
