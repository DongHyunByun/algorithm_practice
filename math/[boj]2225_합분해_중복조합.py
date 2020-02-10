N,K=map(int,input().split())

dp=[[0 for j in range(N+K)] for i in range(N+K)]
for i in range(N+K):
    dp[i][0]=1

for i in range(1,N+K):
    for j in range(1,N+K):
        dp[i][j]=(dp[i-1][j-1]+dp[i-1][j])%1000000000

print(dp[N+K-1][K-1]%1000000000)