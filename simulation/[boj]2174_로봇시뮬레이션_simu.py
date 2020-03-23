A,B=map(int,input().split())
N,M=map(int,input().split())
map=[[-1 for j in range(A)] for i in range(B)]
robot={}
direction=[[-1,0],[0,-1],[1,0],[0,1]]
for num in range(1,N+1):
    x,y,to=input().split()
    r=B-int(y)
    c=int(x)-1
    if to=="N":
        to=0
    elif to=="W":
        to=1
    elif to=="S":
        to=2
    else:
        to=3
    map[r][c]=to
    robot[num]=[r,c]

isCrushed=False
for i in range(M):
    '''
    print()
    for xx in range(B):
        print(map[xx])
    '''
    num,order,time=input().split()
    num=int(num)
    time=int(time)
    #로봇위치,방향
    r=robot[num][0]
    c=robot[num][1]
    startR=r
    startC=c
    to=map[r][c]
    #이동이면?
    if order=="F":
        for t in range(time):
            r+=direction[to][0]
            c+=direction[to][1]
            if 0<=r<B and 0<=c<A:
                if map[r][c]==-1:
                    continue
                #로봇과 박는경우
                else:
                    isCrushed=True
                    for robotNum in robot:
                        if r==robot[robotNum][0] and c==robot[robotNum][1]:
                            print("Robot %d crashes into robot %d"%(num,robotNum))
                            break
                    break
            #벽에 박는경우
            else:
                isCrushed=True
                print("Robot %d crashes into the wall"%(num))
                break
        if isCrushed:
            break
        else:
            map[startR][startC]=-1
            map[r][c]=to
            robot[num][0]=r
            robot[num][1]=c
    #왼쪽으로 90도회전
    elif order=="L":
        to=(to+time)%4
        map[r][c]=to
    #오른쪽으로 90도회전
    else:
        to=(to-time)%4
        map[r][c]=to

if not isCrushed:
    print("OK")