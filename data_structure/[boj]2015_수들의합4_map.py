N,K=map(int,input().split())
L=list(map(int,input().split()))

d={0:1}
cnt=0
S=0
for i in range(N):
    S += L[i]
    if S-K in d:
        cnt+=d[S-K]
    if S in d:
        d[S]+=1
    else:
        d[S]=1
        
print(cnt)



