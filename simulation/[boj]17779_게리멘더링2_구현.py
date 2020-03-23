from collections import deque
dR=[0,0,-1,1]
dC=[1,-1,0,0]

N=int(input())
L=[]
for i in range(N):
    L.append(list(map(int,input().split())))

ans=9876543210
#시작점 찾기
for i in range(N):
    for j in range(N):
        minOfIJ=9876543210
        #d1,d2늘리기
        for d1 in range(1,N):
            for d2 in range(1,N):
                visited=[[0 for j in range(N)] for i in range(N)]
                # 한가지 케이스 시작
                if 0<=j-d1 and j+d2<=N-1 and i+d1+d2<=N-1:
                    # 경계선 만들기
                    for k in range(d1+1):
                        visited[i+k][j-k]=5
                        visited[i+d2+k][j+d2-k]=5
                    for k in range(d2+1):
                        visited[i+k][j+k]=5
                        visited[i+d1+k][j-d1+k]=5
                    #위쪽(1)
                    for k in range(N):
                        if visited[k][j]==5:
                            break
                        else:
                            visited[k][j]=1
                    #오른쪽(2)
                    for k in range(N):
                        if visited[i+d2][N-1-k]==5:
                            break
                        else:
                            visited[i+d2][N-1-k]=2
                    #아래쪽(4)
                    for k in range(N):
                        if visited[N-1-k][j+d2-d1]==5:
                            break
                        else:
                            visited[N-1-k][j+d2-d1]=4
                    #왼쪽(3)
                    for k in range(N):
                        if visited[i+d1][k]==5:
                            break
                        else:
                            visited[i+d1][k]=3

                    #큐로 채워넣기
                    startPoint=[[0,0],[0,N-1],[N-1,0],[N-1,N-1],[i+1,j]]
                    for gooNum in range(5):
                        start=list(startPoint[gooNum])
                        q=deque([start])
                        visited[start[0]][start[1]]=gooNum+1
                        while(q):
                            temp=q.popleft()
                            r=temp[0]
                            c=temp[1]
                            for k in range(4):
                                tempR=r+dR[k]
                                tempC=c+dC[k]
                                if 0<=tempR<N and 0<=tempC<N and visited[tempR][tempC]==0:
                                    visited[tempR][tempC]=gooNum+1
                                    q.append([tempR,tempC])

                    #점수계산
                    goo = [0, 0, 0, 0, 0]
                    for r in range(N):
                        for c in range(N):
                            goo[visited[r][c]-1]+=L[r][c]
                    sumOfD=max(goo)-min(goo)
                    if sumOfD<minOfIJ:
                        minOfIJ=sumOfD
                    '''
                    print(sumOfD)
                    print(goo)
                    for temp in range(N):
                        print(visited[temp])
                    print()
                    '''

                else:
                    continue
        if minOfIJ<ans:
            ans=minOfIJ
print(ans)
