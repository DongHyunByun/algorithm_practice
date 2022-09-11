from collections import deque

dR=[0,0,-1,1]
dC=[1,-1,0,0]

N,M=map(int,input().split())

L=[]
for i in range(N):
    L.append(list(map(int,input().split())))

def get_score():
    group_dict = {}

    visited = [[-1 for j in range(N)] for i in range(N)]

    # bfs
    for i in range(N):
        for j in range(N):
            if visited[i][j]==-1 and L[i][j]>=1:
                visited_rainbow = [[-1 for _ in range(N)] for _ in range(N)]
                cnt = 1
                rainbow = 0
                stand_r = i
                stand_c = j
                t = L[stand_r][stand_c]
                group = [(stand_r,stand_c)]

                visited[stand_r][stand_c]=1
                q = deque([(stand_r,stand_c)])
                while(q):
                    r,c = q.popleft()
                    for k in range(4):
                        next_r = r+dR[k]
                        next_c = c+dC[k]
                        if 0<=next_r<N and 0<=next_c<N and visited[next_r][next_c]==-1:
                            if L[next_r][next_c]==t:
                                cnt+=1
                                group.append((next_r, next_c))

                                visited[next_r][next_c] = 1
                                q.append((next_r,next_c))
                            elif L[next_r][next_c]==0 and visited_rainbow[next_r][next_c]==-1:
                                cnt+=1
                                group.append((next_r, next_c))
                                rainbow+=1

                                visited_rainbow[next_r][next_c]=1
                                q.append((next_r, next_c))


                if cnt>=2:
                    group_dict[(-cnt,-rainbow,-stand_r,-stand_c)]=group

    # print(group_dict)
    # for i in visited:
    #     print(i)
    # for i in visited_rainbow:
    #     print(i)

    # 획득점수
    if group_dict:
        picked_key = sorted(group_dict)[0]
        score = (-picked_key[0])**2

        # 지우기
        erase_group = group_dict[picked_key]
        for i, j in erase_group:
            L[i][j] = -2

        return score
    else:
        return 0

def gravity():
    for j in range(N):
        for i in range(N-1,-1,-1):
            if L[i][j]>=0:
                next_i = i
                for k in range(i+1,N):
                    if L[k][j]==-2:
                        next_i=k
                    else:
                        break

                if next_i!=i:
                    L[next_i][j] = L[i][j]
                    L[i][j]=-2

total_score = 0
while(1):
    score = get_score()
    if score:
        total_score+=score
    else:
        break
    gravity() # 중력
    L = list(map(list,zip(*L)))[::-1]
    gravity()

print(total_score)






