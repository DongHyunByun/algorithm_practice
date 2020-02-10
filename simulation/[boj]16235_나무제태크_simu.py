dR=[-1,-1,-1,0,0,1,1,1]
dC=[-1,0,1,-1,1,-1,0,1]

if __name__=="__main__":
    N,M,K=map(int,input().split())

    add=[]
    for i in range(N):
        add.append(list(map(int,input().split())))

    treeL=[[[] for j in range(N)] for i in range(N)]
    for i in range(M):
        x,y,z=map(int,input().split())
        treeL[x-1][y-1].append(z)

    for i in range(N):
        for j in range(N):
            treeL[i][j].sort()

    source=[[5 for j in range(N)] for i in range(N)]

    for _ in range(K):
        '''
        #확인
        print(_,"번째")
        for i in range(N):
            print(treeL[i])
        for i in range(N):
            print(source[i])
        '''
        # 봄 여름
        for i in range(N):
            for j in range(N):
                for treeIndx,treeAge in enumerate(treeL[i][j]):
                    if source[i][j]>=treeAge:
                        treeL[i][j][treeIndx]+=1
                        source[i][j]-=treeAge
                    # treeIndx부터 끝까지 양분못받음
                    else:
                        for _ in range(len(treeL[i][j])-treeIndx):
                            temp=treeL[i][j].pop()
                            source[i][j]+=temp//2
        # 가을, 겨울
        for i in range(N):
            for j in range(N):
                # 가울
                for treeIndx,treeAge in enumerate(treeL[i][j]):
                    # 5의 배수이면
                    if treeAge%5==0:
                        for k in range(8):
                            tempI=i+dR[k]
                            tempJ=j+dC[k]
                            if 0<=tempI<N and 0<=tempJ<N :
                                treeL[tempI][tempJ].insert(0,1)
                # 겨울
                source[i][j]+=add[i][j]
    '''
    print(K, "번째")
    for i in range(N):
        print(treeL[i])
    '''

    ans=0
    for i in range(N):
        for j in range(N):
            ans+=len(treeL[i][j])
    print(ans)


