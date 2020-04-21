from collections import deque
T=int(input())
#붙은면(시계방향순,"(붙은면)(돌아가는num)(시계방향일때저장순서)(반시계일때저장순서)")
near={"U":["B011","R011","F011","L011"],
      "D":["F211","R211","B211","L211"],
      "L":["U312","F311","D321","B122"],
      "R":["U121","B322","D112","F111"],
      "F":["U212","R321","D012","L121"],
      "B":["U021","L312","D221","R112"]}

# side면의 num방향에 색깔 3개를 얻음
def get(side,num,rev):
    if num=="0":
        temp=list(cube[side][0])
    elif num=="1":
        temp=list([cube[side][i][2] for i in range(3)])
    elif num=="2":
        temp=list(cube[side][2])
    else:
        temp=list([cube[side][i][0] for i in range(3)])

    if rev=="1":
        return temp
    else:
        return list(reversed(temp))

# side면의 num방향에 색깔 3개를 새로칠함
def write(side,num,newColor):
    if num=="0":
        cube[side][0]=newColor
    elif num=="1":
        for i in range(3):
            cube[side][i][2]=newColor[i]
    elif num=="2":
        cube[side][2]=newColor
    else:
        for i in range(3):
            cube[side][i][0]=newColor[i]

def do(side,turn):
    #해당면 회전
    #시계방향
    if turn=="+":
        cube[side]=list(map(list,zip(*cube[side][::-1])))
    #반시계방향
    else:
        for i in range(3):
            cube[side]=list(map(list,zip(*cube[side][::-1])))

    #주변회전
    if turn=="+":
        orderL=list(near[side])
        reverIndx=2
    else:
        orderL=list(reversed(near[side]))
        reverIndx=3
    side=orderL[-1][0]
    num=orderL[-1][1]
    rever=orderL[-1][reverIndx]
    q=deque([get(side,num,rever)])

    for i in range(4):
        #print(q)
        #현재위치 q에넣기
        side=orderL[i][0]
        num=orderL[i][1]
        rever=orderL[i][reverIndx]
        q.append(get(side,num,rever))
        #이전에있는 q 현재위치에 넣기
        temp=q.popleft()
        write(side,num,temp)

for t in range(T):
    # 큐브
    cube = {"U": [["w" for j in range(3)] for i in range(3)],
            "D": [["y" for j in range(3)] for i in range(3)],
            "L": [["g" for j in range(3)] for i in range(3)],
            "R": [["b" for j in range(3)] for i in range(3)],
            "F": [["r" for j in range(3)] for i in range(3)],
            "B": [["o" for j in range(3)] for i in range(3)]}

    n=int(input())
    L=input().split()
    for a in L:
        #print(a)
        do(a[0],a[1])
        '''
        for alpa in ["U","D","L","R","F","B"]:
            print(alpa)
            for i in cube[alpa]:
                print(i)
        '''
    for a in cube["U"]:
        print("".join(a))
