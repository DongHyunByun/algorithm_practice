import sys
sys.setrecursionlimit(10**8)

N=int(input())
board=[]
for i in range(5):
    board.append(input())

sample=["###...#.###.###.#.#.###.###.###.###.###",
        "#.#...#...#...#.#.#.#...#.....#.#.#.#.#",
        "#.#...#.###.###.###.###.###...#.###.###",
        "#.#...#.#.....#...#...#.#.#...#.#.#...#",
        "###...#.###.###...#.###.###...#.###.###"]

# r,c로 시작하는 숫자를 0~9까지 비교한다.
def compare(num):
    c=num*4
    numL=[]
    for sampleNum in range(10):
        sampleC=sampleNum*4
        isPossible=True
        for i in range(5):
            for j in range(3):
                if board[i][c+j]=="#" and sample[i][sampleC+j]==".":
                    isPossible=False
                    break
            if not isPossible:
                break
        if isPossible:
            numL.append(sampleNum)
    return numL

digitL=[]
for j in range(N):
    if board[1][j*4+1]=="#" or board[3][j*4+1]=="#":
        print(-1)
        sys.exit()
    digitL.append(compare(j))

digitLSize=[len(digitL[i]) for i in range(N)]
totalCase=1
for i in digitLSize:
    totalCase*=i

total=0
for i in range(N):
    tenFold = 10 ** (N - i - 1)
    cnt=totalCase//digitLSize[i]
    for t in digitL[i]:
        total+=t*tenFold*cnt
print(total/totalCase)




