# 이거보셈 https://wootool.tistory.com/83
# 0은 왜 시간초과? https://www.acmicpc.net/board/view/14670
dR=[0,0,-1,1]
dC=[1,-1,0,0]
M,N=map(int,input().split())
L=[]
for i in range(M):
    L.append(list(map(int,input().split())))
visited=[[-1 for j in range(N)] for i in range(M)]
visited[M-1][N-1]=1

def dfs(point):
    '''
    for i in range(M):
        print(visited[i])
    '''
    r=point[0]
    c=point[1]

    if visited[r][c]!=-1:
        return visited[r][c]
    else:
        visited[r][c] = 0

    for k in range(4):
        tempR=r+dR[k]
        tempC=c+dC[k]
        if 0<=tempR<M and 0<=tempC<N and L[r][c]>L[tempR][tempC]:
            visited[r][c]+=dfs([tempR,tempC])
    return visited[r][c]

def main():
    dfs([0,0])
    '''
    for i in range(M):
        print(visited[i])
    '''
    print(visited[0][0])
main()


