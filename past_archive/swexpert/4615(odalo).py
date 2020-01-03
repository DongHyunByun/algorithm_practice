def makeOdalo(r,c,collor):
    pivot=[-1,0,1]
    active=[]
    for i in pivot:
        for j in pivot:
            if i==0 and j==0:
                L[r+i][c+j]=collor
            else:
                try:
                    if L[r+i][c+j]!=0 and L[r+i][c+j]!=collor:
                        active.append([i,j])
                except IndexError:
                    pass
    
    for i in range(len(active)):
        saveLoc=[]
        for j in range(1,8):
            try:
                if L[r+active[i][0]*j][c+active[i][1]*j]==0 or c+active[i][1]*j<0 or r+active[i][0]*j<0:
                    break
                elif L[r+active[i][0]*j][c+active[i][1]*j]==collor:
                    for k in saveLoc:
                        L[k[0]][k[1]]=collor
                    break
                elif L[r+active[i][0]*j][c+active[i][1]*j]*collor==2 :
                    saveLoc.append([r+active[i][0]*j,c+active[i][1]*j])
            except IndexError:
                break
   


for t in range(int(input())):
    N,M=map(int,input().split())
    L=[[0]*N for i in range(N)]
    n=N//2
    countB=0
    countW=0

    L[n][n]=2
    L[n-1][n-1]=2
    L[n][n-1]=1
    L[n-1][n]=1

    for i in range(M):
        x,y,rock=map(int,input().split())
        makeOdalo(y-1,x-1,rock)
    for i in L:
        countB+=i.count(1)
        countW+=i.count(2)
    print(f"#{t+1} {countB} {countW}")
        