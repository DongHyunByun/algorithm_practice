from collections import deque

S = int(input())
maxNum=1001
visited=[[-1 for j in range(maxNum)] for i in range(maxNum)]

cnt=1
t = 0
clip = 0
visited[cnt][clip]=t
q = deque([(cnt,clip,t)])

while(q):
    cnt,clip,t = q.popleft()
    # print(cnt,clip,t)
    # print(visited)

    if cnt==S:
        print(t)
        break

    # 복사한게 있으면 붙여넣기
    if clip:
        if cnt+clip<maxNum and clip<maxNum and visited[cnt+clip][clip]==-1:
            visited[cnt+clip][clip]=t+1
            q.append((cnt+clip,clip,t+1))

    # 복사하기
    if cnt<maxNum and visited[cnt][cnt]==-1:
        visited[cnt][cnt] = t+1
        q.append((cnt,cnt,t+1))

    # 하나삭제
    if 0<=cnt-1 and visited[cnt-1][clip]==-1:
        visited[cnt-1][clip] = t+1
        q.append((cnt-1,clip,t+1))