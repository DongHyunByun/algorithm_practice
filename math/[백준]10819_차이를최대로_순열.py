from itertools import permutations

N=int(input())
L=list(map(int,input().split()))

per=list(permutations([i for i in range(N)],N))

def myAdd(tup):

    myS=0
    for i in range(N-1):
        myS+=abs(L[tup[i]]-L[tup[i+1]])

    return myS

ans=0
for tup in per:
    temp=myAdd(tup)
    if temp>ans:
        ans=temp

print(ans)

