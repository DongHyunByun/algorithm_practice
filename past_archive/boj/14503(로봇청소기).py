from collections import deque
ans=0
N,M=map(int,input().split())
r,c,d=map(int,input().split())
L=[]
for i in range(N):
    L.append(list(map(int,input().split())))

dr=[-1,0,1,0]
dc=[0,1,0,-1]

backr=[1,0,-1,0]
backc=[0,-1,0,1]

if L[r][c]==0:
    L[r][c]=1
    ans+=1

while(1):
    tempD=d
    isClean=False
    for i in range(4):
        tempD-=1
        if tempD<0:
            tempD+=4
        tempR=r+dr[tempD]
        tempC=c+dc[tempD]
        if L[tempR][tempC]==0 :
            ans+=1
            isClean=True
            L[tempR][tempC]=3
            r=tempR
            c=tempC
            d=tempD
            break

    #청소실패
    if not isClean:
        r=r+backr[d]
        c=c+backc[d]
        if L[r][c]==1 :
            break



print(ans)