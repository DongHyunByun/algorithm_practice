import sys

sys.setrecursionlimit(10**6)

L=[]
while(1):
    try:
        L.append(int(sys.stdin.readline()))
    except:
        break

def postorder(left,right):
    if left>right:
        return

    parent = L[left]
    mid = right+1
    for i in range(left+1,right+1):
        if parent < L[i]:
            mid = i
            break

    postorder(left+1, mid-1)
    postorder(mid,right)
    print(L[left])

postorder(0,len(L)-1)







