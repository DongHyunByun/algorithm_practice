from collections import deque
from copy import deepcopy

dR=[0,1,0,-1]
dC=[1,0,-1,0]

N,Q = map(int,input().split())
size = 2**N

my_map=[]
for i in range(size):
    my_map.append(list(map(int,input().split())))
L=list(map(int,input().split()))


def spin_v2(now_map, l):
    def spin_box(now_map, start_r, start_c, box_size):
        box = []
        for i in range(box_size):
            box.append(now_map[start_r+i][start_c:start_c+box_size])

        spined_box = list(map(list,zip(*box[::-1])))
        for i in range(box_size):
            for j in range(box_size):
                now_map[start_r+i][start_c+j] = spined_box[i][j]

    total_size = len(now_map)

    box_cnt = total_size // (2 ** l)  # 회전이 발생하는 박스의 개수
    box_size = total_size // box_cnt  # 회전이 발생하는 박스 한개의 길이

    for i in range(box_cnt):
        for j in range(box_cnt):
            start_r = (2 ** l) * i
            start_c = (2 ** l) * j
            # print(start_r,start_c)

            spin_box(now_map, start_r, start_c, box_size)
            # for x in now_map:
            #     print(x)
            # print()

# def spin(now_map, l):
#     '''
#     문제를 잘못읽고 이상하게 짬
#     회전 작업수행
#     '''
#
#     def extract_box(now_map, start_r, start_c, a):
#         temp_total = []
#         for i in range(a):
#             temp_row = []
#             for j in range(a):
#                 temp_row.append(now_map[start_r+i][start_c+j])
#             temp_total.append(temp_row)
#         return temp_total
#
#     def push_box(new_map, start_r, start_c, a, box):
#         for i in range(a):
#             for j in range(a):
#                 new_map[start_r+i][start_c+j] = box[i][j]
#
#
#     total_size = len(now_map)
#     temp_map = [[0 for j in range(total_size)] for i in range(total_size)]
#
#     box_cnt = total_size//(2**l) # 회전이 발생하는 박스의 개수
#     box_size = total_size//box_cnt # 회전이 발생하는 박스 한개의 길이
#
#     for i in range(box_cnt):
#         for j in range(box_cnt):
#             start_r = (2**l)*i
#             start_c = (2**l)*j
#             # print(start_r,start_c)
#             for k in range(4):
#                 moving_box = extract_box(now_map, start_r, start_c, box_size//2)
#
#
#                 # for x in moving_box:
#                 #     print(x)
#                 # print()
#
#                 start_r = start_r + dR[k]*(box_size//2)
#                 start_c = start_c + dC[k]*(box_size//2)
#
#                 push_box(temp_map, start_r, start_c, box_size//2, moving_box)
#
#     return temp_map

def melt(my_map):
    size = len(my_map)
    new_map = deepcopy(my_map)
    for i in range(size):
        for j in range(size):
            cnt = 0
            for k in range(4):
                r = i+dR[k]
                c = j+dC[k]

                if 0<=r<size and 0<=c<size and my_map[r][c]!=0:
                    cnt+=1
            if cnt<3 and my_map[i][j]>0:
                new_map[i][j]-=1
    return new_map

def find_biggist(my_map):
    size = len(my_map)
    visited=[[-1 for j in range(size)] for i in range(size)]
    biggist = 0

    for i in range(size):
        for j in range(size):
            if my_map[i][j]!=0 and visited[i][j]==-1:
                cnt=0
                q = deque([(i,j)])
                visited[i][j]=1

                while(q):
                    r,c = q.popleft()
                    cnt+=1
                    for k in range(4):
                        next_r = r+dR[k]
                        next_c = c+dC[k]

                        if 0<=next_r<size and 0<=next_c<size and visited[next_r][next_c]==-1 and my_map[next_r][next_c]!=0:
                            visited[next_r][next_c] = 1
                            q.append((next_r,next_c))

                if biggist<cnt:
                    biggist = cnt

    return biggist

for l in L:
    # print(l)
    if l!=0:
        spin_v2(my_map,l)
        # print("돌려")
        # for i in my_map:
        #     print(i)

    my_map = melt(my_map)
    # print("녹여")
    # for i in my_map:
    #     print(i)

print(sum([sum(i) for i in my_map]))
print(find_biggist(my_map))