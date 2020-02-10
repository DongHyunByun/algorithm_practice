N=int(input())

myMap=[[0 for _ in range(101)] for _ in range(101)]

dR=[1,0,-1,0]
dC=[0,-1,0,1]

for i in range(N):
    r,c,d,g=map(int,input().split())
    curve=[[r,c],[r+dR[d],c+dC[d]]]
    axis=[r+dR[d],c+dC[d]]
    nextAxis=[0,0]
    # 기준에 1찍기
    for a,b in curve:
        myMap[a][b]=1

    # 세대시작
    for gen in range(g):
        # 기준제외 모든점 돌아서 찍힌다
        for j in range(len(curve)):
            # 회전
            newA=axis[0]+axis[1]-curve[j][1]
            newB=-axis[0]+axis[1]+curve[j][0]
            if (j==0):
                nextAxis[0]=newA
                nextAxis[1]=newB
            if not (newA==axis[0] and newB==axis[1]):
                curve.append([newA,newB])
                myMap[newA][newB]=1
        # 기준교체
        axis[0]=nextAxis[0]
        axis[1]=nextAxis[1]

ans=0
for i in range(100):
    for j in range(100):
        if (myMap[i][j] and myMap[i][j+1] and myMap[i+1][j] and myMap[i+1][j+1]):
            ans+=1
print(ans)