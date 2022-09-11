from collections import deque

N,M = map(int,input().split())
max_load = 0
graph = {i:[] for i in range(1,N+1)}

for i in range(M):
    a,b,cost = map(int,input().split())
    graph[a].append((b,cost))
    graph[b].append((a,cost))
    max_load = max([cost,max_load])
x,y=map(int,input().split())

def bfs(load):
    '''
    무게가 load일 때 x->y 이동가능한지 여부
    '''
    q=deque([x])
    visited=[-1 for j in range(N+1)]
    visited[x]=1

    while(q):
        now_node = q.popleft()
        if now_node==y:
            return True
        for to_node,cost in graph[now_node]:
            if visited[to_node]==-1 and load<=cost:
                visited[to_node]=1
                q.append(to_node)

    return False

def upper_bound():
    bot = 1
    top = max_load+1

    while(bot<top):
        mid = (bot+top)//2
        # print(bot,mid,top)
        if bfs(mid):
            bot = mid+1
        else:
            top = mid

    return bot-1

print(upper_bound())