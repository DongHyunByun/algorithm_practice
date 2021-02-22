N=int(input())
L=[]
dR=[0,1,0,-1]
dC=[-1,0,1,0]

for i in range(N):
    L.append(list(map(int,input().split())))

d=0
r=N//2
c=N//2

start=sum([sum(L[i]) for i in range(N)])

def cheak(r,c):
    if 0<=r<N and 0<=c<N:
        return True
    else:
        return False

#55
def wind(r,c,d):
    sand=L[r][c]
    #왼쪽
    leftD=(d+1)%4
    tempR,tempC=r+dR[leftD],c+dC[leftD]
    if cheak(tempR,tempC):
        L[tempR][tempC]+=int(sand*0.07)

    #왼쪽 앞왼뒤
    p=[0.1,0.02,0.01]
    for i in range(3):
        tempR2,tempC2=tempR+dR[(d+i)%4],tempC+dC[(d+i)%4]
        if cheak(tempR2,tempC2):
            L[tempR2][tempC2]+=int(sand*p[i])

    #오른쪽
    rightD=(d+3)%4
    tempR,tempC=r+dR[rightD],c+dC[rightD]
    if cheak(tempR,tempC):
        L[tempR][tempC]+=int(sand*0.07)

    #오른쪽 앞왼뒤
    p=[0.1,0.02,0.01]
    for i in range(3):
        tempR2,tempC2=tempR+dR[d-i],tempC+dC[d-i]
        if cheak(tempR2,tempC2):
            L[tempR2][tempC2]+=int(sand*p[i])

    # 정방향
    tempR, tempC = r + 2 * dR[d], c + 2 * dC[d]
    if cheak(tempR, tempC):
        L[tempR][tempC] += int(sand * 0.05)

    tempR, tempC = r + dR[d], c + dC[d]
    if cheak(tempR, tempC):
        blow=(int(sand*0.1)*2+int(sand*0.07)*2+int(sand*0.02)*2+int(sand*0.01)*2+int(sand*0.05))
        remain=sand-blow
        L[tempR][tempC] += remain

for i in range(1,N):
    #2번씩 반복
    for j in range(2):
        #i번이동
        for k in range(i):
            r=r+dR[d]
            c=c+dC[d]
            wind(r,c,d)
            L[r][c]=0
        d=(d+1)%4

#마지막반복
for k in range(N-1):
    r=r+dR[d]
    c=c+dC[d]
    wind(r,c,d)
    L[r][c]=0

fin=sum([sum(L[i]) for i in range(N)])


print(start-fin)