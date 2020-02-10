from collections import deque
dR=[0,0,-1,1]
dC=[1,-1,0,0]
color=["R","G","B","P","Y"]
L=[]
for i in range(12):
    L.append(list(input()))

ans=0
while(1):
    isCrushed=False
    #부셔
    for i in range(12):
        for j in range(6):
            if L[i][j] in color:
                toCrushL=[[i,j]]
                nowColor=L[i][j]
                q=deque([[i,j]])
                while(q):
                    temp=q.popleft()
                    r=temp[0]
                    c=temp[1]
                    for k in range(4):
                        tempR=r+dR[k]
                        tempC=c+dC[k]
                        if 0<=tempR<12 and 0<=tempC<6 and L[tempR][tempC]==nowColor and [tempR,tempC] not in toCrushL:
                            toCrushL.append([tempR,tempC])
                            q.append([tempR,tempC])
                if len(toCrushL)>=4:
                    isCrushed=True
                    for r,c in toCrushL:
                        L[r][c]="X"
    if isCrushed:
        ans+=1
    else:
        break

    #내려
    for j in range(6):
        tempL=[]
        for i in range(12):
            if L[i][j]!="X":
                tempL.append(L[i][j])
        size=len(tempL)
        for i in range(12):
            if i<=11-size:
                L[i][j]="."
            else:
                L[i][j]=tempL[i-12+size]
    '''
    print(ans, "번쨰")
    for i in range(12):
        print(L[i])
    print()
    '''
print(ans)



