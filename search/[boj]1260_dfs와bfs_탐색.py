import queue
import sys
sys.setrecursionlimit(10**6)

N,M,V=map(int,input().split())
graph={}

for i in range(M):
    a,b=map(int,input().split())
    if a in graph:
        graph[a].append(b)
    else:
        graph[a]=[b]
    if b in graph:
        graph[b].append(a)
    else:
        graph[b]=[a]
# 작은수부터 나오게 sorting
for i in graph:
    graph[i].sort()

def dfs(V):
    print(V,end=" ")
    visitedL[V]=1
    if V in graph:
        for node in graph[V]:
            if not visitedL[node]:
                dfs(node)

def bfs(V):
    q=queue.Queue()
    q.put(V)
    visitedL[V] = 1
    while(not q.empty()):
        temp=q.get()
        print(temp,end=" ")
        if temp in graph:
            for node in graph[temp]:
                if not visitedL[node]:
                    q.put(node)
                    visitedL[node]=1



visitedL=[0 for _ in range(N+1)]
dfs(V)
print()

visitedL=[0 for _ in range(N+1)]
bfs(V)
print()