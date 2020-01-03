for t in range(int(input())):
    numStr=""
    s=0
    L=[]
    N=int(input())
    while len(L)!=N:
        L.extend(input().split())
    for i in L:
        numStr+=i
    while str(s) in numStr:
        s+=1
    print(f"#{t+1} {s}")
