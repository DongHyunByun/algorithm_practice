n,k=map(int,input().split())
money=[]
INF=9876543210
for i in range(n):
    money.append(int(input()))
dp=[INF for i in range(k+1)]
dp[0]=0
for i in range(n):
    for j in range(k+1):
        if j-money[i]>=0:
            dp[j]=min(dp[j],dp[j-money[i]]+1)


if dp[k]==INF:
    print(-1)
else:
    print(dp[k])