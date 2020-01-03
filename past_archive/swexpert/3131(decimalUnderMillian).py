def isDecimal1(a):
    import math
    if a==2:
        return True
    if a==1 or a%2==0:
        return False
    for i in range(3,int(math.sqrt(a))+1,2):
        if a%i==0:
            return False
    return True
L=[]
for i in range(1000000):
    if isDecimal1(i+1)==True:
        L.append(i+1)
print(*L)
