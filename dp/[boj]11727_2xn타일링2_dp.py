n=int(input())
dp=[1 for i in range(n+1)]
if n==1:
    print(1)
else:
    for i in range(2,n+1):
        dp[i]=(dp[i-1]+2*dp[i-2])%10007

    print(dp[n])