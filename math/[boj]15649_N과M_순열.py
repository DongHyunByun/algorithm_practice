from itertools import permutations

N,M=map(int,input().split())
L=[i for i in range(1,N+1)]

for A in sorted(list(permutations(L,M))):
    for i in range(M):
        print(A[i],end=" ")
    print()

