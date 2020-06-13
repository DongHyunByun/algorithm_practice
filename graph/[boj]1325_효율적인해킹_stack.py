import sys
from collections import deque

N,M=map(int,input().split())
graph={}
for i in range(1,N+1):
    graph[i]=[]
for i in range(M):
    A,B=map(int,sys.stdin.readline().rstrip().split())
    graph[B].append(A)

hackCom=0
ans=[]
for start in range(1,N+1):
    visited=[0 for i in range(N+1)]
    visited[start]=1
    stack = deque([start])
    cnt=1
    while(stack):
        nowNode=stack.pop()
        for toNode in graph[nowNode]:
            if visited[toNode]==0:
                visited[toNode]=1
                cnt+=1
                stack.append(toNode)
    #print(start,cnt)
    if cnt>hackCom:
        hackCom=cnt
        ans=[start]
    elif cnt==hackCom:
        ans.append(start)

print(*ans)
