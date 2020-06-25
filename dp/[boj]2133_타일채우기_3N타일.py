N=int(input())
dp=[0 for i in range(N+1)]
dp[0]=1

for i in range(2,N+1):
    if i%2!=0:
        continue
    dp[i]+=dp[i-2]*3
    for j in range(4,i+1,2):
        dp[i]+=dp[i-j]*2

print(dp[N])