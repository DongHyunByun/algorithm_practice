# from collections import deque
#
# a,b = map(int,input().split())
#
# visited = [-1 for i in range(b+1)]
# visited[a]=1
# q = deque([a])
# ans=-1
#
# while(q):
#     num = q.popleft()
#     # print(num,visited[num])
#     if num==b:
#         ans=visited[num]
#         break
#
#     # 첫번째 숫자
#     first = num*2
#     if first<=b and visited[first]==-1:
#         visited[first]= visited[num]+1
#         q.append(first)
#
#     # 두번째 숫자
#     second = int(str(num)+"1")
#     if second<=b and visited[second]==-1:
#         visited[second] = visited[num]+1
#         q.append(second)
#
# print(ans)
#
#

from collections import deque

a,b = map(int,input().split())

q = deque([(a,1)])
ans=-1

while(q):
    num,cnt = q.popleft()
    # print(num,visited[num])
    if num==b:
        ans=cnt
        break

    # 첫번째 숫자
    first = num*2
    if first<=b :
        q.append((first,cnt+1))

    # 두번째 숫자
    second = int(str(num)+"1")
    if second<=b:
        q.append((second,cnt+1))

print(ans)



