N=int(input())
L=[]
for i in range(N):
    L.append(int(input()))

ans=0
L.sort()
for i in range(N):
    temp=L[i]*(N-i)
    ans=max(ans,temp)
print(ans)
