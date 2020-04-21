from collections import deque
N,S=map(int,input().split())
L=list(map(int,input().split()))

stack=deque([[0,0]])
ans=0
while stack:
    sum,indx=stack.pop()
    if indx==N:
        continue
    # 해당숫자를 선택하지 않는 경우
    stack.append([sum,indx+1])

    # 해당숫자를 선택하는 경우
    if sum+L[indx]==S:
        ans+=1
    stack.append([sum+L[indx],indx+1])

print(ans)
