from collections import deque

n=int(input())
graph={}
dist=[-1 for i in range(n+1)]
for i in range(1,n+1):
    graph[i]=[]

a,b=map(int,input().split())
m=int(input())
for i in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

dist[a]=0
q=deque([a])
ans=-1

while(q):
    node=q.popleft()
    if node==b:
        ans=dist[node]
        break
    for toNode in graph[node]:
        if dist[toNode]==-1:
            q.append(toNode)
            dist[toNode]=dist[node]+1

print(ans)