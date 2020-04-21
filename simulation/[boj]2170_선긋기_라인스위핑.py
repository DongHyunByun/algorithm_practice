import sys
N=int(input())
L=[]
for i in range(N):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    L.append([a,b])

L.sort()
preA,preB=L[0][0],L[0][1]
ans=preB-preA
for i in range(1,N):
    nowA,nowB=L[i][0],L[i][1]
    #겹치지 않는경우
    if preB<nowA:
        ans+=nowB-nowA
        preA, preB = nowA, nowB
    #살짝겹치는경우
    elif nowA<=preB<nowB:
        ans+=(nowB-preB)
        preA, preB = nowA, nowB



print(ans)


