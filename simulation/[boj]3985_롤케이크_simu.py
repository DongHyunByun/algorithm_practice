L=int(input())
N=int(input())

expected=0
expectedP=1
real=0
realP=1
cake=[0 for i in range(L)]

for i in range(1,N+1):
    a,b=map(int,input().split())
    size=b-a+1
    if size>expected:
        expected=size
        expectedP=i
    cnt=0
    for k in range(size):
        if cake[a+k-1]==0:
            cnt+=1
            cake[a+k-1]=i
    if cnt>real:
        real=cnt
        realP=i
print(expectedP)
print(realP)