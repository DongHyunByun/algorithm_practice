S,K=map(int,input().split())
num=S//K
remain=S%K
L=[num for i in range(K)]
for i in range(remain):
    L[i]+=1
ans=1
for i in range(K):
    ans*=L[i]
print(ans)