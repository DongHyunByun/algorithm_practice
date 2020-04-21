N=int(input())
card=list(map(int,input().split()))
card.sort()
M=int(input())
L=list(map(int,input().split()))
size=len(card)

def binary(num):
    left=0
    right=size-1
    while(left<=right):
        mid=(left+right)//2
        if card[mid]<num:
            left=mid+1
        elif card[mid]>num:
            right=mid-1
        else:
            return 1
    return 0

for i in L:
    print(binary(i),end=" ")