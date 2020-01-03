# 2*2부수기
def breakW(m,n,board):
    isbreak=False
    rowNum=[]
    colNum=[]
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j]!=0 and board[i][j]==board[i][j+1] and board[i][j]==board[i+1][j] and board[i][j]==board[i+1][j+1]:
                isbreak=True
                rowNum.append(i)
                colNum.append(j)
    
    for i in range(len(rowNum)):
        board[rowNum[i]][colNum[i]]=0
        board[rowNum[i]+1][colNum[i]]=0
        board[rowNum[i]][colNum[i]+1]=0
        board[rowNum[i]+1][colNum[i]+1]=0
        
    return isbreak

def getdown(m,n,board):
    for j in range(n):
        blockL=[]
        for i in range(m):
            if board[i][j]!=0:
                blockL.append(board[i][j])

        for i in range(len(blockL)):
            board[m-1-i][j]=blockL[len(blockL)-1-i]

        for i in range(m-len(blockL)):
            board[i][j]=0


   


def solution(m, n, board):

    for i in range(m):
        board[i]=list(board[i])

    
    while(breakW(m,n,board)):
        getdown(m,n,board)
        
    
    ans=0
    for i in range(m):
        for j in range(n):
            if board[i][j]==0:
                ans+=1
    
    return ans


solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])