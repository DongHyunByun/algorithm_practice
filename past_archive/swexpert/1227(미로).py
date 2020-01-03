from collections import deque
for i in range(10):
    t=int(input())
    maze=[]
    for i in range(16):
        maze.append(list(input()))
    
    ans=0
    stack=deque([[1,1]])
    
    while stack:
        location=stack.pop()

        row=location[0]
        col=location[1]

        #3이면 종료
        if maze[row][col]=="3":
            ans=1
            break
        #방문위치는 1로
        maze[row][col]="1"
        
        #오왼위아 확인
        if maze[row+1][col]!="1":
            stack.append([row+1,col])
        if maze[row][col+1]!="1":
            stack.append([row,col+1])
        if maze[row-1][col]!="1":
            stack.append([row-1,col])
        if maze[row][col-1]!="1":
            stack.append([row,col-1])

    print(f"#{t} {ans}")
    