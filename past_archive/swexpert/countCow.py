def countLev(List,L,R) :
    return List[L-1:R].count(1),List[L-1:R].count(2),List[L-1:R].count(3)


for t in range(int(input())):
    cowNum=[]
    N,Q=map(int,input().split())
    for u in range(N):
        cowNum.append(int(input()))
    L=[0 for i in range(Q)]
    R=[0 for j in range(Q)]
    for v in range(Q):
        L[v],R[v]=map(int,input().split())

    print(f"#{t+1}")
    for w in range(Q):
        print(*countLev(cowNum,L[w],R[w]))

