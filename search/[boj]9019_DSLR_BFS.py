from collections import deque
import sys
d=["D","S","L","R"]

def do(num,order):
    if order=="D":
        return (int(num)*2)%10000
    elif order=="S":
        return (int(num)-1)%10000
    elif order=="L":
        firstDigit = num // 1000
        return num % 1000 * 10 + firstDigit
    else:
        lastDigit = num % 10
        return num // 10 + 1000 * lastDigit

T=int(input())
for t in range(T):
    visited=[0 for i in range(10000)]
    A,B=map(int,sys.stdin.readline().rstrip().split())
    q=deque([[A,""]])
    visited[A]=1
    while(q):
        nowNum,sol=q.popleft()
        if nowNum==B:
            print(sol)
            break
        for k in range(4):
            newNum=do(nowNum,d[k])
            if not visited[newNum]:
                q.append([newNum,sol+d[k]])
                visited[newNum]=1