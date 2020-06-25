import sys

N=int(input())
L=[]
for i in range(N):
    L.append(int(sys.stdin.readline().rstrip()))
L.sort()

ans=0
for i in range(1,N+1):
    ans+=abs(L[i-1]-i)

print(ans)