N,L=map(int,input().split())

time=0
nowLoc=0
for i in range(N):
    D,R,G=map(int,input().split())
    #신호등까지시간
    time+=D-nowLoc
    #신호등에서 대기시간
    a=time%(R+G)

    if a<R:
        time+=R-a

    nowLoc=D

time+=L-nowLoc
print(time)

