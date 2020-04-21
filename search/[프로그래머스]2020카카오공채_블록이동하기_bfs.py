from collections import deque

dR=[0,-1,0,1]
dC=[1,0,-1,0]
reH=[2,3,0,1]
def solution(board):
    N=len(board)
    visited=[[[-1,-1,-1,-1] for j in range(N)] for i in range(N)]
    visited[0][0][0]=0
    q=deque([[0,0,0]])

    while(q):

        r1,c1,h=q.popleft() #기준점
        r2,c2=r1+dR[h],c1+dC[h] #연결점
        '''
        print(r1,c1,h)
        for i in visited:
            print(i)
        '''
        if ([r1,c1]==[N-1,N-1]) or ([r1,c1,h]==[N-1,N-2,0]) or ([r1,c1,h]==[N-2,N-1,3]):
            return visited[r1][c1][h]
        #상하좌우 검사
        for k in range(4):
            tempR1=r1+dR[k]
            tempC1=c1+dC[k]
            tempR2=r2+dR[k]
            tempC2=c2+dC[k]
            if 0<=tempR1<N and 0<=tempC1<N and 0<=tempR2<N and 0<=tempC2<N and board[tempR1][tempC1]==0 and board[tempR2][tempC2]==0 and visited[tempR1][tempC1][h]==-1:
                q.append([tempR1,tempC1,h])
                visited[tempR1][tempC1][h]=visited[r1][c1][h]+1
        #기준점 중심회전
        for k in [1,-1]:
            tempH=(h+k)%4
            tempR2=r1+dR[tempH]
            tempC2=c1+dC[tempH]
            if 0<=tempR2<N and 0<=tempC2<N and board[tempR2][tempC2]==0 and board[tempR2+dR[h]][tempC2+dC[h]]==0 and visited[r1][c1][tempH]==-1:
                q.append([r1,c1,tempH])
                visited[r1][c1][tempH]=visited[r1][c1][h]+1
        #연결점 중심회전
        for k in [1,-1]:
            tempH=(h+k)%4
            tempR1=r2+dR[tempH]
            tempC1=c2+dC[tempH]
            if 0<=tempR1<N and 0<=tempC1<N and board[tempR1][tempC1]==0 and board[r1+dR[tempH]][c1+dC[tempH]]==0 and visited[tempR1][tempC1][reH[tempH]]==-1:
                q.append([tempR1,tempC1,reH[tempH]])
                visited[tempR1][tempC1][reH[tempH]]=visited[r1][c1][h]+1




print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))
