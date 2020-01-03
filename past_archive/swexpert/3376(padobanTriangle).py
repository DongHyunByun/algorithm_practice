def maketri(L,num,N):
    if num!=N+1:
        L.append(L[num-1]+L[num-5])
        num+=1
        return maketri(L,num,N)


for t in range(int(input())):
    N=int(input())
    N-=1
    L=[1,1,1,2,2]
    if N<=2:
        ans=L[N]
    if N<=4:
        ans=L[N]
    else:
        maketri(L,5,N)
        ans=L[N]
    print(f"#{t+1} {ans}")
