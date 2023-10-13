from copy import deepcopy
from collections import deque

def main():
    f_dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
    f_dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]

    M, S = map(int, input().split())
    L = [[[] for j in range(5)] for i in range(5)]
    for i in range(M):
        fx, fy, d = map(int, input().split())
        L[fx][fy].append(d)

    sx, sy = map(int, input().split())

    def fish_move():
        new_L = [[[] for j in range(5)] for i in range(5)]

        for fx in range(5):
            for fy in range(5):
                for d in L[fx][fy]:
                    is_move=False
                    for k in range(1,9):
                        next_direct = (d-k)%8+1
                        next_fx = fx + f_dr[next_direct]
                        next_fy = fy + f_dc[next_direct]
                        if 1<=next_fx<=4 and 1<=next_fy<=4 and (not shark_smell_L[next_fx][next_fy]) and ((sx,sy)!=(next_fx,next_fy)):
                            new_L[next_fx][next_fy].append(next_direct)
                            is_move=True
                            break

                    if not is_move:
                        new_L[fx][fy].append(d)

        # print("움직인후!")
        # for i in new_L:
        #     print(i)

        return new_L

    def shark_move(new_L,sx,sy):
        s_dr = [0, -1, 0, 1, 0]
        s_dc = [0, 0, -1, 0, 1]

        def dfs_shark(r,c,next_d,dir_hist,move_hist,eat_fish,visited):
            next_r = r + s_dr[next_d]
            next_c = c + s_dc[next_d]

            if 1<=next_r<=4 and 1<=next_c<=4:
                if visited[next_r][next_c]==-1:
                    now_eat_fish = len(new_L[next_r][next_c])+eat_fish
                else:
                    now_eat_fish = eat_fish
                now_dir_hist = dir_hist+str(next_d)
                now_move_hist = move_hist+[[next_r,next_c]]

                if len(dir_hist)==2:
                    shark_move_list.append([-now_eat_fish, now_dir_hist, now_move_hist])
                    return

                for k in range(1,5):
                    visited[next_r][next_c] = 1
                    dfs_shark(next_r,next_c,k,now_dir_hist,now_move_hist,now_eat_fish,visited)
                    visited[next_r][next_c] = -1

        shark_move_list = []
        visited=[[-1 for j in range(5)] for i in range(5)]
        for k in range(1,5):
            dfs_shark(sx,sy,k,"",[],0,visited)

        shark_move_list.sort()
        # print(shark_move_list)
        return shark_move_list[0][2]

        # for a in range(1,5):
        #     total_fish = 0
        #     eaten_fish,next_sx_a,next_sy_a = eat_fish(sx,sy,a)
        #     move_history = [(next_sx,next_sy)]
        #     if eaten_fish == -1:
        #         continue
        #     else:
        #         total_fish += eaten_fish
        #     for b in range(1,5):
        #         eaten_fish, next_sx, next_sy = eat_fish(next_sx, next_sy, b)
        #         if eaten_fish == -1:
        #             continue
        #         else:
        #             total_fish += eaten_fish
        #         for c in range(1,5):
        #             if eaten_fish == -1:
        #                 continue
        #             else:
        #                 total_fish += eaten_fish
        #                 move_list.append([-total_fish,int(str(a)+str(b)+str(c))])

    def check_smell(new_L,shark_move,shark_smell_L):
        for i in range(1,5):
            for j in range(1,5):
                if shark_smell_L[i][j]:
                    shark_smell_L[i][j]-=1

        for a,b in shark_move:
            if new_L[a][b]:
                # print(new_fish_list, [a,b,new_L[a][b]])
                shark_smell_L[a][b]=2
                new_L[a][b]=[]

    def copy_fish(new_L,copied_list):
        for i in range(5):
            for j in range(5):
                for copied_fish in copied_list[i][j]:
                    new_L[i][j].append(copied_fish)
        return new_L

    shark_smell_L = [[0 for j in range(5)] for i in range(5)]

    for i in range(S):
        copied_list = deepcopy(L)
        # print(f"======{i+1}번째 시작상태======")
        # print("상어는",sx,sy)
        # for i in L:
        #     print(i)

        new_L = fish_move()
        # print("물고기 이동후")
        # for i in new_L:
        #     print(i)

        dir_hist= shark_move(new_L,sx,sy)
        sx, sy = dir_hist[-1]
        check_smell(new_L, dir_hist, shark_smell_L)
        # print("상어이동후")
        # print("상어위치",sx,sy)
        # for i in new_L:
        #     print(i)
        # print("물고기냄새")
        # for i in shark_smell_L:
        #     print(i)

        L = copy_fish(new_L,copied_list)
        # print("복제후")
        # for i in L:
        #     print(i)

    ans=0
    for i in range(5):
        for j in range(5):
            ans+=len(L[i][j])
    print(ans)

# 1 10
# 1 1 1
# 4 4
# 26
main()