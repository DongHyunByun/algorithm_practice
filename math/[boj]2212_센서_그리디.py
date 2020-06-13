
N=int(input())
K=int(input())
L=list(map(int,input().split()))
L=sorted(set(L))
size=len(L)

# 사이길이
between=[]
for i in range(size-1):
    between.append(L[i+1]-L[i])
between.sort(reverse=True)

ans=L[size-1]-L[0]
ans-=sum(between[:K-1])
print(ans)



