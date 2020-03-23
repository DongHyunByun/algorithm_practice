from itertools import combinations
import sys

N=int(input())
L=[]
for i in range(N):
    a,b=map(int,sys.stdin.readline().strip().split())
    L.append([a,b])
ans=[1 for i in range(N)]
for i in range(N):
    for j in range(i+1,N):
        a1,b1=L[i]
        a2,b2=L[j]
        # 둘다 안좋으면 후보제외
        if (a1>=a2 and b1>=b2) :
            ans[i]=0
        elif (a1<=a2 and b1<=b2):
            ans[j]=0
print(sum(ans))


