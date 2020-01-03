from collections import deque
N=int(input())
tL=[]

#끝나는시간, 시작시간, 돈
for i in range(N):
    T,P=map(int,input().split())
    tL.append([i+T,i+1,P])

tL.sort()
tL=deque(tL)
ans= [0]
for day in range(1,N+1):
    maxL=[]
    for i in range(len(tL)):
        temp=tL.popleft()
        if temp[0]==day:
            maxL.append(ans[temp[1]-1]+temp[2])
        else:
            tL.appendleft(temp)
            break

    if maxL :
        maxNum=max(maxL)
        if ans[len(ans)-1]>maxNum:
            ans.append(ans[len(ans)-1])
        else:
            ans.append(maxNum)
    else:
        ans.append(ans[len(ans)-1])
    

print(ans.pop())


