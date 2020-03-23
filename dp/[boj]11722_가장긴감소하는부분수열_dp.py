N=int(input())
L=list(map(int,input().split()))
dp=[1 for i in range(N)]
for i in range(N):
    for j in range(i):
        if L[i]<L[j] and dp[i]<dp[j]+1:
            dp[i]=dp[j]+1
print(max(dp))