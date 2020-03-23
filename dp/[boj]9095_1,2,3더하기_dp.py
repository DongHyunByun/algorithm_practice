T=int(input())
for t in range(T):
    n=int(input())
    dp = [1,1,2]
    size=3
    for i in range(n-2):
        dp.append(dp[size-3]+dp[size-2]+dp[size-1])
        size+=1
    print(dp[n])

