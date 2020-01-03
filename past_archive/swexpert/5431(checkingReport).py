for t in range(int(input())):
    N,K=map(int,input().split())
    studentList=[i for i in range(1,N+1)]
    ReportDoneList=list(map(int,input().split()))
    for k in range(K):
        studentList.remove(ReportDoneList[k])
    print(f"#{t+1}",*studentList)
