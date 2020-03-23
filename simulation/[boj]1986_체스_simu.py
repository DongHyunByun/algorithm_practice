kdR=[-1,-1,-2,-2,1,1,2,2]
kdC=[2,-2,1,-1,2,-2,1,-1]
qdR=[-1,-1,-1,0,0,1,1,1]
qdC=[-1,0,1,-1,1,-1,0,1]

def knightMove(r,c,L):
    #나이트 위치도 제외
    safe[r][c]=0
    #나이트가 움직일 수 잇는 위치도 제외
    for k in range(8):
        tempR=r+kdR[k]
        tempC=c+kdC[k]
        if 0<=tempR<n and 0<=tempC<m:
            safe[tempR][tempC]=0

def queenMove(r,c,L):
    #여왕위치 제외
    safe[r][c]=0
    #여왕 움직일 수 있는 위치 제외
    for k in range(8):
        tempR=r+qdR[k]
        tempC=c+qdC[k]
        while(1):
            if 0<=tempR<n and 0<=tempC<m and myMap[tempR][tempC]==0:
                safe[tempR][tempC]=0
                tempR+=qdR[k]
                tempC+=qdC[k]
            else:
                break

n,m=map(int,input().split())
queen=list(map(int,input().split()))
queenNum=queen.pop(0)
knight=list(map(int,input().split()))
knightNum=knight.pop(0)
pawn=list(map(int,input().split()))
pawnNum=pawn.pop(0)

safe=[[1 for j in range(m)] for i in range(n)]
myMap=[[0 for j in range(m)] for i in range(n)]
#퀸표시
for i in range(0,2*queenNum,2):
    myMap[queen[i]-1][queen[i+1]-1]="q"
#나이트표시
for i in range(0,2*knightNum,2):
    myMap[knight[i]-1][knight[i+1]-1]="k"
#폰표시
for i in range(0,2*pawnNum,2):
    myMap[pawn[i]-1][pawn[i+1]-1]="p"

for i in range(0,2*queenNum,2):
    queenMove(queen[i]-1,queen[i+1]-1,safe)
for i in range(0,2*knightNum,2):
    knightMove(knight[i]-1,knight[i+1]-1,safe)
for i in range(0,2*pawnNum,2):
    safe[pawn[i]-1][pawn[i+1]-1]=0
'''
for i in range(n):
    print(safe[i])
'''

ans=0
for i in range(n):
    ans+=sum(safe[i])
print(ans)

