N=int(input())

dp=[[0 for i in range(10+N)] for _ in range(10+N)]
dp[0][0]=1
for i in range(10+N):
    for j in range(i+1):
        if j==0:
            dp[i][j]=1
        else:
            dp[i][j]=(dp[i-1][j]+dp[i-1][j-1])%10007

print(dp[9+N][N]%10007)
