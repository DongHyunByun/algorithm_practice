dR=[0,0,-1,-1,-1,0,1,1,1]
dC=[0,-1,-1,0,1,1,1,0,-1]

diaR=[-1,-1,1,1]
diaC=[-1,1,-1,1]

N,M = map(int,input().split())

L=[]

for i in range(N):
    L.append(list(map(int,input().split())))

cmd=[]
for i in range(M):
    a,b = map(int,input().split())
    cmd.append([a,b])

cloud = [(N-1,0),(N-1,1),(N-2,0),(N-2,1)]

def rain(moved_cloud):
    for r,c in moved_cloud:
        L[r][c]+=1

def copy_water(moved_cloud):
    for r,c in moved_cloud:
        cnt=0
        for k in range(4):
            next_r = r+diaR[k]
            next_c = c+diaC[k]
            if 0<=next_r<N and 0<=next_c<N and L[next_r][next_c]>0:
                cnt+=1

        L[r][c]+=cnt

def get_next_cloud(moved_cloud):
    next_cloud = []
    for i in range(N):
        for j in range(N):
            if L[i][j]>=2 and ((i,j) not in moved_cloud):
                L[i][j]-=2
                next_cloud.append((i,j))

    return next_cloud

for d,s in cmd:
    moved_cloud = []
    for r,c in cloud:
        next_r = (r+dR[d]*s)%N
        next_c = (c+dC[d]*s)%N
        moved_cloud.append((next_r,next_c))

    rain(moved_cloud) # 비내리기
    copy_water(moved_cloud)
    cloud = get_next_cloud(moved_cloud)

    # print(moved_cloud)
    # print(cloud)
    # for i in L:
    #     print(i)

ans=0
for i in L:
    ans+=sum(i)
print(ans)



