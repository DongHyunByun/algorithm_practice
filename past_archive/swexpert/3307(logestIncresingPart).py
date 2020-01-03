for t in range(int(input())):
    
    N=int(input())
    dp=[1]*N
    L=list(map(int,input().split()))
    for i in range(1,len(L)):
        for j in range(i):
            if L[j]<L[i]:
                dp[i]=max(dp[i],dp[j]+1)
    print(f"#{t+1} {max(dp)}")
            
