import math

X=int(input())
word=list(input())
wordSize=len(word)
wordL=[list(word)]

#주기를 구하자
pe=1
while(1):
    for i in range(math.ceil(wordSize/2)-1):
        temp=word.pop()
        word.insert(2*i+1,temp)

    if wordL[0]!=word:
        pe+=1
        wordL.append(list(word))
    else:
        break

X=X%pe
for i in range(wordSize):
    print(wordL[(pe-X)%pe][i],end="")


