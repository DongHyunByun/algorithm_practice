from collections import deque
N=int(input())
K=int(input())
def minus(num):
    return num-1
apple=[]
for i in range(K):
    apple.append(list(map(minus,map(int,input().split()))))
L=int(input())
drec=deque([])
for i in range(L):
    a,b=input().split()
    drec.append([int(a)+1,b])

game=[[0 for i in range(N)] for j in range(N)]
for i in apple:
    game[i[0]][i[1]]=2
game[0][0]=1
headR=0
headC=0
forward=1
time=0
tailR=0
tailC=0


direcL=[[4 for _ in range(N)] for _ in range(N)]


while(1):
    time+=1
    #방향결정
    if drec:
        if time==drec[0][0]:
            d=drec.popleft()[1]
            if d=="D":
                forward=(forward+1)%4
            else:
                forward=(forward+3)%4
    direcL[headR][headC]=forward
    #늘어난다
    isEat=False
    #위
    if forward==0:
        headR-=1
        if headR==-1 or game[headR][headC]==1:
            break
        else:
            #사과먹음
            if game[headR][headC]==2:
                isEat=True
            game[headR][headC]=1
    #오른쪽
    if forward==1:
        headC+=1
        if headC==N or game[headR][headC]==1:
            break
        else:
            #사과먹음
            if game[headR][headC]==2:
                isEat=True
            game[headR][headC]=1
    #아래
    if forward==2:
        headR+=1
        if headR==N or game[headR][headC]==1:
            break
        else:
            #사과먹음
            if game[headR][headC]==2:
                isEat=True
            game[headR][headC]=1
    #오른쪽
    if forward==3:
        headC-=1
        if headC==-1 or game[headR][headC]==1:
            break
        else:
            #사과먹음
            if game[headR][headC]==2:
                isEat=True
            game[headR][headC]=1

    direcL[headR][headC]=forward
    '''
    for i in direcL:
        print(i)
    '''
    if not isEat:
        game[tailR][tailC]=0
        if direcL[tailR][tailC]==0:
            tailR-=1
        elif direcL[tailR][tailC]==1:
            tailC+=1
        elif direcL[tailR][tailC]==2:
            tailR+=1
        else:
            tailC-=1

print(time)