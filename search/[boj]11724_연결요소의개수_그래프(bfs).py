from collections import deque

N,M=map(int,input().split())
graph={}
for i in range(1,N+1):
    graph[i]=[]
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited=[0 for i in range(N+1)]

ans=0
for i in range(1,N+1):
    if visited[i]:
        continue
    ans+=1
    q = deque([i])
    while(q):
        temp=q.popleft()
        for toNode in graph[temp]:
            if not visited[toNode]:
                q.append(toNode)
                visited[toNode]=1
print(ans)