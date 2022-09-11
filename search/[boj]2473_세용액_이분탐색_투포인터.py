import sys

N=int(input())
L=list(map(int,sys.stdin.readline().split()))
L.sort()

import sys

N=int(input())
L=list(map(int,sys.stdin.readline().split()))
L.sort()


min_sum = 9876543210
ans=[0,0,0]

for i in range(N-2):
    first = i
    left = i+1
    right = N-1
    while(left<right):
        now_sum = L[first]+L[left]+L[right]
        # print(left,right,now_sum)
        if abs(now_sum)<abs(min_sum):
            min_sum = now_sum
            ans[0]=first
            ans[1]=left
            ans[2]=right

        if now_sum<0:
            left+=1
        elif now_sum>0:
            right-=1
        else:
            break

print(L[ans[0]],L[ans[1]],L[ans[2]])
min_sum = 9876543210
ans=[0,0,0]

for i in range(N-2):
    first = i
    left = i+1
    right = N-1
    while(left<right):
        now_sum = L[first]+L[left]+L[right]
        # print(left,right,now_sum)
        if abs(now_sum)<abs(min_sum):
            min_sum = now_sum
            ans[0]=first
            ans[1]=left
            ans[2]=right

        if now_sum<0:
            left+=1
        elif now_sum>0:
            right-=1
        else:
            break

print(L[ans[0]],L[ans[1]],L[ans[2]])