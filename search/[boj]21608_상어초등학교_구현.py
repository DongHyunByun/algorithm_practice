dR=[0,0,-1,1]
dC=[1,-1,0,0]

N=int(input())
s_cnt = N**2

L = [[0 for j in range(N)] for i in range(N)]
fL = [[0 for j in range(N)] for i in range(N)]

def check_sit(r,c,friend):
    blank = 0
    favor = 0
    for k in range(4):
        next_r = r+dR[k]
        next_c = c+dC[k]
        if 0<=next_r<N and 0<=next_c<N:
            if L[next_r][next_c]==0:
                blank+=1
            elif L[next_r][next_c] in friend:
                favor+=1

    return (blank,favor)

graph={0:[]}
students = []
for _ in range(s_cnt):
    a = list(map(int,input().split()))
    student = a[0]
    friend = a[1:]

    graph[student] = friend
    students.append(student)

for student in students:
    friend = graph[student]
    candi = []
    for i in range(N):
        for j in range(N):
            if L[i][j]==0:
                blank,favor= check_sit(i,j,friend)
                candi.append((-favor,-blank,i,j))

    f,b,r,c = sorted(candi)[0]
    L[r][c]=student
    # print(student,r,c)

    fL[r][c]=-f
    for k in range(4):
        next_r = r+dR[k]
        next_c = c+dC[k]
        if 0<=next_r<N and 0<=next_c<N and (student in graph[L[next_r][next_c]]):
            fL[next_r][next_c]+=1

# for i in L:
#     print(i)
# print()
# for i in fL:
#     print(i)

score_dict = {0:0,1:1,2:10,3:100,4:1000}
total = 0
for i in range(N):
    for j in range(N):
        total+=score_dict[fL[i][j]]
print(total)



