from itertools import combinations
N=int(input())
L=list(map(int,input().split()))
L.sort()
comb=list(combinations([i for i in range(N)],2))

def lowerBound(target):
    left=0
    right=N
    while(left<right):
        mid=(left+right)//2
        if target<=L[mid]:
            right=mid
        else:
            left=mid+1
    return right

# 좋은수중 가장 빠른 index에 1이 들어가있는 isGoodNumL 리스트
isGoodNumL=[0 for i in range(N)]
for a,b in comb:
    num=L[a]+L[b]
    if num>L[N-1]:
        continue
    numIndx=lowerBound(num)
    if numIndx!=a and numIndx!=b and L[numIndx]==num:
        isGoodNumL[numIndx]=1

# 중복된 좋은수 모두 찾기
goodNumL=[]
for i in range(N):
    if isGoodNumL[i]==1:
        goodNumL.append(L[i])
    else:
        if L[i] in goodNumL:
            isGoodNumL[i]=1


print(sum(isGoodNumL))