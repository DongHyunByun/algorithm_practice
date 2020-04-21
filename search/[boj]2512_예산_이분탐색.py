N=int(input())
L=list(map(int,input().split()))
M=int(input())
L.sort()

def cal(sanghan):
    money=0
    for i in L:
        if i<=sanghan:
            money+=i
        else:
            money+=sanghan
    return money

# upperbound찾기
def binary(total):
    left=0
    right=L[N-1]+1
    while(left<right):
        mid=(right+left)//2
        temp=cal(mid)
        if total<temp:
            right=mid
        else:
            left=mid+1
    return right-1

print(binary(M))