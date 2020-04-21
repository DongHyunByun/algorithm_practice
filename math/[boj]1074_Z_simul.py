N,r,c=map(int,input().split())

startNum=0
lastNum=2**(2*N)

def findLoc(x):
    a=r%x
    b=c%x
    half=x//2
    if a<half and b<half:
        return 0
    elif a<half and b>=half:
        return 1
    elif a>=half and b<half:
        return 2
    else:
        return 3

for i in range(N,0,-1):
    x=2**i
    k=findLoc(x)
    temp=startNum
    startNum=temp+(2**(2*i-2))*k
    lastNum=startNum+2**(2*i-2)
    #print(startNum,lastNum)
print(startNum)