n,m=map(int,input().split())

dp=[[0 for j in range(n+1)] for i in range(n+1)]
for i in range(n+1):
    dp[i][0]=1

for i in range(1,n+1):
    for j in range(1,i+1):
        dp[i][j]=dp[i-1][j-1]+dp[i-1][j]

print(dp[n][m])