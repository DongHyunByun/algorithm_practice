N=int(input())
L=list(map(int,input().split()))
L.sort()
size=len(L)
if size%2==0:
    print(L[0]*L[size-1])
else:
    print(L[size//2]**2)