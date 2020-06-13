import heapq
import sys
from collections import deque

N=int(input())
point=[]
for i in range(N):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    point.append([a,b])
L,P=map(int,input().split())

point.sort()
point=deque(point)
oil=P
ans=0
shopPQ=[]
while(1):
    # 마을도착하면 그만
    if oil>=L:
        break
    # 도착못하면 주유소에 서기
    else:
        # 후보주유소 추가
        while(point):
            loc,addedOil=point.popleft()
            if loc<=oil:
                heapq.heappush(shopPQ,-1*addedOil)
            else:
                point.appendleft([loc,addedOil])
                break
        # 범위안에 최대충전량 더하기
        if shopPQ:
            added=heapq.heappop(shopPQ)
            added*=-1
            ans+=1
            oil+=added
        else:
            ans=-1
            break

print(ans)