N=int(input())
L=[]
for i in range(N):
    L.append(list(map(int,input().split())))

ans=[0,0,0]

# L이 -1 or 0 or 1로만 되있는가
def cheak(r,c,size):
    num=L[r][c]
    for i in range(size):
        for j in range(size):
            if L[r+i][c+j]!=num:
                return 2
    return num

def dfs(r,c,size):
    #print(r,c,size)
    # (1)만족?
    number=cheak(r,c,size)
    if number in [-1,0,1]:
        ans[number]+=1
        return
    # (1)만족안하면 나누기
    divided=size//3
    for i in range(3):
        for j in range(3):
            dfs(r+i*divided,c+j*divided,divided)

dfs(0,0,N)
print(ans[-1])
print(ans[0])
print(ans[1])



