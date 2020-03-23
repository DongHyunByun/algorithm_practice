N=int(input())
L=list(map(int,input().split()))
isPossible=[0 for i in range(400001)]

ans=0
#숫자 하나씩 확인
for x in range(N):
    #있는지 확인
    for k in range(x):
        if isPossible[L[x]-L[k]+200000]:
            ans+=1
            break
    #숫자추가
    for j in range(x+1):
        isPossible[L[x]+L[j]+200000]=1
print(ans)