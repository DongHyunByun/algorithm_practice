import sys
import math
T=int(input())
for t in range(T):
    x,y=map(int,sys.stdin.readline().rstrip().split())
    num=y-x
    sqrtNum=math.sqrt(num)
    intSqrtNum=int(sqrtNum)
    if sqrtNum==intSqrtNum:
        print(2*intSqrtNum-1)
    elif num<=intSqrtNum**2+intSqrtNum:
        print(2*intSqrtNum)
    else:
        print(2*intSqrtNum+1)
