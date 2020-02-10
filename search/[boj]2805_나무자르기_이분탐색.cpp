def getSize(tempH):
    global h
    tree=0
    for i in range(N):
        temp=L[i]-tempH
        if (temp>0):
            tree+=temp

    # 많이짤랐으면
    if tree>=M:       
        if (tempH>h):
            h=tempH
        return True
    # 조금자랐으면
    else:
        return False

N,M=map(int,input().split())
L=list(map(int,input().split()))
h=0

left=1
right=2000000000
while(left<=right):
    mid=(left+right)//2
    if getSize(mid):
        left=mid+1
    else:
        right=mid-1

print(h)
