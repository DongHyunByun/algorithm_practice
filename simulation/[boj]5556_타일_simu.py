N=int(input())
K=int(input())

for k in range(K):
    r,c=map(int,input().split())
    r-=1
    c-=1
    if r>N//2:
        r=N-r-1

    if r<=c<=N-1-r:
        ans=r%3
    elif c<r:
        ans=c%3
    else:
        ans=(-c+N-1)%3
    print(ans+1)

