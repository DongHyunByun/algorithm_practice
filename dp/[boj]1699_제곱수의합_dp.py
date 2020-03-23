import math
INF=9876543210
N=int(input())
dp=[i for i in range(N+1)]
dp[0]=0
for i in range(1,N+1):
    j=1
    while(1):
        power=j**2
        if i<power:
            break
        else:
            dp[i]=min(dp[i],dp[i-power]+1)
            j+=1
print(dp[N])