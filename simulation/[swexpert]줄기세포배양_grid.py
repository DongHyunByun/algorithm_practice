T=int(input())
dR=[0,0,-1,1]
dC=[1,-1,0,0]

for t in range(T):
    N,M,K=map(int,input().split())
    L=[]
    for i in range(N):
        L.append(list(map(int,input().split())))
    d={}

    for i in range(N):
        for j in range(M):
            if L[i][j]!=0:
                d[(i,j)]=[L[i][j],L[i][j]]
    for _ in range(K):
        toBreed = {}
        #번식할것 찾기
        for loc in d:
            if d[loc][1]==0:
                for k in range(4):
                    tempR=loc[0]+dR[k]
                    tempC=loc[1]+dC[k]
                    # 이미 있으면
                    if (tempR,tempC) in d:
                        continue
                    # 없으면
                    else:
                        #동시 번식이면
                        if (tempR,tempC) in toBreed:
                            toBreed[(tempR,tempC)]=max(toBreed[(tempR,tempC)],d[loc][0])
                        #단독 번식이면
                        else:
                            toBreed[(tempR,tempC)]=d[loc][0]

        #활성,비활성 -=1
        for loc in d:
            #죽지않은것만
            if d[loc][0]!=-1*d[loc][1]:
                d[loc][1]-=1
        #번식시작
        for breedLoc in toBreed:
            d[breedLoc]=[toBreed[breedLoc],toBreed[breedLoc]]
    ans=0
    for loc in d:
        #죽은거 빼고 카운트
        if d[loc][0]!=-1*d[loc][1]:
            ans+=1
    print("#%d %d"%(t+1,ans))