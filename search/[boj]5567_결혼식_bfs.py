from collections import deque

n=int(input())
m=int(input())
graph={}
for i in range(n):
    graph[i+1]=[]

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

ans=0
visited=[0 for _ in range(n+1)]
q=deque([1])
visited[1]=1
while (q):
    temp=q.popleft()
    for node in graph[temp]:
        if not visited[node]:
            visited[node]=visited[temp]+1
            ans+=1
            if visited[node]!=3:
                q.append(node)

print(ans)