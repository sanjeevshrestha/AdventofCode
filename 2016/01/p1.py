d=raw_input().split(", ")
r=[0]*4
c=0
for x in d:
    c+=(1 if x[0]=='L' else -1)
    r[c%4]+=int(x[1:])
print abs(r[0]-r[2])+abs(r[1]-r[3])