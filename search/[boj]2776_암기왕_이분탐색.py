import sys

T=int(input())

def binary_search(target):
    bot = 0
    top = a

    while(bot<top):
        mid = (bot+top)//2
        # print(bot,mid,top)
        if L1[mid]<target:
            bot=mid+1
        else:
            top=mid

    if bot<a and L1[bot]==target:
        return 1
    else:
        return 0

for _ in range(T):
    a=int(input())
    L1=list(map(int,sys.stdin.readline().split()))
    L1.sort()

    b=int(input())
    L2=list(map(int,sys.stdin.readline().split()))

    for num in L2:
        print(binary_search(num))
