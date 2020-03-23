N=int(input())
move=input()

dR=[1,0,-1,0]
dC=[0,-1,0,1]

r=0
c=0
rot=0
point=[[0,0]]
for i in move:
    if i=="F":
        r+=dR[rot]
        c+=dC[rot]
        point.append([r,c])
    elif i=="R":
        rot=(rot+1)%4
    else:
        rot=(rot-1)%4

a=50
b=-50
c=50
d=-50
for row,col in point:
    if row<a:
        a=row
    if row>b:
        b=row
    if col<c:
        c=col
    if col>d:
        d=col


for i in range(a,b+1):
    for j in range(c,d+1):
        if [i,j] in point:
            print(".",end="")
            point.remove([i,j])
        else:
            print("#",end="")
    print()
