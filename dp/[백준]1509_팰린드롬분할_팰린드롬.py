INF=9876543210

word=input()
size=len(word)
L=[[1 for j in range(size)] for i in range(size)]

# L[i][j]=1 : i에서 j가 팰린드롬이면 1
for j in range(1,size):
    for k in range(size-j):
        if word[k]==word[j+k] and L[k+1][j+k-1]==1:
            L[k][j+k]=1
        else:
            L[k][j+k]=0

minL=[i for i in range(size+1)]
for j in range(1,size):
    for i in range(j,-1,-1):
        if L[i][j]==1:
            minL[j+1]=min(minL[j+1],minL[i]+1)
        else:
            minL[j+1]=min(minL[j+1],minL[i]+j-i+1)
print(minL[size])





