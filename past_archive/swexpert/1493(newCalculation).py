def andCal(a):
    i=1
    while (pow(i,2)-i+2)//2 <= a :
        i+=1
    i-=1
    ini=((pow(i,2)-i+2)//2)
    x=1+(a-ini)
    y=i-(a-ini)
    return [x,y]

def shapCal(list):
    return ((list[0]+list[1]-2)*(list[0]+list[1]-1))//2+list[0]

for t in range(int(input())):
    p,q=map(int,input().split())
    print(f"#{t+1} {shapCal([andCal(p)[0]+andCal(q)[0],andCal(p)[1]+andCal(q)[1]])}")

