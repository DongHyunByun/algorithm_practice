import sys

K,N=map(int,input().split())
L=[]
minNum=9876543210
for i in range(K):
    temp=int(sys.stdin.readline().rstrip())
    if temp<minNum:
        minNum=temp
    L.append(temp)

def cut(size):
    a=0
    for i in L:
        a+=i//size
    return a

left=1
right=minNum

while(left<=right):
    mid=(left+right)//2
    #print(left,right,mid)
    num=cut(mid) #막대개수
    # 부족함, 더 짧게 잘라야함
    if num<N:
        right=mid-1
    # 너무 잘개자름, 더 길개 잘라야함
    elif num>N:
        left=mid+1
    else:
        ans=mid
        break
print(ans)
