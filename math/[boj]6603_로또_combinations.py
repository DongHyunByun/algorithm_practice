from itertools import combinations
while True:
    L=list(map(int,input().split()))
    N=L.pop(0)
    if N==0:
        break
    else:
        com=list(combinations(L,6))
        for i in com:
            print(*i)
        print()