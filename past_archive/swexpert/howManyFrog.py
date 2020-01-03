for t in range(int(input())):
    word=input()
    ans=True
    minimumFrog=0

    if len(word)%5!=0:
        print(f"#{t+1} -1")
        continue

    numOfFrog=[0]*(len(word)//5)
    for i in word:
        if i=="c":
            isPossible=False
            for j in range(len(numOfFrog)):
                if numOfFrog[j]==0:
                    numOfFrog[j]+=1
                    isPossible=True
                    break
            if isPossible==True:
                continue
            else:
                ans=False
                print(f"#{t+1} -1")
                break

        if i=="r":
            isPossible=False
            for j in range(len(numOfFrog)):
                if numOfFrog[j]==1:
                    numOfFrog[j]+=1
                    isPossible=True
                    break
            if isPossible==True:
                continue
            else:
                ans=False
                print(f"#{t+1} -1")
                break

        if i=="o":
            isPossible=False
            for j in range(len(numOfFrog)):
                if numOfFrog[j]==2:
                    numOfFrog[j]+=1
                    isPossible=True
                    break
            if isPossible==True:
                continue
            else:
                ans=False
                print(f"#{t+1} -1")
                break

        if i=="a":
            isPossible=False
            for j in range(len(numOfFrog)):
                if numOfFrog[j]==3:
                    numOfFrog[j]+=1
                    isPossible=True
                    break
            if isPossible==True:
                continue
            else:
                ans=False
                print(f"#{t+1} -1")
                break

        if i=="k":
            isPossible=False
            for j in range(len(numOfFrog)):
                if numOfFrog[j]==4:
                    if j>minimumFrog:
                        minimumFrog=j
                    numOfFrog[j]=0
                    isPossible=True
                    break
            if isPossible==True:
                continue
            else:
                ans=False
                print(f"#{t+1} -1")
                break

    if ans==True:
        print(f"#{t+1} {minimumFrog+1}")