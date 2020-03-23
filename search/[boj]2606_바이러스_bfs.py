from collections import deque

N=int(input())
M=int(input())
graph={}
for i in range(N+1):
    graph[i]=[]
for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt=0
q=deque([1])
visited=[-1 for i in range(N+1)]
visited[1]=1
while(q):
    temp=q.popleft()
    for toNode in graph[temp]:
        if visited[toNode]==-1:
            visited[toNode]=1
            cnt+=1
            q.append(toNode)
print(cnt)
