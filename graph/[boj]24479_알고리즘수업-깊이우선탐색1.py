import sys
sys.setrecursionlimit(10**5)

N,M,R = map(int,input().split())

g = {i:[] for i in range(1,N+1)}

for _ in range(M):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

for i in range(1,N+1):
    g[i].sort()


visited = [-1 for j in range(N+1)]
def dfs(a):
    for next_node in g[a]:
        if visited[next_node]==-1:
            visit_order.append(next_node)
            visited[next_node]=1
            dfs(next_node)

visit_order = [0,R]
visited[R]=1
dfs(R)

ans_dict = {i:0 for i in range(1,N+1)}
for order,node in enumerate(visit_order):
    if order==0:
        continue
    ans_dict[node]=order

# print(ans_dict)
for node in ans_dict:
    print(ans_dict[node])

