import sys
N,M,K=map(int,input().split())

supply = list(map(int,input().split()))

graph={i:[] for i in range(1,N+1)}
edges = []
parent = {i:i for i in range(1,N+1)}

for i in range(M):
    u,v,w = map(int,sys.stdin.readline().rstrip().split())
    graph[u].append((v,w))
    graph[v].append((u,w))
    edges.append((w,u,v))

for i in range(len(supply)-1):
    graph[supply[i]].append((supply[i+1],0))
    graph[supply[i+1]].append((supply[i],0))
    edges.append((0,supply[i],supply[i+1]))

edges.sort()

def find(a):
    if parent[a]==a:
        return a
    else:
        parent[a]=find(parent[a])
        return parent[a]

def union(a,b):
    a_parent = find(a)
    b_parent = find(b)
    parent[b_parent]=a_parent


ans=0
for w, a, b in edges:
    if find(a)!=find(b):
        # print(w,a,b)
        ans+=w
        union(a,b)
print(ans)