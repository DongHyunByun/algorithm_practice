N=int(input())
L=list(map(int,input().split()))
dp=list(L)
for i in range(1,N):
    for j in range(i):
        if L[j]<L[i] and dp[i]<dp[j]+L[i]:
            dp[i]=dp[j]+L[i]
print(max(dp))