import math

min,max=map(int,input().split())
sqrtMax=int(math.sqrt(max))+1
isNoNo=[1 for i in range(max-min+1)]

for i in range(2,sqrtMax):
    double=i**2

    start=math.ceil(min/double) #몫
    fin=(max//double)+1

    for j in range(start,fin):
        isNoNo[j*double-min]=0

#print(isNoNo)
print(sum(isNoNo))