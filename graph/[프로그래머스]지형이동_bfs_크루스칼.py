from collections import deque

dR = [0, 0, -1, 1]
dC = [-1, 1, 0, 0]
def solution(land, height):
    M=len(land)
    N=len(land[0])

    #영역 구하기
    cnt=0
    visited = [[-1 for j in range(N)] for i in range(M)]
    for i in range(M):
        for j in range(N):
            if visited[i][j]==-1:
                cnt+=1
                q=deque([[i,j]])
                visited[i][j]=cnt
                while(q):
                    r,c=q.popleft()
                    for k in range(4):
                        tempR=r+dR[k]
                        tempC=c+dC[k]
                        if 0<=tempR<M and 0<=tempC<N and visited[tempR][tempC]==-1 and abs(land[tempR][tempC]-land[r][c])<=height:
                            visited[tempR][tempC]=cnt
                            q.append([tempR,tempC])
    #영역별 최소거리 구하기
    edge=[]
    for i in range(M):
        for j in range(N):
            for k in range(4):
                tempR=i+dR[k]
                tempC=j+dC[k]
                if 0<=tempR<M and 0<=tempC<N and visited[i][j]!=visited[tempR][tempC]:
                    edge.append([abs(land[i][j]-land[tempR][tempC]),visited[i][j],visited[tempR][tempC]])
    edge.sort()
    #크루스칼
    parent=[i for i in range(cnt+1)]

    def find(a):
        if a==parent[a]:
            return a
        else:
            parent[a]=find(parent[a])
            return parent[a]
    def union(a,b):
        a=find(a)
        b=find(b)
        parent[b]=a

    size=len(edge)
    unionCnt=0
    cost=0
    for i in range(size):
        c,a,b=edge[i]
        if find(a)!=find(b):
            union(a,b)
            unionCnt+=1
            cost+=c
            if unionCnt==cnt-1:
                break
    return cost




print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]],3))

