N,M=map(int,input().split())
L=[]
for i in range(N):
    L.append(list(map(int,input().split())))

dp=[[0 for j in range(M+1)] for i in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j]=L[i-1][j-1]+max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
print(dp[N][M])