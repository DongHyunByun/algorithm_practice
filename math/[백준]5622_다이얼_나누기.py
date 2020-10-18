word=input()

ans=0
for c in word:
    num=ord(c)-ord("A")
    if num<=17:
        ans+=num//3+3
    elif num==18:
        ans+=8
    elif 19<=num<22:
        ans+=9
    else:
        ans+=10


print(ans)