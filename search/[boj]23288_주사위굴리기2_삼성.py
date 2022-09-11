from collections import deque

dR=[0,1,-1,0]
dC=[1,0,0,-1]

N,M,K=map(int,input().split())

L=[]
for i in range(N):
    L.append(list(map(int,input().split())))

dice = [0,1,2,3,4,5]

def rolling(d):
    if d==0:
        dice[2], dice[5], dice[3], dice[0] = dice[0], dice[2], dice[5], dice[3]
    elif d==1:
        dice[4], dice[5], dice[1], dice[0] = dice[0], dice[4], dice[5], dice[1]
    elif d==2:
        dice[1], dice[5], dice[4], dice[0] = dice[0], dice[1], dice[5], dice[4]
    elif d==3:
        dice[3], dice[5], dice[2], dice[0] = dice[0], dice[3], dice[5], dice[2]

def get_score(sR,sC):
    visited = [[-1 for j in range(M)] for i in range(N)]
    q=deque([(sR,sC)])
    visited[sR][sC]=1

    cnt=1
    num = L[sR][sC]
    while(q):
        r,c = q.popleft()
        for k in range(4):
            nextR=r+dR[k]
            nextC=c+dC[k]

            if 0<=nextR<N and 0<=nextC<M and visited[nextR][nextC]==-1 and L[nextR][nextC]==num:
                cnt+=1
                q.append((nextR,nextC))
                visited[nextR][nextC]=1

    return cnt*num

def get_direct(A,B,d):
    antiClockwise = {0:2,2:3,3:1,1:0}
    clockwise={2:0,0:1,1:3,3:2}

    if A>B:
        next_d = clockwise[d]
    elif A<B:
        next_d = antiClockwise[d]
    else:
        next_d = d

    return next_d

r=0
c=0
d=0

score_sum = 0
for _ in range(K):
    nextR=r+dR[d]
    nextC=c+dC[d]

    if 0<=nextR<N and 0<=nextC<M:
        r=nextR
        c=nextC
    else:
        d=3-d
        r=r+dR[d]
        c=c+dC[d]

    rolling(d) #1.굴리기
    score_sum += get_score(r,c) #2.점수획득
    d = get_direct(dice[5]+1,L[r][c],d) #3.이동방향결정


    # print("점수",score_sum)
    # print("방향",d)
    # print(r,c)
    # print("*", dice[1], "*")
    # print(dice[3], dice[0], dice[2])
    # print("*", dice[4], "*")
    # print("*", dice[5], "*")
    # print("================")

print(score_sum)