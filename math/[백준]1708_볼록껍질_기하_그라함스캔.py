import sys
import math
from collections import deque

def dist(x,y):
    return math.sqrt((sX-x)**2+(sY-y)**2)

def CP(a,b):
    a1,a2=a
    b1,b2=b
    return a1*b2-a2*b1

def minusL(L1,L2):
    return [L1[0]-L2[0],L1[1]-L2[1]]

N=int(input())
L=[]
for i in range(N):
    x,y=map(int,sys.stdin.readline().rstrip().split())
    L.append([0,0,y,x])

# 기준점잡기
L.sort()
sY,sX=L[0][2],L[0][3]
del L[0]

# cos으로 각도가 작은것부터 정렬
for i in range(N-1):
    tempD=dist(L[i][3],L[i][2])
    L[i][0]=-round((L[i][3]-sX)/tempD,10)
    L[i][1]=tempD
L.sort()

# 껍질 포함여부 확인시작
stack=deque([[sX,sY]])
stack.append([L[0][3],L[0][2]])
del L[0]

for i in range(N-2):
    while(1):
        #print(stack)
        if len(stack)<2:
            stack.append([L[i][3],L[i][2]])
            break
        p2=stack.pop()
        p1=stack.pop()
        #print(p1,p2)
        vec=minusL(p2,p1)
        p3=[L[i][3],L[i][2]]
        vec2=minusL(p3,p1)
        cp=CP(vec,vec2)
        # 왼쪽에 있으면?
        if cp>0:
            stack.append(p1)
            stack.append(p2)
            stack.append(p3)
            break
        # 겹치면?
        elif cp==0:
            stack.append(p1)
            stack.append(p3)
            break
        # 오른쪽에 있으면?
        else:
            stack.append(p1)


#print(stack)
print(len(stack))
