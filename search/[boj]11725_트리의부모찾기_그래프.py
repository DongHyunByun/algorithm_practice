import sys
sys.setrecursionlimit(10**6)
N=int(input())

graph={i:[] for i in range(1,N+1)}
visited=[-1 for _ in range(N+1)]

for i in range(N-1):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

graph_parent={i:[] for i in range(1,N+1)}
visited[0]=visited[1]=1

def dfs(a):
    for son in graph[a]:
        if visited[son]==-1:
            visited[son] = 1
            graph_parent[son]=a
            dfs(son)

dfs(1)
for i in range(2,N+1):
    print(graph_parent[i])



