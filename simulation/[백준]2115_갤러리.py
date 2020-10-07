N,M=map(int,input().split())

L=[]
for i in range(N):
    temp=list(input())
    L.append(temp)

wall=[[[0,0,0,0] for j in range(M)] for i in range(N)]

ans=0

# 행검사
for i in range(1,N-1):
    for j in range(1,M-2):
        if L[i][j]=="." and L[i][j+1]==".":
            # 위쪽확인
            if L[i-1][j]=="X" and L[i-1][j+1]=="X" and wall[i][j][0]==0 and wall[i][j+1][0]==0:
                ans+=1
                wall[i][j][0]=wall[i][j+1][0]=1
            # 아래쪽확인
            if L[i+1][j]=="X" and L[i+1][j+1]=="X" and wall[i][j][2]==0 and wall[i][j+1][2]==0:
                ans+=1
                wall[i][j][2]=wall[i][j+1][2]=1

# 열
for j in range(1,M-1):
    for i in range(1,N-2):
        if L[i][j]=="." and L[i+1][j]==".":
            # 왼쪽확인
            if L[i][j-1]=="X" and L[i+1][j-1]=="X" and wall[i][j][1]==0 and wall[i+1][j][1]==0:
                ans+=1
                wall[i][j][1]=wall[i+1][j][1]=1
            # 오른쪽확
            if L[i][j+1]=="X" and L[i+1][j+1]=="X" and wall[i][j][3]==0 and wall[i+1][j][3]==0:
                ans+=1
                wall[i][j][3]=wall[i+1][j][3]=1

print(ans)



