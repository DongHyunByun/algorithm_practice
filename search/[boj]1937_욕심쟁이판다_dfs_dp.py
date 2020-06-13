import sys

sys.setrecursionlimit(10**6)
dR=[0,0,-1,1]
dC=[1,-1,0,0]
n=int(input())

L=[]
for i in range(n):
    L.append(list(map(int,input().split())))
dp=[[0 for j in range(n)] for i in range(n)]

def dfs(r,c):
    # [값이 존재하면]
    if dp[r][c]!=0:
        return dp[r][c]

    # [값이 존재안하면 탐색시작]
    nowValue=0
    for k in range(4):
        tempR=r+dR[k]
        tempC=c+dC[k]
        if 0<=tempR<n and 0<=tempC<n and L[tempR][tempC]>L[r][c]:
            nowValue=max(nowValue,dfs(tempR,tempC))
    dp[r][c]=nowValue+1
    return dp[r][c]

for i in range(n):
    for j in range(n):
        dfs(i,j)

print(max([max(dp[i]) for i in range(n)]))

