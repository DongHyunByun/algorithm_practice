from math import ceil
def solution(progresses, speeds):
    #완료시간저장 list
    timeL=[]
    #배포되는 갯수
    numOfReturn=1

    ansL=[]
    for i in range(len(progresses)):
        timeL.extend([ceil((100-progresses[i])/speeds[i])])
    maxTime=timeL[0]
     
    for i in range(1,len(progresses)):
        if timeL[i]>maxTime:
            ansL.extend([numOfReturn])
            numOfReturn=1
            maxTime=timeL[i]
        else:
            numOfReturn+=1
            if i==len(progresses)-1:
                ansL.extend([numOfReturn])
    return ansL