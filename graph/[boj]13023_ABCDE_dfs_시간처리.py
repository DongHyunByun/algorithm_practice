import sys
N,M = map(int,input().split())

graph={i:[] for i in range(N)}

for i in range(M):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

ans=0
visited = [0 for _ in range(N)]

def dfs(node,cnt):
    global ans
    # print(node,visited)
    if cnt==5:
        ans=1
        print(ans)
        sys.exit()
    else:
        for toNode in graph[node]:
            if visited[toNode]==0:
                visited[toNode]=1
                dfs(toNode,cnt+1)
                visited[toNode]=0

for i in range(N):
    visited[i] = 1
    dfs(i,1)
    visited[i] = 0
    if ans:
        break

print(ans)
