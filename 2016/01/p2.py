d=raw_input().split(', ')
v=[[0]*200 for i in range(200)]
x=y=c=0;
r=[0]*4
for j in d:
    c+=(1 if j[0]=='L' else -1)
    i=c%4
    q=int(j[1:])
    for _ in range(q):
        x+=(-1 if i==1 else 1 if i==3 else 0)
        y+=(1 if i==0 else -1 if i==2 else 0)
        r[i]=r[i]+1
        e=abs(r[0]-r[2])+abs(r[1]-r[3])
        if v[x][y]!=0:
            break
        v[x][y] = e
    else:
        continue
    break
print e