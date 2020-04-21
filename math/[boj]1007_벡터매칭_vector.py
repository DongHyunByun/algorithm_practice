import sys
from itertools import combinations
import math

T=int(input())
for t in range(T):
    N=int(input())
    L=[]
    for i in range(N):
        L.append(list(map(int,sys.stdin.readline().rstrip().split())))
    #출발점
    comb=list(combinations([i for i in range(N)],N//2))
    ans=9876543210
    for starts in comb:
        fins=[i for i in range(N)]
        for s in starts:
            fins.remove(s)
        startX=sum([L[starts[i]][0] for i in range(N//2)])
        startY=sum([L[starts[i]][1] for i in range(N//2)])
        finX=sum([L[fins[i]][0] for i in range(N//2)])
        finY=sum([L[fins[i]][1] for i in range(N//2)])
        temp=math.sqrt((startX-finX)**2+(startY-finY)**2)
        if temp<ans:
            ans=temp
    print(ans)

