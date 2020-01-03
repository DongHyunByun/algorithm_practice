def returnRC(L,N,i,j):
    row=1
    col=1
    L[i][j]=0
    try:
        while(L[i+row][j]!=0):
            row+=1
    except:
        pass

    try:
        while(L[i][j+col]!=0):
            col+=1
    except:
        pass

    for a in range(row):
        for b in range(col):
            L[i+a][j+b]=0
    return [row*col,row,col]



for t in range(int(input())):
    N=int(input())
    L=[]
    for i in range(N):
        L.append(list(map(int,input().split())))
    ans=[]

    for i in range(N):
        for j in range(N):
            if L[i][j]!=0:
                ans.append(returnRC(L,N,i,j))

    ans.sort()
 
    print(f"#{t+1} {len(ans)}",end=' ')
    for i in range(len(ans)):
        print(ans[i][1],ans[i][2],end=' ')
    print()

