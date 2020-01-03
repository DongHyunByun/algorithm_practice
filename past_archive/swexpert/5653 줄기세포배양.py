for t in range(int(input())):
    N=int(input())
    moleL=[]
    for i in range(N):
        moleL.append(list(map(int,input().split())))
    top=moleL[0][1]
    bottom=moleL[0][1]
    right=moleL[0][0]
    left=moleL[0][0]

    for i in moleL:
        if i[1]>top:
            top=i[1]
        if i[1]<bottom:
            bottom=i[1]
        if i[0]<left:
            left=i[0]
        if i[0]>right:
            right=i[0]
    ans=0
    c=right-left+1
    r=top-bottom+1
    field=[[0 for _ in range(c)] for _ in range(r)]
    for i in moleL:
        field[top-i[1]][i[0]-left]=[i[2],i[3]]
    
    while(1):
        # field밖 소멸
        for j in range(c):
            if field[0][j]!=0 and field[0][j][0]==0:
                field[0][j]=0
        for i in range(r):
            if field[i][0]!=0 and field[i][0][0]==2:
                field[i][0]=0
            if field[i][c-1]!=0 and field[i][c-1][0]==3:
                field[i][c-1]=0
        for j in range(c):
            if field[r-1][j]!=0 and field[r-1][j][0]==1:
                field[r-1][j]=0
        # 이동전 만남 확인(직선)
        for i in range(r-1):
            for j in range(c-1):
                if field[i][j]!=0 and field[i][j][0]==3 and field[i][j+1]!=0 and field[i][j+1][0]==2:
                    ans+=field[i][j][1]+field[i][j+1][1]
                    field[i][j]=0
                    filed[i][j+1]=0
                if field[i][j]!=0 and field[i][j][0]==1 and field[i+1][j]!=0 and field[i+1][j][0]==0:
                    ans+=field[i][j][1]+field[i+1][j][1]
                    field[i][j]=0
                    filed[i+1][j]=0
        # 이동후 필드
        
        visitedL=[[[] for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                temp=field[i][j]
                if temp!=0:
                    if temp[0]==0:
                        visitedL[i-1][j].append(temp)
                    elif temp[0]==3:
                        visitedL[i][j+1].append(temp)
                    elif temp[0]==1:
                        visitedL[i+1][j].append(temp)
                    else:
                        visitedL[i][j-1].append(temp)
        
        for i in range(r):
            for j in range(c):
                if visitedL!=0:
                    if len(visitedL[i][j])==1:
                        field[i][j]=list(visitedL[i][j][0])
                    else:
                        for i in visitedL[i][j]:
                            ans+=i[1]
                        field[i][j]=0
                else:
                    fieldL[i][j]=0
        
        isContinue=False
        for i in range(r):
            for j in range(c):
                if field[i][j]!=0:
                    isContinue=True
                    break
            if isContinue:
                break

        if isContinue:
            continue
        break
    print(f"#{t+1} {ans}")

                 

