R,C=map(int,input().split())

# 3면이상이 바다면 True, 아니면 False
def cheak(r,c):
    dR=[0,0,-1,1]
    dC=[1,-1,0,0]
    #땅의 개수
    cnt=0
    for i in range(4):
        tempR=r+dR[i]
        tempC=c+dC[i]
        if 0<=tempR<R and 0<=tempC<C:
            if map[tempR][tempC]=="X":
                cnt+=1
                if cnt==2:
                    return False
    return True

cheakL=[[0 for _ in range(C)] for _ in range(R)]
map=[]
for _ in range(R):
    map.append(list(input()))

for i in range(R):
    for j in range(C):
        if map[i][j]=="X":
            if cheak(i,j):
                continue
            cheakL[i][j]=1

top=0
for i in range(R):
    if 1 in cheakL[i]:
        top=i
        break
bottom=R-1
for i in range(R-1,-1,-1):
    if 1 in cheakL[i]:
        bottom=i
        break
left=0
for j in range(C):
    isOne=False
    for i in range(R):
        if cheakL[i][j]==1:
            isOne=True
            break
    if isOne:
        left=j
        break

right=0
for j in range(C-1,-1,-1):
    isOne=False
    for i in range(R):
        if cheakL[i][j]==1:
            isOne=True
            break
    if isOne:
        right=j
        break

for i in range(top,bottom+1):
    for j in range(left,right+1):
        if cheakL[i][j]==0:
            print(".",end="")
        else:
            print("X",end="")
    print()


