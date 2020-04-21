import sys
word=input()
size=len(word)
half=size//2

#짝수면0, 홀수면1
if size%2==0:
    type=0

else:
    type=1

def isPalin(x):
    right=x+type
    left=x-1
    for i in range(size-right):
        if word[left-i]!=word[right+i]:
            return False
    return True

for i in range(half,size):
    while(type<2):
        if isPalin(i):
            print(i*2+type)
            sys.exit()
        else:
            type+=1
    type=0
