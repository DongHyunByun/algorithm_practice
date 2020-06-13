from collections import deque
import heapq

N=int(input())
L=[]
for i in range(N):
    L.append(list(map(int,input().split())))

# t시간까지 해야되는거 pq에추가
def addPQ(t):
    while(L):
        dead,cup=L.pop()
        if dead==t:
            heapq.heappush(cupPQ,-1*cup)
        else:
            L.append([dead,cup])
            return

L.sort()
L=deque(L)
cupPQ=[]
ans=0
addPQ(N)
for i in range(N-1,-1,-1):
    # 현재 해야되는거(컵라면가장많은거) 하기
    if cupPQ:
        ans+=-1*heapq.heappop(cupPQ)
    # 후보 추가
    addPQ(i)


print(ans)