from collections import deque

D,N=map(int,input().split())
oven=list(map(int,input().split()))
pizza=list(map(int,input().split()))

for i in range(1,D):
    if oven[i-1]<oven[i]:
        oven[i]=oven[i-1]

ans=0
pizzaIndx=0
for d in range(D-1,-1,-1):
    if oven[d]>=pizza[pizzaIndx]:
        pizzaIndx+=1
        if pizzaIndx==N:
            ans=d+1
            break

print(ans)