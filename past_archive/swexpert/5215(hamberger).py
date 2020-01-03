def linearSearch(cal,index):
    if index==N:
        return 0
    unpick=linearSearch(cal,index+1)
    pick=0
    if cal+foodList[index][1]<L:
        pick=linearSearch(cal+foodList[index][1],index+1)+foodList[index][0]
    return max(pick,unpick)
 
 
 
 
for t in range(int(input())):
    foodList=[]
    N,L=map(int,input().split())
    for i in range(N):
        foodList.append(list(map(int,input().split())))
    print(f"#{t+1} {linearSearch(0,0)}")