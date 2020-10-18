import heapq
import math
INF=9876543210
n=int(input())
m=int(input())

edge={}
preL=[i for i in range(n+1)] #pre[x]=y : x도시 이전에 방문한도시는 y

for i in range(1,n+1):
    edge[i]=[]

for i in range(m):
    a,b,c=map(int,input().split())
    edge[a].append([b,c])

S,T=map(int,input().split())

pq=[[0,S,S]]
nodeDist=[INF for i in range(n+1)]
nodeDist[S]=0

while(pq):
    cost,preNode,node=heapq.heappop(pq)

    if cost>nodeDist[node]:
        continue



    if node==T:
        break

    for toNode,addedCost in edge[node]:
        newCost=addedCost+cost
        if newCost<nodeDist[toNode]:
            nodeDist[toNode]=newCost
            heapq.heappush(pq,[newCost,node,toNode])
            preL[toNode] = node

ans=[]
def dfs(a):
    ans.append(a)
    if a==S:
        ans.reverse()
        return
    else:
        dfs(preL[a])

dfs(T)

print(nodeDist[T])
print(len(ans))
print(*ans)

