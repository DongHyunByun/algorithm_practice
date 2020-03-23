N=int(input())
dp=[0 for i in range(N+3)]
preNum=0
for i in range(3,N+3):
    nowNum=int(input())
    # i번째와 i-1번째를 마시는 경우
    a=preNum+nowNum+dp[i-3]
    # i번째를 마시고, i-1번째를 마시지 않는 경우
    b=nowNum+dp[i-2]
    # i번째를 마시지 않는 경우
    c=dp[i-1]

    dp[i]=max(a,b,c)
    preNum=nowNum
print(dp[N+2])