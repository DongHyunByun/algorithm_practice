N=int(input())
card=list(map(int,input().split()))
card.sort()
M=int(input())
L=list(map(int,input().split()))

# target<=L[i]인 가장 작은 i를 찾음
def leftBinary(target):
    left=0
    right=N
    while(left<right):
        mid=(left+right)//2
        if target<=card[mid]:
            right=mid
        else:
            left=mid+1
    return right

# target<L[i]인 가장 작은 i를 찾음
def rightBinary(target):
    left=0
    right=N
    while(left<right):
        mid=(left+right)//2
        if target<card[mid]:
            right=mid
        else:
            left=mid+1
    return right

for i in L:
    r=rightBinary(i)
    l=leftBinary(i)
    print(r-l,end=" ")