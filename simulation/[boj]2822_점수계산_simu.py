def sortKey(L):
    return L[1]
L=[]
for i in range(8):
    L.append([int(input()),i+1])
L.sort()
tempL=L[3:]
tempL.sort(key=sortKey)
sum=0
for i in range(5):
    sum+=tempL[i][0]
print(sum)
print(*[tempL[i][1] for i in range(5)])



