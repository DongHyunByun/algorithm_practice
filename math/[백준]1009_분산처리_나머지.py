T=int(input())
L=[[0],[1],[2,4,8,6],[3,9,7,1],[4,6],[5],[6],[7,9,3,1],[8,4,2,6],[9,1]]
for i in range(T):
    a,b=input().split()
    b=int(b)
    indx=int(a[-1])
    size=len(L[indx])

    ans=L[indx][b%size-1]
    if ans==0:
        print(10)
    else:
        print(ans)
