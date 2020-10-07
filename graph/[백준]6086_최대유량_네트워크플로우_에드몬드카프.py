N, M, r, c, K = map(int, input().split())
L = []
for _ in range(N):
    L.append(list(map(int, input().split())))
com = list(map(int, input().split()))
dice = [0 for _ in range(6)]
head = 1
east = 3

moveUp = [{3: 1, 1: 2, 2: 4, 4: 3}, {0: 3, 2: 0, 3: 5, 5: 2}, {0: 1, 1: 5, 4: 0, 5: 4}, {0: 4, 1: 0, 5: 1, 4: 5},
          {0: 2, 2: 5, 3: 0, 5: 3}, {1: 3, 2: 1, 3: 4, 4: 2}]
moveDown = [{} for _ in range(6)]
for i in range(6):
    for j in moveUp[i]:
        moveDown[i][j] = 5 - moveUp[i][j]

for move in com:
    # 위
    if move == 3:
        if r == 0:
            continue
        else:
            r -= 1
            head = moveUp[head][east]
    # 아래
    elif move == 4:
        if r == N - 1:
            continue
        else:
            r += 1
            head = moveDown[head][east]
    # 왼쪽
    elif move == 2:
        if c == 0:
            continue
        else:
            c -= 1
            head, east = east, 5 - head
    # 오른쪽
    else:
        if c == M - 1:
            continue
        else:
            c += 1
            head, east = 5 - east, head
    print(dice[head])

    # 바닥이 0일때
    if L[r][c] == 0:
        L[r][c] = dice[5 - head]
    # 주사위바닥이 0일때
    else:
        dice[5 - head] = L[r][c]
        L[r][c] = 0

    for i in L:
        print(i)

    print("*",dice[0],"*")
    print(dice[2],dice[1],dice[3])
    print("*",dice[5],"*")
    print("*",dice[4],"*")
