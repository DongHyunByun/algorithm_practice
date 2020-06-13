N,M=map(int,input().split())
paint=[[0 for j in range(100)] for i in range(100)]

for _ in range(N):
    x1,y1,x2,y2=map(int,input().split())
    x1-=1
    y1-=1
    x2-=1
    y2-=1
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            paint[i][j]+=1


ans=0
for i in range(100):
    for j in range(100):
        if paint[i][j]>M:
            ans+=1
print(ans)