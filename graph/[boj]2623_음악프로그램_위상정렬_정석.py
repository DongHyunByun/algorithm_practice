from collections import deque

N,M=map(int,input().split())

inorder_graph = {i:set() for i in range(1,N+1)}
disorder_graph = {i:set() for i in range(1,N+1)}

for i in range(M):
    L = list(map(int,input().split()))[1:]
    size = len(L)
    for j in range(size-1):
        from_node = L[j]
        to_node = L[j+1]
        inorder_graph[from_node].add(to_node)
        disorder_graph[to_node].add(from_node)

q=deque([])
for i in range(1,N+1):
    if not disorder_graph[i]:
        q.append(i)

ans=[]
while(q):
    node = q.popleft()
    ans.append(node)

    for to_node in inorder_graph[node]:
        disorder_graph[to_node] = disorder_graph[to_node]-{node}
        if len(disorder_graph[to_node])==0:
            q.append(to_node)


if len(ans)==N:
    for i in ans:
        print(i)
else:
    print(0)

