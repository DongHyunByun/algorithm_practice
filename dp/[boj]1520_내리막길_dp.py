import sys
sys.setrecursionlimit(10**6)

dR=[0,0,-1,1]
dC=[1,-1,0,0]

def dfs(r,c):
    if r==M-1 and c==N-1:
        return 1
    if dp[r][c]!=-1:
        return dp[r][c]

    dp[r][c]=0
    for k in range(4):
        tempR=r+dR[k]
        tempC=c+dC[k]
        if 0<=tempR<M and 0<=tempC<N and L[r][c]>L[tempR][tempC]:
            dp[r][c]+=dfs(tempR,tempC)
    return dp[r][c]



M,N=map(int,input().split())
L=[]
for i in range(M):
    L.append(list(map(int,input().split())))

dp=[[-1 for j in range(N)] for i in range(M)]
print(dfs(0,0))
