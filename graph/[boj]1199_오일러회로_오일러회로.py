import sys
sys.setrecursionlimit(10**9)

N=int(input())
L=[]
for i in range(N):
    L.append(list(map(int,sys.stdin.readline().rstrip().split())))

edge=0
graph={}
for i in range(N):
    graph[i]=[]
    rowSum=0
    for j in range(N):
        for _ in range(L[i][j]):
            rowSum+=1
            graph[i].append(j)
    if rowSum%2==1:
        print(-1)
        sys.exit()
    else:
        edge+=rowSum
edge=edge//2

def dfs(nowNode):
    for conNode in graph[nowNode]:
        if L[nowNode][conNode]:
            L[nowNode][conNode]-=1
            L[conNode][nowNode]-=1
            dfs(conNode)
    print(nowNode+1,end=" ")

dfs(0)
