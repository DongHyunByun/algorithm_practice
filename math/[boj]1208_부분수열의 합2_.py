from collections import deque
N,S=map(int,input().split())
L=list(map(int,input().split()))
halfSize=N//2
leftDict={}

def dfsLeft():
    stack = deque([[0, 0]])
    ans = 0
    while stack:
        sum, indx = stack.pop()
        if indx == halfSize:
            continue
        # 해당숫자를 선택하지 않는 경우
        stack.append([sum, indx + 1])
        # 해당숫자를 선택하는 경우
        if sum+L[indx] in leftDict:
            leftDict[sum+L[indx]]+=1
        else:
            leftDict[sum+L[indx]]=1
        stack.append([sum + L[indx], indx + 1])

def dfsRight():
    global ans
    stack=deque([[0,halfSize]])
    while stack:
        sum,indx=stack.pop()
        if indx==N:
            continue
        # 해당숫자를 선택하지 않는경우
        stack.append([sum,indx+1])
        # 해당숫자를 선택하는 경우
        temp=sum+L[indx]
        if S-temp in leftDict:
            ans+=leftDict[S-temp]
        if temp==S:  #오른쪽만으로 만들기
            ans+=1
        stack.append([temp,indx+1])

ans=0
dfsLeft()
dfsRight()
if S in leftDict:  #왼쪽만으로 만들기
    ans+=leftDict[S]
print(ans)
