

def maxiValue(volume,index,value):
    global maxForPrune

    if index==N:
        if maxForPrune<value:
            maxForPrune=value
        return 
    
    
    #가지치기
    lastValue=0
    for i in range(index+1,N):
        lastValue+=listOfThing[i][1]
    if (value+lastValue<maxForPrune):
        return 

    #고르는경우or안고르는경우
    if volume+listOfThing[index][0]<=K:
        maxiValue(volume+listOfThing[index][0],index+1,value+listOfThing[index][1])
    maxiValue(volume,index+1,value)

    

ansL=[]

for t in range(int(input())):
    #부피0 가치1
    listOfThing=[]

   
    

    N,K=map(int,input().split())
    for i in range(N):
        listOfThing.append(list(map(int,input().split())))
    
    maxForPrune=0
    maxiValue(0,0,0)
    ansL.append(maxForPrune)
    

for t in range(len(ansL)):
    print(f"#{t+1} {ansL[t]}")
