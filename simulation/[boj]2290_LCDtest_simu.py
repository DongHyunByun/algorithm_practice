s,n=input().split()
s=int(s)
size=len(n)
board=[[" " for j in range((s+2)*size+size)] for i in range(2*s+3)]

#c열기준 p부분 칠하기
def part(c,p):
    if p==0:
        for j in range(s):
            board[0][c+1+j]="-"
    elif p==1:
        for i in range(s):
            board[1+i][c]="|"
    elif p==2:
        for i in range(s):
            board[1+i][c+s+1]="|"
    elif p==3:
        for j in range(s):
            board[s+1][c+1+j]="-"
    elif p==4:
        for i in range(s):
            board[s+2+i][c]="|"
    elif p==5:
        for i in range(s):
            board[s+2+i][c+s+1]="|"
    else:
        for j in range(s):
            board[2*s+2][c+1+j]="-"

#c번째숫자, col에서 시작
def draw(c,col):
    drawPart=[]
    if n[c]=="0":
        drawPart=[0,1,2,4,5,6]
    elif n[c]=="1":
        drawPart=[2,5]
    elif n[c]=="2":
        drawPart=[0,2,3,4,6]
    elif n[c]=="3":
        drawPart=[0,2,3,5,6]
    elif n[c]=="4":
        drawPart=[1,3,2,5]
    elif n[c]=="5":
        drawPart=[0,1,3,5,6]
    elif n[c]=="6":
        drawPart=[0,1,3,4,5,6]
    elif n[c]=="7":
        drawPart=[0,2,5]
    elif n[c]=="8":
        drawPart=[0,1,2,3,4,5,6]
    elif n[c]=="9":
        drawPart=[0,1,2,3,5,6]
    for i in drawPart:
        part(col,i)

for c in range(size):
    draw(c,(s+3)*c)

for i in board:
    print("".join(i[:(s+2)*size+size-1]))