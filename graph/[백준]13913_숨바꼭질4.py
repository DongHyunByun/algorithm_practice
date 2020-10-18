import sys
from collections import deque
sys.setrecursionlimit(10**6)

maxNum=100000
N,K=map(int,input().split())

# [걸린시간, 이전노드]
visited=[[-1,-1] for i in range(maxNum+1)]
visited[N]=[0,N]
q=deque([N])

def dfs(loc):
    if loc==N:
        ans.append(loc)
        return
    else:
        ans.append(loc)
        dfs(visited[loc][1])


while(q):
    loc=q.popleft()
    if loc==K:
        print(visited[loc][0])
        break

    # 앞으로이동
    if loc-1!=-1 and visited[loc-1][0]==-1:
        visited[loc-1][0]=visited[loc][0]+1
        visited[loc-1][1]=loc
        q.append(loc-1)

    # 뒤로이동
    if loc+1!=maxNum+1 and visited[loc+1][0]==-1:
        visited[loc+1][0]=visited[loc][0]+1
        visited[loc+1][1]=loc
        q.append(loc+1)

    # 순간이동
    tempLoc=loc*2
    if tempLoc<=maxNum and visited[tempLoc][0]==-1:
        visited[tempLoc][0]=visited[loc][0]+1
        visited[tempLoc][1]=loc
        q.append(tempLoc)

ans=[]
dfs(K)
print(*list(reversed(ans)))