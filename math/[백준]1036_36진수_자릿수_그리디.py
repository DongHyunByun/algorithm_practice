N=int(input())
L=[]
for i in range(N):
    L.append(input())
K=int(input())
digit=[[i,0] for i in range(36)]

def toThree(num):
    if num<10:
        return str(num)
    else:
        return chr(num-10+65)

def toAns(num):
    ans=""
    while(num//36):
        remain=toThree(num%36)
        ans=remain+ans
        num=num//36
    ans=toThree(num)+ans
    return ans


def toDecimal(a):
    try:
        return int(a)
    except:
        return 10+ord(a)-ord("A")

def compare(l):
    return l[1]*35-l[1]*l[0]

# 각 숫자별 크기확안
for word in L:
    size=len(word)
    for i in range(size):
        num=toDecimal(word[size-1-i])
        digit[num][1]+=(36**i)

# 큰순서대로 정렬 후 Z로 바꾸기
digit.sort(key=compare,reverse=True)
#print(digit)
cnt=0
for i in range(36):
    if cnt == K:
        break
    if digit[i][0]!=35:
        digit[i][0]=35
        cnt+=1
#print(digit)

# 10진수 합 구하기
sumDicimal=0
for i in range(36):
    sumDicimal+=digit[i][0]*digit[i][1]


print(toAns(sumDicimal))
