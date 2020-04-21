from itertools import combinations
L=[i for i in range(10)]
comb=[]
for digit in range(1,11):
    temp=list(combinations(L,digit))
    for case in temp:
        A=sorted(case)
        num=0
        for i in range(digit):
            num+=(10**i)*A[i]
        comb.append(num)
comb.sort()
N=int(input())
try:
    print(comb[N-1])
except:
    print(-1)
