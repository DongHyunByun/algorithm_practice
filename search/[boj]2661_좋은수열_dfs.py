import sys

def dfs(nowNum,size):
    if size==N:
        print(nowNum)
        sys.exit()
    size+=1
    #숫자 하나씩 추가해보기
    for num in ["1","2","3"]:
        newNum=nowNum+num
        isPossible=True
        for i in range(1,size//2+1):
            back=newNum[size-i:]
            front=newNum[size-2*i:size-i]
            if back==front:
                isPossible=False
                break
        if isPossible:
            dfs(newNum,size)

N = int(input())
dfs("",0)
