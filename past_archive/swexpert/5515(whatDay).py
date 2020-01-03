
date=[31,29,31,30,31,30,31,31,30,31,30,31] #n달의 index:n-1
for t in range(int(input())):
    m,d=map(int,input().split())
    sumOfDate=sum(date[0:m-1])+d
    ans=sumOfDate%7
    if ans>=4:
        print(f"#{t+1} {ans-4}")
    else :
        print(f"#{t+1} {ans+3}")