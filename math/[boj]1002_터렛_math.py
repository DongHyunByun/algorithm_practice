import math

T=int(input())

for t in range(T):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    dist=math.sqrt((x1-x2)**2+(y1-y2)**2)
    if x1==x2 and y1==y2 and r1==r2:
        print(-1)
    elif r1+r2<dist or dist+min(r1,r2)<max(r1,r2):
        print(0)
    elif r1+r2==dist or max(r1,r2)-dist==min(r1,r2):
        print(1)
    else:
        print(2)