M,N=map(int,input().split())
L=[]
for i in range(M):
    L.append(list(input()))

wordL=[]
#가로확인
nowWord=""
for i in range(M):
    for j in range(N):
        #끝내야하는경우(벽이거나 끝이거나)
        if L[i][j]=="#":
            if len(nowWord)>=2:
                wordL.append(nowWord)
                nowWord=""
            else:
                nowWord=""
        elif j==N-1:
            nowWord+=L[i][j]
            if len(nowWord)>=2:
                wordL.append(nowWord)
                nowWord=""
            else:
                nowWord=""
        else:
            nowWord+=L[i][j]
#세로확인
nowWord=""
for j in range(N):
    for i in range(M):
        #끝내야하는경우(벽이거나 끝이거나)
        if L[i][j]=="#":
            if len(nowWord)>=2:
                wordL.append(nowWord)
                nowWord=""
            else:
                nowWord=""
        elif i==M-1:
            nowWord+=L[i][j]
            if len(nowWord)>=2:
                wordL.append(nowWord)
                nowWord=""
            else:
                nowWord=""
        else:
            nowWord+=L[i][j]

wordL.sort()
print(wordL[0])