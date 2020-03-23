import sys

sample=[i for i in range(1,13)]
toNum=ord("A")-1
L=[]
for i in range(5):
    L.append(input())

def isMagic(numL):
    size=len(numL)
    if size==5:
        #1확인
        if sum(numL[1:])!=26:
            return False
    if size==8:
        #2확인
        if numL[0]+numL[2]+numL[5]+numL[7]!=26:
            return False
    if size==11:
        #3,4확인
        if (sum(numL[7:])!=26 or numL[0]+numL[3]+numL[6]+numL[10]!=26):
            return False
    if size==12:
        #5,6확인
        if (numL[1]+numL[5]+numL[8]+numL[11]!=26 or numL[4]+numL[6]+numL[9]+numL[11]!=26):
            return False
    return True

#(현재까지 list,위치)
def dfs(numL,loc):
    r=loc//9
    c=loc%9
    #print(loc,numL)
    #되는지 확인해
    if not isMagic(numL):
        return

    #끝까지왔으면 출력후 종료
    if r==5:
        for i in range(5):
            for j in range(9):
                if L[i][j]!=".":
                    print(chr(numL.pop(0)+toNum),end="")
                else:
                    print(".",end="")
            print()
        sys.exit()

    #탐색
    if L[r][c]==".":
        dfs(numL,loc+1)
    else:
        if L[r][c]=="x":
            for i in sample:
                if i not in numL:
                    dfs(numL+[i],loc+1)
        else:
            addedNum=ord(L[r][c])-toNum
            if addedNum not in numL:
                dfs(numL+[ord(L[r][c])-toNum],loc+1)

dfs([],0)