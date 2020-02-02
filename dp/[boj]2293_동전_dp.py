N,K=map(int,input().split())
coin=[]
for i in range(N):
    coin.append(int(input()))

dp=[0 for money in range(K+1)]
dp[0]=1

for co in range(N):
    for j in range(1,K+1):
        if (j-coin[co]>=0):
            dp[j] = dp[j] + dp[j - coin[co]]
print(dp[K])