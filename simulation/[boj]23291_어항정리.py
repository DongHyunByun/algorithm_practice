N,K = map(int,input().split())
L=list(map(int,input().split()))

def plus_one_max(L):
    min_num = min(L)
    for i,num in enumerate(L):
        if num==min_num:
            L[i]+=1
    return L

def get_list_2d(nowL,x,y):
    left_list = []
    right_list = []
    for i in range(y):
        left_list.append(nowL[i][:x])
        right_list.append(nowL[i][x:])
    return left_list,right_list

def spin(L):
    stage=1
    x,y=1,1
    while(1):
        left_list,right_list = get_list_2d(L,x,y)

        # print("spin!")
        spined_left_list = list(map(list,zip(*left_list[::-1])))
        # for i in spined_left_list:
        #     print(i)
        # for i in right_list:
        #     print(i)

        # print("fill zero")
        right_size = len(right_list[0])
        left_size = len(spined_left_list[0])
        plus_size = right_size-left_size
        fill_spined_left_list = []
        for now_row in spined_left_list:
            fill_spined_left_list.append(now_row+[0 for _ in range(plus_size)])
            # print(now_row+[0 for _ in range(plus_size)])

        # print("합친후")
        fill_spined_left_list.append(right_list[-1])
        L = list(fill_spined_left_list)
        # for i in L:
        #     print(i)

        # 크기 및 횟수 +1
        if stage%2==1:
            y+=1
        else:
            x+=1

        # 종료조건 확인
        if y > len(L[0])-x:
            break
        stage+=1

    return L

def set_fish_num(L):
    dR=[0,0,-1,1]
    dC=[1,-1,0,0]

    row_size=len(L)
    col_size=len(L[0])

    diff_list = [[0 for j in range(col_size)] for i in range(row_size)]

    for i in range(row_size):
        for j in range(col_size):
            now_num = L[i][j]
            if now_num:
                for k in range(4):
                    next_i = i+dR[k]
                    next_j = j+dC[k]
                    if 0<=next_i<row_size and 0<=next_j<col_size and L[next_i][next_j] and (now_num - L[next_i][next_j])>0:
                        d = (now_num - L[next_i][next_j])//5
                        if d>0:
                            diff_list[i][j]-=d
                            diff_list[next_i][next_j]+=d

    # for i in diff_list:
    #     print(i)

    for i in range(row_size):
        for j in range(col_size):
            if L[i][j]:
                L[i][j]+=diff_list[i][j]

    return L

def set_one_row(L):
    row_size = len(L)
    col_size = len(L[0])

    final_list = []
    for j in range(col_size):
        for i in range(row_size-1,-1,-1):
            if L[i][j]:
                final_list.append(L[i][j])
    return final_list

def half_spin(L):
    size = len(L)
    left_list = L[:size//2]
    right_list = L[size//2:]

    list_2d = [list(reversed(left_list)),right_list]

    left_list, right_list = get_list_2d(list_2d, size//4, 2)
    for _ in range(2):
        left_list = list(map(list,zip(*left_list[::-1])))

    for right_row in right_list:
        left_list.append(right_row)

    return left_list

def is_fin(L,K):
    if (max(L)-min(L))<=K:
        return True
    else:
        return False

def print_list(L):
    print("=================")
    for i in L:
        print(i)

ans=1
while(1):
    # print(ans,"번째 start!")
    L = plus_one_max(L)
    L = spin([L])
    L = set_fish_num(L)
    L = set_one_row(L)
    L = half_spin(L)
    L = set_fish_num(L)
    L = set_one_row(L)

    if is_fin(L,K):
        print(ans)
        break
    else:
        ans+=1