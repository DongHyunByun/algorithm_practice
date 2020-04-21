from itertools import combinations
N,S=map(int,input().split())
L=list(map(int,input().split()))

ans=0
for j in range(1,N+1):
    comb=list(combinations([i for i in range(N)],j))
    for case in comb:
        sum=0
        for indx in case:
            sum+=L[indx]
        if sum==S:
            ans+=1
print(ans)



