def measure(a):
    for i in range(1,a+1):
        if(a%i==0):
            print(i,end=' ')


measure(int(input()))
        



'''
<다른사람답>
k=int(input())
[print(f'{i} ',end='')for i in range(1,k+1)if k%i==0]
'''

'''
<내답> 마지막에 왜 None? : 프린트를 2번했기때문...숫자가 나오고 빈칸이 한번더 입력되었기 때문에(end=' ')
def measure(a):
    for i in range(1,a+1):
        if(a%i==0):
            print(i,end=' ')


print(measure(int(input())))
'''