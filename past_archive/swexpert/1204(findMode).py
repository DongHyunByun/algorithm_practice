for t in range(int(input())):
    scoreByp=[]
    case=int(input())
    a=list(map(int,input().split()))
    for i in range(101):
        scoreByp.append(a.count(i)) #scoreByp[i]는 i점을가진 사람수
    k=list(reversed(scoreByp)).index(max(scoreByp))
    print(f"#{case} {100-k}")
