from collections import deque

def second(L):
    return L[1]

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
    loc=deque([])
    field=[[0 for _ in range(c)] for _ in range(r)]
    for i in moleL:
        loc.append([top-i[1],i[0]-left])
        field[top-i[1]][i[0]-left]=[i[2],i[3]]
    while(len(loc)>=2):
        size=len(loc)
        # field밖 소멸
        for i in range(size):
            temp=loc.popleft()
            a=temp[0]
            b=temp[1]
            if a==0 and field[a][b][0]==0:
                field[a][b]=0
                continue
            if a==r-1 and field[a][b][0]==1:
                field[a][b]=0
                continue
            if b==0 and field[a][b][0]==2:
                field[a][b]=0
                continue
            if b==c-1 and field[a][b][0]==3:
                field[a][b]=0
                continue
            loc.append(list(temp))
        '''
        print("장외")
        print(loc)
        for i in field:
            print(i)
        '''

        # 이동전 만남 확인(직선)
        sortedLocR=sorted(loc)
        sortedLocC=sorted(loc,key=second)
        removeLR=[]
        removeLC=[]
        

        #세로로 만날때
        for i in range(len(sortedLocC)-1):
            if field[sortedLocC[i][0]][sortedLocC[i][1]]!=0 and sortedLocC[i][0]+1==sortedLocC[i+1][0] and sortedLocC[i][1]==sortedLocC[i+1][1] and field[sortedLocC[i][0]][sortedLocC[i][1]][0]==1 and field[sortedLocC[i+1][0]][sortedLocC[i+1][1]][0]==0 :
                removeLC.extend([i,i+1])
                ans+=field[sortedLocC[i][0]][sortedLocC[i][1]][1]+field[sortedLocC[i+1][0]][sortedLocC[i+1][1]][1]
                field[sortedLocC[i][0]][sortedLocC[i][1]]=0
                field[sortedLocC[i+1][0]][sortedLocC[i+1][1]]=0
        #가로로 만날때
        for i in range(len(sortedLocR)-1):
            if field[sortedLocR[i][0]][sortedLocR[i][1]]!=0 and sortedLocR[i][1]+1==sortedLocR[i+1][1] and sortedLocR[i][0]==sortedLocR[i+1][0] and field[sortedLocR[i][0]][sortedLocR[i][1]][0]==3 and field[sortedLocR[i+1][0]][sortedLocR[i+1][1]][0]==2 :
                removeLR.extend([i,i+1])
                ans+=field[sortedLocR[i][0]][sortedLocR[i][1]][1]+field[sortedLocR[i+1][0]][sortedLocR[i+1][1]][1]
                field[sortedLocR[i][0]][sortedLocR[i][1]]=0
                field[sortedLocR[i+1][0]][sortedLocR[i+1][1]]=0
        
        for i in removeLR:
            loc.remove(sortedLocR[i])
        for i in removeLC:
            loc.remove(sortedLocC[i])

        '''
        print("직선만남후")
        print(loc)
        for i in field:
            print(i)
        '''
        # 이동후 필드
        visitedL=[[[] for _ in range(c)] for _ in range(r)]
        for i in range(len(loc)):
            a=loc[i][0]
            b=loc[i][1]
            direc=field[a][b][0]
            if direc==0:
                visitedL[a-1][b].append(list(field[a][b]))
                loc[i][0]-=1
            elif direc==3:
                visitedL[a][b+1].append(list(field[a][b]))
                loc[i][1]+=1
            elif direc==1:
                visitedL[a+1][b].append(list(field[a][b]))
                loc[i][0]+=1
            else:
                visitedL[a][b-1].append(list(field[a][b]))
                loc[i][1]-=1
        
        #중복제거
        loc=deque(list(map(list,set(tuple(a) for a in loc))))
        field=[[0 for _ in range(c)] for _ in range(r)]
        
        for _ in range(len(loc)):
            temp=loc.popleft()
            a=temp[0]
            b=temp[1]
            if len(visitedL[a][b])==1:
                field[a][b]=list(visitedL[a][b][0])
                loc.append(temp)
            else:
                for k in visitedL[a][b]:
                    ans+=k[1]
        print(loc)

        '''
        print("이동후")
        print(loc)
        for i in field:
            print(i)
        print(ans)
        '''
    print(f"#{t+1} {ans}")

                 

