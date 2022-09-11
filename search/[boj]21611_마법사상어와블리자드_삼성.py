from collections import deque
dR=[0,-1,1,0,0]
dC=[0,0,0,-1,1]

pull_dR=[0,1,0,-1]
pull_dC=[-1,0,1,0]

N,M=map(int,input().split())
L=[]
for i in range(N):
    L.append(list(map(int,input().split())))

magic=[]
for i in range(M):
    d,s = map(int,input().split())
    magic.append((d,s))

def shark_break(d,s):
    sharkR, sharkC = N // 2, N // 2
    for k in range(1,s+1):
        nextR=sharkR+dR[d]*k
        nextC=sharkC+dC[d]*k
        L[nextR][nextC]=0

def get_order():
    d=0
    r=N//2
    c=N//2

    nums=[]

    for s in range(1,N):
        for _ in range(1,s+1):
            r = r + pull_dR[d]
            c = c + pull_dC[d]
            if L[r][c]:
                nums.append(L[r][c])

        d = (d+1)%4

        for _ in range(1,s+1):
            r = r + pull_dR[d]
            c = c + pull_dC[d]
            if L[r][c]:
                nums.append(L[r][c])

        d = (d + 1) % 4

    # 마지막
    for _ in range(1, N):
        r = r + pull_dR[d]
        c = c + pull_dC[d]

        if L[r][c]:
            nums.append(L[r][c])

    return nums

def pulling(nums):
    d = 0
    r = N // 2
    c = N // 2
    nums = deque(nums)

    for s in range(1, N):
        for _ in range(1, s + 1):
            r = r + pull_dR[d]
            c = c + pull_dC[d]
            if nums:
                L[r][c] = nums.popleft()
            else:
                L[r][c] = 0

        d = (d + 1) % 4

        for _ in range(1, s + 1):
            r = r + pull_dR[d]
            c = c + pull_dC[d]
            if nums:
                L[r][c] = nums.popleft()
            else:
                L[r][c] = 0

        d = (d + 1) % 4

    # 마지막
    for _ in range(1, N):
        r = r + pull_dR[d]
        c = c + pull_dC[d]
        if nums:
            L[r][c] = nums.popleft()
        else:
            L[r][c] = 0

def boom(nums):
    preNum = nums[0]
    tempL = [preNum]
    cnt = 1
    size = len(nums)
    newNums=[]
    for i in range(1, size):
        num = nums[i]
        if num == preNum:
            cnt += 1
            tempL.append(num)
        else:
            if cnt >= 4:
                ans[preNum] += cnt
            else:
                newNums.extend(tempL)
            cnt=1
            tempL = [num]
            preNum = num

    if cnt>=4:
        ans[num] += cnt
    else:
        newNums.extend(tempL)

    return newNums

def changing(nums):
    preNum = nums[0]
    cnt = 1
    size = len(nums)
    newNums = []

    for i in range(1, size):
        num = nums[i]
        if num == preNum:
            cnt+=1
        else:
            newNums.append(cnt)
            newNums.append(preNum)

            preNum=num
            cnt=1

    newNums.append(cnt)
    newNums.append(preNum)

    return newNums

ans = [0,0,0,0]
for d,s in magic:
    # 1.상어파괴
    shark_break(d,s)
    # 2.당기기
    nums = get_order()
    if not nums:
        break
    pulling(nums)
    # print("====상어파괴후=====")
    # for i in L:
    #     print(i)

    # 3.폭발
    nums = get_order()
    while(1):
        newNums = boom(nums)
        if nums==newNums:
            break
        nums=list(newNums)
        if not nums:
            break
    if not nums:
        break
    pulling(nums)
    # print("====폭발후=====")
    # for i in L:
    #     print(i)

    # 4.변화
    nums = get_order()
    if not nums:
        break
    nums = changing(nums)
    pulling(nums)

    # print("====변화후=====")
    # for i in L:
    #     print(i)

a = 0
for i in range(4):
    a+=i*ans[i]
print(a)