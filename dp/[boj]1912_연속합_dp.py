n=int(input())
L=list(map(int,input().split()))
dp=[0 for i in range(n)]
nowSum=0
for i in range(n):
    nowSum=max(nowSum+L[i],L[i])
    dp[i]=nowSum
print(max(dp))