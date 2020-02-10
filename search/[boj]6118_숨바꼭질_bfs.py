from collections import deque
#입력
N,M=map(int,input().split())
graph={}
for i in range(N):
    graph[i+1]=[]
for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

#큐시작
longestNode=[]
longestDist=0
dist=[-1 for i in range(N+1)]
q=deque([1])
dist[1]=0
while(q):
    temp=q.popleft()
    for conNode in graph[temp]:
        if dist[conNode]==-1:
            dist[conNode]=dist[temp]+1
            q.append(conNode)
            if dist[conNode]>longestDist:
                longestDist=dist[conNode]
                longestNode=[conNode]
            elif dist[conNode]==longestDist:
                longestNode.append(conNode)

print(min(longestNode),longestDist,len(longestNode))