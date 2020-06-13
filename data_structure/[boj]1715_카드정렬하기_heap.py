import heapq
import sys


N=int(input())
pq=[]
for i in range(N):
    num=int(sys.stdin.readline().rstrip())
    heapq.heappush(pq,num)

ans=0
for i in range(N-1):
    a=heapq.heappop(pq)
    b=heapq.heappop(pq)
    mySum=a+b
    ans+=mySum
    heapq.heappush(pq,mySum)

print(ans)